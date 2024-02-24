import os
import streamlit as st
from langchain_helper_functions import query_assistant


if 'chat_history' not in st.session_state:
    st.session_state['chat_history'] = []

def send_message(user_input, container):
    if user_input:
        st.session_state['chat_history'].append(f"**You:** {user_input}")
        response = query_assistant(user_input)
        st.session_state['chat_history'].append(f"**Chef:** {response}")
        for message in st.session_state['chat_history']:
            container.markdown(message)

def main():
    st.title("Recipe Assistant")
    chat_container = st.container()
    with st.form("message_form"):
        user_input = st.text_input("Ask for recipes or mention ingredients and get recipes based on them...", "")
        send = st.form_submit_button("Send")

    if send:
        send_message(user_input, chat_container)

if __name__ == "__main__":
    main()
