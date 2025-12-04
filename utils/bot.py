import os
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from langchain_core.prompts import ChatPromptTemplate
from .rag import get_context
from .executor import CodeExecutor

class MathBot:
    def __init__(self, api_key: str):
        self.api_key = api_key
        # Update model to 1.5-flash or pro which supports vision better, though 'gemini-1.5-pro' is fine.
        self.llm = ChatGoogleGenerativeAI(
            model="gemini-1.5-pro",
            temperature=0.2,
            google_api_key=api_key,
            convert_system_message_to_human=True 
        )
        self.executor = CodeExecutor()
        self.chat_history = []

    def _format_history(self):
        return self.chat_history

    def generate_response(self, user_input: str, image_data: dict = None) -> str:
        """
        Generates a response to the user query using RAG, Vision, and Code Execution.
        image_data: dict with keys "mime_type" and "data" (base64 encoded or bytes) suitable for LangChain/Gemini.
        """
        
        # 1. Retrieve Knowledge (Text based RAG)
        rag_context = get_context(user_input, self.api_key)
        
        # 2. Construct System Prompt
        system_prompt = f"""You are a specialized Math Chatbot. 
        You have access to a knowledge base of mathematics documents.
        You can also execute Python and R code to solve problems, perform calculations, and create visualizations.
        
        CONTEXT FROM KNOWLEDGE BASE:
        {rag_context}
        
        INSTRUCTIONS:
        1. **Format:** Use LaTeX for all mathematical expressions.
           - For important equations, center them using double dollar signs: $$ ... $$
           - For less important or inline equations, use single dollar signs: $ ... $
        2. **Notation:** You MUST explicitly define the notation of any symbol the first time it is introduced. Be rigorous.
        3. Always try to answer using the provided context first.
        4. If the user provides an image, analyze it mathematically.
        5. If calculation or plotting is needed, generate Python or R code.
        6. To execute code, output it in a specific block:
           ```python
           # code here
           ```
           OR
           ```R
           # code here
           ```
        7. If you write R code for plotting, you MUST wrap it in:
           png('output_plot.png')
           # plot commands
           dev.off()
        8. If you write Python code for plotting, save the figure:
           plt.savefig('output_plot.png')
        9. Explain your steps clearly.
        
        Current User Question: {user_input}
        """
        
        messages = [SystemMessage(content=system_prompt)] + self.chat_history
        
        # Construct current turn message
        current_content = []
        
        # Add text
        current_content.append({"type": "text", "text": user_input})
        
        # Add image if present
        if image_data:
            # LangChain ChatGoogleGenerativeAI expects content blocks for multimodal
            # Format: {"type": "image_url", "image_url": {"url": f"data:{mime_type};base64,{data}"}}
            # Or simplified depending on version. 
            # Ideally passing the raw image data if supported, but base64 data URI is standard for this integration.
            current_content.append({
                "type": "image_url", 
                "image_url": {"url": f"data:{image_data['mime_type']};base64,{image_data['data']}"}
            })
            
        messages.append(HumanMessage(content=current_content))
        
        # Step 1: Ask LLM
        response = self.llm.invoke(messages)
        response_content = response.content
        
        # Step 2: Check for code blocks
        code_block = None
        language = None
        
        if "```python" in response_content:
            language = "python"
            code_block = response_content.split("```python")[1].split("```")[0].strip()
        elif "```R" in response_content:
            language = "R"
            code_block = response_content.split("```R")[1].split("```")[0].strip()
            
        if code_block:
            # Execute Code
            if language == "python":
                exec_result = self.executor.execute_python(code_block)
            else:
                exec_result = self.executor.execute_r(code_block)
                
            # Formulate result message
            result_msg = f"\n\n[System: Code Executed]\nOutput:\n{exec_result['output']}\nError:\n{exec_result['error']}"
            
            if exec_result['images']:
                result_msg += f"\nGenerated Images: {exec_result['images']}"
            
            # Step 3: Feed back to LLM to interpret result
            messages.append(AIMessage(content=response_content))
            messages.append(HumanMessage(content=f"Code Execution Result: {result_msg}\nPlease formulate the final answer based on this result."))
            
            final_response = self.llm.invoke(messages)
            final_text = final_response.content
            
            full_response = response_content + result_msg + "\n\n" + final_text
            
            # Update History (Flattening content for storage might be needed if simple list, 
            # but LangChain handles complex content blocks well usually. 
            # For simplicity in history display we might just store text, but for context we need the object)
            self.chat_history.append(HumanMessage(content=current_content))
            self.chat_history.append(AIMessage(content=full_response))
            
            return full_response, exec_result['images']
            
        else:
            # No code, just text
            self.chat_history.append(HumanMessage(content=current_content))
            self.chat_history.append(AIMessage(content=response_content))
            return response_content, []
