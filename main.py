import os
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI

# Load environment variables
load_dotenv()

# Initialize LLM (Gemini)
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Initialize TavilySearch tool
tavily_tool = TavilySearch(
    api_key=os.getenv("TAVILY_API_KEY"),
    max_results=5,      # number of search results
    topic="general"     # can adjust for specific domains
)

# Web search function using Tavily
def web_search(query):
    res = tavily_tool.invoke({"query": query})
    snippets = []
    for r in res.get("results", []):
        if r.get("content"):
            snippets.append(r["content"])
        else:
            # fallback to title + URL if no content
            snippets.append(r.get("title", "") + " — " + r.get("url", ""))
    return snippets

# Ask function: search + summarize
def ask(query):
    print(f"\n🔎 Searching online for: {query}")
    search_results = web_search(query)

    context = "\n\n".join(search_results)

    print("🤖 Summarizing...")
    response = llm.invoke(
        f"You are an expert AI. Use the provided data if available. "
        f"If data is missing or incomplete, answer using your own internal knowledge. "
        f"The user asked: {query}. Data from web:\n{context}"
    )

    return response

# Main interactive loop
if __name__ == "__main__":
    while True:
        user_input = input("\nAsk: ")
        if user_input.lower() in ["exit", "quit", "bye"]:
            break
        answer = ask(user_input)
        # Print only the text content
        print("\n🧠 Final Answer:", answer.content if hasattr(answer, "content") else answer)




'''
"# Web-Search-AI-Agent" 
"# Web-Search-AI-Agent" 



Here’s a clear guide for creating a GitHub repository for your project and a professional description you can use:

---

### **Steps to Create the GitHub Repository**

1. **Go to GitHub**: [https://github.com](https://github.com)

2. **Log in** to your account.

3. Click the **“+”** icon (top-right) → **New repository**.

4. **Fill in repository details**:

   * **Repository name**: `web-search-ai-agent` (or any name you prefer)
   * **Description**: *(use the text below)*
   * **Visibility**: Public or Private
   * **Initialize this repository with a README**: ✅ (optional, but recommended)

5. Click **Create repository**.

6. **Push your project files from your local machine**:
   Open terminal/command prompt in your project folder:

   ```bash
   git init
   git add .
   git commit -m "Initial commit: Add web search AI agent app"
   git branch -M main
   git remote add origin https://github.com/yourusername/web-search-ai-agent.git
   git push -u origin main
   ```

---

### **Repository Description Example**

**Short Description (visible in GitHub repo list):**

> 🌐 Web Search + AI Answer Agent using Tavily and Gemini LLM

**Project Description :**

````markdown
# Web Search + AI Answer Agent

This project is an AI-powered web search agent that combines **Tavily** search with **Google Gemini LLM** to provide summarized, accurate answers to user queries.  

### Features
- Search the web using Tavily API.
- Summarize and answer user queries using Gemini LLM.
- Simple and interactive **Gradio** interface for easy use.
- Handles incomplete or missing data gracefully by using internal LLM knowledge.

### How to Run
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
   TAVILY_API_KEY=your_api_key_here
   ```
4. Run the app:

   ```bash
   python app.py
   ```

### Screenshots

*(Add screenshots of your Gradio interface here)*

### Tech Stack

* Python
* Gradio (for UI)
* LangChain Tavily
* Google Gemini LLM

```



'''