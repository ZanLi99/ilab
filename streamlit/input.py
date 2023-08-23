import streamlit as st

def input():
    st.title("input")
    user_input = st.text_input("your text", "default text")
    st.write("What's your input:", user_input)
input()