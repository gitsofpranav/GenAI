import streamlit as st
from dotenv import load_dotenv

load_dotenv()

from langchain_mistralai import ChatMistralAI
from langchain.messages import SystemMessage, HumanMessage, AIMessage

st.title("Poetry Expert Chatbot")

mode = st.sidebar.selectbox(
    "AI Mode",
    ["Friendly", "Funny", "Sad", "Angry","Teacher"]
)

mode_prompts = {
    "Friendly": "You are a poetry expert. Respond in a warm, friendly tone.",
    "Funny": "You are a poetry expert. Respond in a funny, humorous tone.",
    "Sad": "You are a poetry expert. Respond in a sad, melancholic tone.",
    "Angry": "You are a poetry expert. Respond in an angry, irritated tone.",
    "Teacher": "you are a teacher who teaches DSA and give good respone of the question asked about DSA",
}

model = ChatMistralAI(
    model="mistral-small-2506",
    temperature=0,
    max_tokens=500
)

if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(mode_prompts[mode]),
    ]
    st.session_state.mode = mode

# Update system prompt if mode changes
if st.session_state.mode != mode:
    st.session_state.messages[0] = SystemMessage(mode_prompts[mode])
    st.session_state.mode = mode

# Display chat history (skip the SystemMessage)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.write(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.write(msg.content)

prompt = st.chat_input("You :")

if prompt:
    st.session_state.messages.append(HumanMessage(prompt))
    with st.chat_message("user"):
        st.write(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(response.content))
    with st.chat_message("assistant"):
        st.write(response.content)