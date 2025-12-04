import os
import gradio as gr
from dotenv import load_dotenv
from langchain_tavily import TavilySearch
from langchain_google_genai import ChatGoogleGenerativeAI

# Load ENV
load_dotenv()

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

# Initialize Tavily Search Tool
tavily_tool = TavilySearch(
    api_key=os.getenv("TAVILY_API_KEY"),
    max_results=5,
    topic="general"
)

# Web Search Function
def web_search(query):
    res = tavily_tool.invoke({"query": query})
    snippets = []
    for r in res.get("results", []):
        if r.get("content"):
            snippets.append(r["content"])
        else:
            snippets.append(r.get("title", "") + " — " + r.get("url", ""))
    return snippets


# Ask Function (Search + Summarize)
def ask(query, history):
    if not query.strip():
        return "❗ Please enter a question.", history

    history = history or []

    # STEP 1: Web search
    search_results = web_search(query)
    context = "\n\n".join(search_results)

    # STEP 2: Summarize using Gemini
    llm_response = llm.invoke(
        f"You are an expert AI. Use the web data if available. "
        f"If data is missing, use your internal knowledge.\n\n"
        f"USER QUESTION:\n{query}\n\n"
        f"WEB DATA:\n{context}"
    )

    final_answer = llm_response.content if hasattr(llm_response, "content") else llm_response

    # Save history
    history.append((query, final_answer))

    return final_answer, history


# -----------------------------#
#       GRADIO INTERFACE       #
# -----------------------------#
css = """
#big-title {font-size: 32px; font-weight: 800; text-align:center;}
#sub {font-size: 16px; text-align:center; margin-bottom:20px;}
"""

with gr.Blocks(css=css, theme=gr.themes.Soft()) as demo:

    gr.HTML("<div id='big-title'>🌐 Web Search AI Agent</div>")
    gr.HTML("<div id='sub'>Tavily Search + Gemini LLM Summarizer</div>")

    with gr.Row():
        with gr.Column(scale=2):
            query = gr.Textbox(
                label="Ask anything",
                placeholder="Example: Who is the current richest person in the world?",
            )
            ask_btn = gr.Button("🔎 Search & Answer")
        
            final_answer = gr.Markdown("## 🧠 Final Answer will appear here")

        with gr.Column(scale=1):
            history_state = gr.State([])
            history_display = gr.Chatbot(label="Search History")

    ask_btn.click(
        ask,
        inputs=[query, history_state],
        outputs=[final_answer, history_state],
    ).then(
        lambda h: h,
        inputs=history_state,
        outputs=history_display
    )

# Run app
if __name__ == "__main__":
    demo.launch()
