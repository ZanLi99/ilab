import streamlit as st
import pandas as pd

def input():
    st.title("input")
    user_input = st.text_input("your text", "")
    st.write("What's your input:", user_input)
    st.session_state['input'] = user_input

def select_class():
    contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'], case=False, na='ignore')
    temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()
    with st.form('sub_class'):
        selected_values = st.multiselect("what classification do you fall under", temp)
        submit = st.form_submit_button(label='class_submit')
        if submit:
            st.session_state['current_class'] = []
            st.session_state['current_class'].extend(selected_values)
            st.write('you have submitted ', st.session_state['current_class'])




def select_rate_type():
    classification = st.session_state['classification']
    classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
    classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
    classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')

    base_rate_type = classification['base_rate_type'].drop_duplicates()

    classification['base_rate_annual'] = classification.apply(
        lambda row: row['base_rate'] * 40 * 52 if row['base_rate_type'] == 'hourly' else
        row['base_rate'] * 12 if row['base_rate_type'] == 'monthly' else
        row['base_rate'] * 5 * 52 if row['base_rate_type'] == 'daily' else
        row['base_rate'] * 52 if row['base_rate_type'] == 'weekly' else
        row['base_rate'], axis=1)

    st.session_state['classification_annual_rate'] = classification

    with st.form('base_rate_type'):
        current_rate_type = st.selectbox('what type of base rate',
                            options=sorted(base_rate_type), key='base_rate_type')
        submitted = st.form_submit_button(label='submit')
        if submitted:
            st.write('you have submitted ', current_rate_type)

    st.dataframe(st.session_state['classification_annual_rate'])