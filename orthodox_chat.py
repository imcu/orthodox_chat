import streamlit as st
import openai
import os

openai.api_key = os.environ["OPENAI_KEY"]


def initialize_streamlit():
    st.set_page_config(initial_sidebar_state="collapsed")
    st.title("Eastern Orthodox Assistant")
    st.markdown("You are a helpful assistant with deep knowledge about the Eastern Orthodox Church. Provide as thoughtful and detailed as answers as possible.")

    if 'conversation' not in st.session_state:
        st.session_state.conversation = [{
            "role": "system", "content": """
                I am are a helpful assistant with deep knowledge about the Eastern Orthodox Church. 
                You can ask me anything and I will provide as thoughtful and detailed as answers as possible.
                """
        }]


def main():
    initialize_streamlit()
    question = st.text_input("question")
    if question == "": return
    st.session_state.conversation.append({"role": "user", "content": question})
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=st.session_state.conversation
    )
    answer = response['choices'][0]['message']['content']
    st.session_state.conversation.append({"role": "assistant", "content": answer}, )
    st.write(answer)


main()
