import streamlit as st
import pandas as pd

def input():
    st.title("input")
    user_input = st.text_input("your text", "")
    st.write("What's your input:", user_input)
    st.session_state['input'] = user_input

def selectawards():
    contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'], case=False, na='ignore')
    temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()
    with st.form('class'):
        current_award = st.selectbox('what award do you fall under',
                            options=sorted(temp), key='option_award')
        submitted = st.form_submit_button(label='submit_class')
        if submitted:
            st.write('you have submitted ', current_award)