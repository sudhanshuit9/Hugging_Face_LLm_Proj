import streamlit as st
import requests

st.title("Intelligent Chatbot")
user_input = st.text_input("You:")

if st.button("Send"):
    response = requests.post("http://localhost:8000/chat", json={"message": user_input}).json()
    st.text_area("Bot:", response["response"], height=200)
