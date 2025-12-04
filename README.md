# 🧮 Math Chatbot powered by Gemini & RAG

이 프로젝트는 Google Gemini API (1.5 Pro)와 RAG (Retrieval-Augmented Generation) 기술을 활용한 수학 전문 챗봇입니다.  
GitHub 저장소 (`hanwo-ol/GLM2025_2`)에 있는 강의 자료와 숙제 파일들을 학습하여 답변을 제공하며, Python과 R 코드를 실행하여 정확한 계산과 시각화를 지원합니다.

## ✨ 주요 기능

*   **📚 RAG 기반 지식 검색**: `hanwo-ol/GLM2025_2` 저장소의 PDF 문서들을 자동으로 다운로드하고 색인화하여 답변의 근거로 사용합니다.
*   **💻 코드 실행 (Python & R)**:
    *   **Python**: 수학 계산 및 `matplotlib`을 이용한 그래프 그리기 지원.
    *   **R**: 통계 분석 및 시각화를 위한 R 코드 실행 지원 (`packages.txt`를 통해 Streamlit Cloud에서 R 환경 자동 구성).
*   **👁️ 멀티모달 (Vision)**: 사용자가 업로드한 수학 문제 이미지(.png, .jpg)나 PDF 문서를 분석하여 풀이합니다.
*   **📝 LaTeX 수식 지원**: 중요한 수식은 중앙 정렬(`$$...$$`), 인라인 수식은(`$...$`) 구분하여 출력하며, 엄밀한 노테이션 정의를 따릅니다.

---

## 🚀 시작하기 (로컬 실행)

### 1. 환경 설정

**⚠️ 주의:** 이 프로젝트는 **Python 3.9 이상**이 필수입니다. (`google-generativeai` 라이브러리 요구사항)

```bash
# 저장소 클론
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

# 가상환경 생성 (권장 - Python 3.9 이상 사용)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 의존성 설치
pip install -r requirements.txt
```

### 2. R 언어 설정 (선택 사항)
로컬에서 R 코드를 실행하려면 R이 설치되어 있어야 하며, 시스템 PATH에 `Rscript`가 등록되어 있어야 합니다.

### 3. 애플리케이션 실행

```bash
streamlit run app.py
```
브라우저가 열리면 `http://localhost:8501`에서 챗봇을 사용할 수 있습니다.

---

## ☁️ 배포하기 (Streamlit Cloud)

이 프로젝트는 [Streamlit Cloud](https://streamlit.io/cloud)에 최적화되어 있습니다.

1.  GitHub에 이 코드를 Push합니다.
2.  Streamlit Cloud에 로그인하고 **"New app"**을 클릭합니다.
3.  방금 Push한 저장소를 선택합니다.
4.  **Deploy!**
    *   `packages.txt`: Streamlit Cloud가 자동으로 `r-base`를 설치합니다.
    *   `runtime.txt`: Streamlit Cloud가 자동으로 Python 3.9 환경을 구성합니다.

---

## 🔧 문제 해결 (Troubleshooting)

### Q: `ERROR: No matching distribution found for google-generativeai` 오류가 발생해요.
**A:** 현재 사용 중인 Python 버전이 **3.9 미만**일 가능성이 높습니다.
1. 터미널에서 `python --version`을 입력하여 버전을 확인하세요.
2. 만약 3.8 이하라면, [Python 공식 홈페이지](https://www.python.org/downloads/)에서 3.9 이상의 버전을 설치하세요.
3. 기존 가상환경 폴더(`venv`)를 삭제하고, 새 버전의 Python으로 다시 가상환경을 생성해 주세요.

---

## 💡 사용 방법

1.  **API Key 입력**:
    *   앱 사이드바에 **Google Gemini API Key**를 입력합니다. (키가 없다면 [Google AI Studio](https://aistudio.google.com/)에서 발급받으세요).

2.  **지식 베이스 구축 (Build Knowledge Base)**:
    *   사이드바의 **"Build/Rebuild Knowledge Base"** 버튼을 클릭합니다.
    *   최초 1회 실행이 필요하며, GitHub에서 PDF 파일들을 다운로드하고 벡터 인덱스를 생성합니다. (시간이 조금 걸릴 수 있습니다).

3.  **질문하기**:
    *   채팅창에 수학 관련 질문을 입력합니다.
    *   **이미지/PDF 업로드**: 문제 사진이나 문서를 업로드하면 챗봇이 내용을 인식하고 풀이를 제공합니다.
    *   **코드 요청**: "이 데이터의 산점도를 R로 그려줘" 또는 "이 적분을 파이썬으로 계산해줘"와 같이 요청하면 코드를 작성하고 실행 결과를 보여줍니다.

---

## 📂 프로젝트 구조

*   `app.py`: Streamlit 메인 애플리케이션 (UI).
*   `utils/bot.py`: 챗봇 로직 (LangChain, Gemini 설정, 프롬프트 엔지니어링).
*   `utils/rag.py`: GitHub 파일 다운로드, PDF 텍스트 추출, FAISS 벡터 저장소 구축.
*   `utils/executor.py`: Python 및 R 코드 실행 엔진 (Sandbox 환경).
*   `requirements.txt`: Python 라이브러리 목록.
*   `packages.txt`: 시스템 패키지 목록 (R 설치용).
