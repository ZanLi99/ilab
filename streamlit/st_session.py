import streamlit as st
import pandas as pd


def initialize_st():
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = []
    if 'current_class' not in st.session_state:
        st.session_state['current_class'] = []
    st.session_state['awards'] = pd.read_csv('./streamlit/awards.csv')
    st.session_state['classification'] = pd.read_csv('./streamlit/classification.csv')
    st.session_state['classification'] = st.session_state['classification'].apply(lambda x: x.astype(str).str.lower() if x.dtype == "object" else x)
    st.session_state['selection_class'] = st.session_state['classification']['classification'].drop_duplicates()

    if 'classification_annual_rate' not in st.session_state:
        st.session_state['classification_annual_rate'] = []
    if 'base_rate_type' not in st.session_state:
        st.session_state['base_rate_type'] = []
    if 'user_salary' not in st.session_state:
        st.session_state['user_salary'] = []