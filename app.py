import streamlit as st
import google.generativeai as genai


st.title("welcome to my AI App")
genai.configure(api_key="AIzaSyBwfHm7EXjoY_hrZcIw1s2v67-sOKDN4hQ")
    
text = st.text_input("enter your question")

model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

if st.button("Click me"):
    response = chat.send_message(text)
    st.write(response.text)
    
