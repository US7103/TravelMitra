import streamlit as st
import requests

# ---- CONFIGURATION ----
MODEL = "TravelMitra"
OLLAMA_URL = "http://localhost:11434/api/chat"

st.set_page_config(page_title="Travel Mitra", page_icon="🧳", layout="wide")

# ---- STYLING ----
st.markdown("""
<style>
html, body, [class*="css"] {
    font-family: 'Segoe UI', sans-serif;
    margin: 0;
    padding: 0;
    background: linear-gradient(135deg, #FFDEE9, #B5FFFC);
    height: 100%;
    width: 100%;
    overflow-x: hidden;
}

.header {
    background: linear-gradient(to right, #4facfe, #00f2fe);
    padding: 3rem 2rem;
    border-radius: 20px;
    text-align: center;
    color: white;
    margin-bottom: 2rem;
    box-shadow: 0 6px 30px rgba(0,0,0,0.2);
}
.header h1 {
    font-size: 3rem;
    margin-bottom: 0.5rem;
}
.header p {
    font-size: 1.25rem;
    opacity: 0.95;
}

.chat-container {
    background: rgba(255,255,255,0.9);
    border-radius: 25px;
    padding: 2rem;
    max-height: 70vh;
    overflow-y: auto;
    box-shadow: 0 10px 25px rgba(0,0,0,0.1);
    margin-bottom: 2rem;
}

.chat-bubble-user, .chat-bubble-bot {
    padding: 1rem 1.5rem;
    margin: 1rem 0;
    border-radius: 20px;
    max-width: 80%;
    font-size: 1.1rem;
    box-shadow: 0 4px 12px rgba(0,0,0,0.05);
}
.chat-bubble-user {
    background: #ffecd2;
    align-self: flex-end;
    color: #333;
    text-align: right;
}
.chat-bubble-bot {
    background: #e0f7fa;
    color: #222;
    text-align: left;
    align-self: flex-start;
}

.input-row {
    display: flex;
    gap: 1rem;
    justify-content: center;
    align-items: center;
    margin-top: 2rem;
}
input[type="text"] {
    width: 100%;
    padding: 1rem;
    font-size: 1.1rem;
    border: 2px solid #ddd;
    border-radius: 15px;
}

.stButton > button {
    background-color: #4facfe;
    color: white;
    padding: 0.75rem 2rem;
    font-size: 1rem;
    border-radius: 12px;
    border: none;
    box-shadow: 0 4px 10px rgba(0,0,0,0.1);
    transition: 0.3s ease;
}
.stButton > button:hover {
    background-color: #00c6ff;
}

::-webkit-scrollbar {
    width: 8px;
}
::-webkit-scrollbar-thumb {
    background-color: #bbb;
    border-radius: 20px;
}

.footer {
    text-align: center;
    margin-top: 3rem;
    font-size: 0.9rem;
    color: #666;
}
</style>
""", unsafe_allow_html=True)

# ---- HEADER ----
st.markdown("""
<div class='header'>
    <h1>🧳 Travel Mitra</h1>
    <p>Your AI travel planner for unforgettable budget trips across India 🇮🇳</p>
</div>
""", unsafe_allow_html=True)

# ---- SESSION STATE ----
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! 👋 I’m **Travel Mitra** — your guide for amazing budget trips in India. Where do you want to go today?"}
    ]

# ---- INPUT FORM ----
st.markdown("<div class='input-row'>", unsafe_allow_html=True)
with st.form("chat_form", clear_on_submit=True):
    user_input = st.text_input("", placeholder="e.g., Plan a 3-day trip from Jaipur to Mumbai")
    submitted = st.form_submit_button("Send")
st.markdown("</div>", unsafe_allow_html=True)

if submitted and user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    payload = {
        "model": MODEL,
        "messages": st.session_state.messages,
        "stream": False
    }
    try:
        response = requests.post(OLLAMA_URL, json=payload)
        reply = response.json()["message"]["content"]
    except Exception as e:
        reply = f"⚠️ Error from Ollama: {e}"

    st.session_state.messages.append({"role": "assistant", "content": reply})

# ---- CHAT WINDOW ----
st.markdown("<div class='chat-container'>", unsafe_allow_html=True)

for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='chat-bubble-user'>🧑 You: {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='chat-bubble-bot'>🤖 Mitra: {msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)

# ---- FOOTER ----
st.markdown("<div class='footer'>✨ Built with ❤️ by Travel Mitra · Explore India your way 🌏</div>", unsafe_allow_html=True)

# ---- AUTO SCROLL ----
st.markdown("""
<script>
window.scrollTo(0, document.body.scrollHeight);
</script>
""", unsafe_allow_html=True)

