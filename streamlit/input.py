import streamlit as st
from st_session import initialize_st

def input():
    st.title("input")
    user_input = st.text_input("your text", "default text")
    st.write("What's your input:", user_input)
    st.session_state['input'] = user_input
    
initialize_st()
input()

st.write(st.session_state['input'])