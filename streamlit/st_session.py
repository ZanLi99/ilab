import streamlit as st
import pandas as pd


def initialize_st():
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = []
    if 'current_class' not in st.session_state:
        st.session_state['current_class'] = []
    if 'penalty_rate' not in st.session_state:
        st.session_state['penalty_rate'] = []
    if 'current_rate_type' not in st.session_state:
        st.session_state['current_rate_type'] = []
    # ---------
    if 'user_salary' not in st.session_state:
        st.session_state['user_salary'] = 0
    # ---------
    if 'worktime' not in st.session_state:
        st.session_state['worktime'] = []
    if 'work_type' not in st.session_state:
        st.session_state['work_type'] = []
    if 'worktime_Start' not in st.session_state:
        st.session_state['worktime_Start'] = []
    if 'worktime_End' not in st.session_state:
        st.session_state['worktime_End']= []
    if 'Lunch_breack' not in st.session_state:
        st.session_state['Lunch_breack']= []
    if 'User_salary' not in st.session_state:
        st.session_state['User_salary'] = []
    if 'salary_type' not in st.session_state:
        st.session_state['salary_type'] = []
    if 'user_country' not in st.session_state:
        st.session_state['user_country'] = []
    if 'holiday' not in st.session_state:
        st.session_state['holiday'] = []
    if 'select_weekend' not in st.session_state:
        st.session_state['select_weekend'] = 0

    st.session_state['country'] = pd.read_csv('country.csv')
    st.session_state['awards'] = pd.read_csv('awards.csv')
    st.session_state['classification'] = classification_clean()
    st.session_state['classification'] = st.session_state['classification'].apply(lambda x: x.astype(str).str.lower() if x.dtype == "object" else x)
    st.session_state['selection_class'] = st.session_state['classification']['classification'].drop_duplicates()
    st.session_state['merged'] = pd.read_csv('merge_classification_penalty.csv')

    if 'classification_annual_rate' not in st.session_state:
        st.session_state['classification_annual_rate'] = []
    if 'base_rate_type' not in st.session_state:
        st.session_state['base_rate_type'] = []
    if 'user_salary' not in st.session_state:
        st.session_state['user_salary'] = []

def classification_clean():
    classification = pd.read_csv('classification.csv')
    classification['classification'] = classification['classification'].astype(str)
    classification['classification'] = classification['classification'].str.lower()
    classification.dropna(subset=['base_rate','base_pay_rate_id','base_rate_type'], axis=0, inplace=True)

    max_versions = classification.groupby(['classification','employee_rate_type_code'])['version_number'].max().reset_index()
    result = classification.merge(max_versions, on=['classification', 'version_number'])

    return result