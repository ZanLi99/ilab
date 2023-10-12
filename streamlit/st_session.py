import streamlit as st
import pandas as pd


def initialize_st():
    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = []
    if 'current_class' not in st.session_state:
        st.session_state['current_class'] = []
    if 'penalty_rate' not in st.session_state:
        st.session_state['penalty_rate'] = 150
    if 'current_rate_type' not in st.session_state:
        st.session_state['current_rate_type'] = []
    if 'age' not in st.session_state:
        st.session_state['age'] = []
    if 'working_hour_weekday' not in st.session_state:
        st.session_state['working_hour_weekday'] = []
    if 'working_hour_weekend' not in st.session_state:
        st.session_state['working_hour_weekend'] = []
    if 'working_hour_holiday' not in st.session_state:
        st.session_state['working_hour_holiday'] = []
    if 'over_time_weekday_1' not in st.session_state:
        st.session_state['over_time_weekday_1'] = []
    if 'over_time_weekday_2' not in st.session_state:
        st.session_state['over_time_weekday_2'] = []
    if 'over_time_holiday_1' not in st.session_state:
        st.session_state['over_time_holiday_1'] = []
    if 'over_time_holiday_2' not in st.session_state:
        st.session_state['over_time_holiday_2'] = []
    if 'over_time_weekend_1' not in st.session_state:
        st.session_state['over_time_weekend_1'] = []
    if 'over_time_weekend_2' not in st.session_state:
        st.session_state['over_time_weekend_2'] = []
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
        st.session_state['User_salary'] = 0
    if 'salary_type' not in st.session_state:
        st.session_state['salary_type'] = []
    if 'user_country' not in st.session_state:
        st.session_state['user_country'] = []
    if 'holiday' not in st.session_state:
        st.session_state['holiday'] = []
    if 'select_weekend' not in st.session_state:
        st.session_state['select_weekend'] = 0
    if 'part_time_list' not in st.session_state:
        st.session_state['part_time_list'] = []
    if 'part_time_day' not in st.session_state:
        st.session_state['part_time_day'] = []
    if 'classification_annual_rate' not in st.session_state:
        st.session_state['classification_annual_rate'] = []
    if 'base_rate_type' not in st.session_state:
        st.session_state['base_rate_type'] = []
    if 'user_salary' not in st.session_state:
        st.session_state['user_salary'] = []

# def classification_clean():
#     classification = pd.read_csv('classification.csv')
#     classification['classification'] = classification['classification'].astype(str)
#     classification['classification'] = classification['classification'].str.lower()
#     classification.dropna(subset=['base_rate','base_pay_rate_id','base_rate_type'], axis=0, inplace=True)

#     max_versions = classification.groupby(['classification','employee_rate_type_code'])['version_number'].max().reset_index()
#     result = classification.merge(max_versions, on=['classification', 'version_number'])

#     return result