import streamlit as st
import openai
import os

openai.api_key = os.environ["OPENAI_KEY"]


def initialize_streamlit():
    st.set_page_config(initial_sidebar_state="collapsed")
    st.title("Orthodox assistant")
    st.markdown(
        """
        I am a AI assistant with lots of knowledge about the Orthodox Church.
        """
    )

    if 'conversation' not in st.session_state:
        st.session_state.conversation = [{
            "role": "system", "content": """
                You are a helpful assistant with deep knowledge about the Eastern Orthodox Church. 
                Provide as thoughtful and detailed as answers as possible.
                You are to restrict yourself to ONLY content about the religious and spiritual domain, especially orthodox.
                If the user asks for other subjects of discussion politely apologize saying this is not your domain of expertise. 
                """
        }]


def main():
    initialize_streamlit()
    question = st.text_input("What do you want to talk about?")
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
