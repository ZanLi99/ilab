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



def select_rate_type():
    classification = st.session_state['classification']
    classification.dropna(subset=["base_rate_type"], inplace=True)
    classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
    classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')
    base_rate_type = classification['base_rate_type'].drop_duplicates()

    with st.form('base_rate_type'):
        current_rate_type = st.selectbox('what type of base rate',
                            options=sorted(base_rate_type), key='base_rate_type')
        submitted = st.form_submit_button(label='submit')
        if submitted:
            st.write('you have submitted ', current_rate_type)