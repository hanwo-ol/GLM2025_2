import os
import requests
import shutil
from pathlib import Path
from typing import List
from pypdf import PdfReader
from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import FAISS

# Constants
REPO_OWNER = "hanwo-ol"
REPO_NAME = "GLM2025_2"
DATA_DIR = Path("data")
INDEX_DIR = Path("faiss_index")
FOLDERS_TO_INDEX = ["homework_pdfs", "lecture_pdfs"]

def fetch_file_list(folder_path: str) -> List[dict]:
    """Fetches the list of files in a specific GitHub folder."""
    url = f"https://api.github.com/repos/{REPO_OWNER}/{REPO_NAME}/contents/{folder_path}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching {folder_path}: {response.status_code}")
        return []

def download_file(url: str, save_path: Path):
    """Downloads a file from a URL to a local path."""
    response = requests.get(url, stream=True)
    if response.status_code == 200:
        with open(save_path, 'wb') as f:
            for chunk in response.iter_content(chunk_size=8192):
                f.write(chunk)
    else:
        print(f"Failed to download {url}")

def load_pdfs(data_dir: Path) -> List[Document]:
    """Loads all PDFs in the data directory and extracts text."""
    documents = []
    for pdf_file in data_dir.glob("**/*.pdf"):
        try:
            reader = PdfReader(pdf_file)
            text = ""
            for page in reader.pages:
                text += page.extract_text() + "\n"
            
            if text.strip():
                doc = Document(
                    page_content=text,
                    metadata={"source": str(pdf_file.name)}
                )
                documents.append(doc)
        except Exception as e:
            print(f"Error reading {pdf_file}: {e}")
    return documents

def build_index(api_key: str):
    """Downloads files, processes them, and builds the FAISS index."""
    if not api_key:
        raise ValueError("API Key is required")
    
    DATA_DIR.mkdir(exist_ok=True)
    
    # 1. Download Files (Overwrite logic)
    print("Fetching file list from GitHub...")
    for folder in FOLDERS_TO_INDEX:
        files = fetch_file_list(folder)
        target_dir = DATA_DIR / folder
        target_dir.mkdir(parents=True, exist_ok=True)
        
        for file_info in files:
            if file_info['name'].endswith('.pdf'):
                download_url = file_info['download_url']
                save_path = target_dir / file_info['name']
                # Always download to ensure freshness
                print(f"Downloading {file_info['name']}...")
                download_file(download_url, save_path)

    # 2. Load Documents
    print("Loading PDFs...")
    documents = load_pdfs(DATA_DIR)
    if not documents:
        print("No documents found.")
        return

    # 3. Split Text
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)
    print(f"Created {len(splits)} chunks.")

    # 4. Create Index
    print("Creating Embeddings and Index...")
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    vectorstore = FAISS.from_documents(splits, embeddings)
    
    # 5. Save Index
    vectorstore.save_local(str(INDEX_DIR))
    print("Index saved successfully.")

def get_vector_store(api_key: str):
    """Loads the existing FAISS index."""
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001", google_api_key=api_key)
    if INDEX_DIR.exists():
        return FAISS.load_local(str(INDEX_DIR), embeddings, allow_dangerous_deserialization=True)
    else:
        return None

def get_context(query: str, api_key: str) -> str:
    """Retrieves relevant context for a query."""
    vectorstore = get_vector_store(api_key)
    if not vectorstore:
        return ""
    
    docs = vectorstore.similarity_search(query, k=3)
    return "\n\n".join([doc.page_content for doc in docs])
