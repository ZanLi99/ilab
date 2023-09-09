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
