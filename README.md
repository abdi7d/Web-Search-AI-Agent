## **Web Search AI Agent**

> 🌐 Web Search + AI Answer Agent using Tavily and Gemini LLM

### **Project Description :**


#### Web Search + AI Answer Agent

> This project is an AI-powered web search agent that combines **Tavily** search with **Google Gemini LLM** to provide summarized, accurate answers to user queries.  

#### Features
- Search the web using Tavily API.
- Summarize and answer user queries using Gemini LLM.
- Simple and interactive **Gradio** interface for easy use.
- Handles incomplete or missing data gracefully by using internal LLM knowledge.

#### How to Run
1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/web-search-ai-agent.git
   cd web-search-ai-agent 
   ````

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set environment variables in a `.env` file:

    ```env
    GOOGLE_API_KEY=your_google_api_key_here
    GROQ_API_KEY= your_groq_api_key_here (optional)
    TAVILY_API_KEY=your_api_key_here
    ```

4. Run the app:
    ```bash
    python app.py
    ```

### Screenshots

*(screenshots of Streamlit interface )*

### Tech Stack

* Python
* Streamlit (for UI)
* LangChain Tavily
* Google Gemini LLM

