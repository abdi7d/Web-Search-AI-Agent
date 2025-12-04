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



