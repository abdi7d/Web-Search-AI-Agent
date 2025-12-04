'''
import streamlit as st
from main import ask

# Page config
st.set_page_config(page_title="🌐 Web Search AI Agent", page_icon="🌐")

# Custom CSS
st.markdown(
    """
    <style>
    #big-title {font-size: 32px; font-weight: 800; text-align:center;}
    #sub {font-size: 16px; text-align:center; margin-bottom:20px;}
    .user-msg {background-color:#DCF8C6; padding:8px; border-radius:8px; margin-bottom:4px;}
    .ai-msg {background-color:#F1F0F0; padding:8px; border-radius:8px; margin-bottom:4px;}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<div id='big-title'>🌐 Web Search AI Agent</div>", unsafe_allow_html=True)
st.markdown("<div id='sub'>Tavily Search + Gemini LLM Summarizer</div>", unsafe_allow_html=True)

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form
with st.form("query_form", clear_on_submit=True):
    query = st.text_input("Ask anything", placeholder="Example: Who is the richest person in the world?")
    submitted = st.form_submit_button("🔎 Search & Answer")

if submitted and query.strip():
    answer = ask(query)
    st.session_state.chat_history.append(("user", query))
    st.session_state.chat_history.append(("ai", answer))

# Display chat history
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"<div class='user-msg'>👤 {message}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='ai-msg'>🤖 {message}</div>", unsafe_allow_html=True)
'''




import streamlit as st
from main import ask

# Page config
st.set_page_config(page_title="🌐 Web Search AI Agent", page_icon="🌐")

# Avatar URLs
USER_AVATAR = "https://cdn-icons-png.flaticon.com/512/2922/2922510.png"
AI_AVATAR = "https://cdn-icons-png.flaticon.com/512/4712/4712027.png"

# Custom CSS
st.markdown(
    f"""
    <style>
    #big-title {{font-size: 32px; font-weight: 800; text-align:center;}}
    #sub {{font-size: 16px; text-align:center; margin-bottom:20px;}}
    .chat-container {{display: flex; align-items: flex-start; margin-bottom: 10px;}}
    .chat-avatar {{width: 40px; height: 40px; border-radius: 50%; margin-right: 10px;}}
    .user-msg {{background-color:#DCF8C6; padding:8px; border-radius:8px; max-width: 70%;}}
    .ai-msg {{background-color:#F1F0F0; padding:8px; border-radius:8px; max-width: 70%;}}
    </style>
    """,
    unsafe_allow_html=True,
)

# Title
st.markdown("<div id='big-title'>🌐 Web Search AI Agent</div>", unsafe_allow_html=True)
st.markdown("<div id='sub'>Tavily Search + Gemini LLM Summarizer</div>", unsafe_allow_html=True)

# Initialize chat history
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Input form
with st.form("query_form", clear_on_submit=True):
    query = st.text_input("Ask anything", placeholder="Example: Who is the richest person in the world?")
    submitted = st.form_submit_button("🔎 Search & Answer")

# Handle user query
if submitted and query.strip():
    answer = ask(query)
    st.session_state.chat_history.append(("user", query))
    st.session_state.chat_history.append(("ai", answer))

# Display chat history with avatars
for sender, message in st.session_state.chat_history:
    if sender == "user":
        st.markdown(
            f"""
            <div class="chat-container">
                <img src="{USER_AVATAR}" class="chat-avatar">
                <div class="user-msg">👤 {message}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f"""
            <div class="chat-container">
                <img src="{AI_AVATAR}" class="chat-avatar">
                <div class="ai-msg">🤖 {message}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
