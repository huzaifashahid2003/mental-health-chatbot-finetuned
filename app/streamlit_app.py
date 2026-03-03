import sys
import os

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)

import streamlit as st
from app.chatbot import get_response, get_status

st.set_page_config(
    page_title="MindEase",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&display=swap');

html, body, [data-testid="stAppViewContainer"],
[data-testid="stMain"], [data-testid="block-container"] {
    font-family: 'Inter', sans-serif !important;
    background: #1e1e2e !important;
    color: #cdd6f4 !important;
}

#MainMenu, footer, header, [data-testid="stToolbar"],
[data-testid="stSidebar"], [data-testid="collapsedControl"] {
    display: none !important;
    visibility: hidden !important;
}

.block-container {
    max-width: 680px !important;
    margin: 0 auto !important;
    padding: 2rem 1rem 8rem !important;
}

/* Header */
.chat-title {
    font-size: 1rem;
    font-weight: 500;
    color: #cdd6f4;
    text-align: center;
    padding: 1rem 0 0.25rem;
    letter-spacing: 0.01em;
}
.chat-sub {
    font-size: 0.75rem;
    color: #585b70;
    text-align: center;
    margin-bottom: 1.5rem;
}

/* Messages */
[data-testid="stChatMessage"] {
    background: transparent !important;
    border: none !important;
    padding: 0.5rem 0 !important;
    gap: 0.75rem !important;
}

[data-testid="stChatMessageContent"] {
    background: transparent !important;
}

[data-testid="stChatMessageContent"] p {
    font-size: 0.9rem !important;
    line-height: 1.7 !important;
    color: #cdd6f4 !important;
    margin: 0 !important;
}

/* User message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) {
    flex-direction: row-reverse !important;
}

[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-user"]) [data-testid="stChatMessageContent"] p {
    background: #313244 !important;
    padding: 0.65rem 1rem !important;
    border-radius: 18px 18px 4px 18px !important;
    display: inline-block !important;
    color: #cdd6f4 !important;
}

/* Bot message */
[data-testid="stChatMessage"]:has([data-testid="chatAvatarIcon-assistant"]) [data-testid="stChatMessageContent"] p {
    background: #181825 !important;
    padding: 0.65rem 1rem !important;
    border-radius: 18px 18px 18px 4px !important;
    display: inline-block !important;
    color: #cdd6f4 !important;
    border: 1px solid #313244 !important;
}

/* Avatar circles */
[data-testid="chatAvatarIcon-user"] {
    background: #89b4fa !important;
    color: #1e1e2e !important;
    border-radius: 50% !important;
    width: 32px !important;
    height: 32px !important;
}

[data-testid="chatAvatarIcon-assistant"] {
    background: #cba6f7 !important;
    color: #1e1e2e !important;
    border-radius: 50% !important;
    width: 32px !important;
    height: 32px !important;
}

/* Input */
[data-testid="stBottom"] {
    background: #1e1e2e !important;
    border-top: 1px solid #313244 !important;
    padding: 1rem !important;
}

[data-testid="stChatInput"] {
    background: #313244 !important;
    border-radius: 14px !important;
    border: 1px solid #45475a !important;
}

[data-testid="stChatInput"] textarea {
    background: transparent !important;
    border: none !important;
    color: #cdd6f4 !important;
    font-family: 'Inter', sans-serif !important;
    font-size: 0.9rem !important;
    padding: 0.75rem 1rem !important;
}

[data-testid="stChatInput"] textarea::placeholder {
    color: #585b70 !important;
}

[data-testid="stChatInput"] textarea:focus {
    outline: none !important;
    box-shadow: none !important;
    border: none !important;
}

/* Divider */
hr { border-color: #313244 !important; margin: 0.5rem 0 1rem !important; }
</style>
""", unsafe_allow_html=True)


def start_messages():
    return [
        {"role": "assistant", "content": "Hello. I am MindEase, your mental health companion."},
        {"role": "assistant", "content": "This is a safe and confidential space. How are you feeling today?"},
    ]


st.markdown('<div class="chat-title">Mental Health Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="chat-sub">A private space to talk about how you feel</div>', unsafe_allow_html=True)
st.divider()

if "messages" not in st.session_state:
    st.session_state.messages = start_messages()

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)
    with st.chat_message("assistant"):
        with st.spinner(""):
            reply = get_response(user_input)
        st.markdown(reply)
    st.session_state.messages.append({"role": "assistant", "content": reply})