# app.py

import gradio as gr
from main import ask

css = """
<style>
#big-title {font-size: 32px; font-weight: 800; text-align:center;}
#sub {font-size: 16px; text-align:center; margin-bottom:20px;}
</style>
"""

def gradio_ask(query, chat_history):
    if not query.strip():
        return "", chat_history

    answer = ask(query)
    chat_history = chat_history or []
    chat_history.append((query, answer))  # tuple = (user_message, ai_response)
    return "", chat_history


with gr.Blocks() as demo:

    gr.HTML(css)
    gr.HTML("<div id='big-title'>🌐 Web Search AI Agent</div>")
    gr.HTML("<div id='sub'>Tavily Search + Gemini LLM Summarizer</div>")

    with gr.Row():
        with gr.Column(scale=2):
            query = gr.Textbox(
                label="Ask anything",
                placeholder="Example: Who is the richest person in the world?",
            )
            ask_btn = gr.Button("🔎 Search & Answer")

        with gr.Column(scale=2):
            chatbot = gr.Chatbot(
                type="messages",  # ✅ ChatGPT-style messages
                label="Chatbot",
                avatar_images=(
                    "https://cdn-icons-png.flaticon.com/512/2922/2922510.png",  # user
                    "https://cdn-icons-png.flaticon.com/512/4712/4712027.png",  # AI
                ),
                show_copy_button=True  # ✅ allows copy button per message
            )

    # Wire up the textbox + button
    ask_btn.click(
        fn=gradio_ask,
        inputs=[query, chatbot],
        outputs=[query, chatbot],
    )
    query.submit(
        fn=gradio_ask,
        inputs=[query, chatbot],
        outputs=[query, chatbot],
    )

if __name__ == "__main__":
    demo.launch()
