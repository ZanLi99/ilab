import streamlit as st
import pandas as pd
import numpy as np
## loads in the data
awards = pd.read_csv('./streamlit/awards.csv')
classification = pd.read_csv('./streamlit/classification.csv')


def replace_null_others(dataframe, column, text):
    dataframe[f'{column}'] = dataframe[f'{column}'].fillna(f'{text}')


# find potential awards
replace_null_others(classification, 'calculated_rate', 'Unavailable_data')
replace_null_others(classification, 'base_rate', 'Unavailable_data')

classification = classification.loc[(
    classification['calculated_rate'] != 'Unavailable_data') & (classification['base_rate'] != 'Unavailable_data')]

award_list = awards['name']
with st.form('award_form'):
    current_award = st.selectbox('what award do you fall under',
                          options=award_list, key='option_award')
    submitted = st.form_submit_button(label='submit')
    if submitted:
        st.write('you have submitted ', current_award)

#filter data based on input
current_award = awards.loc[awards["name"] == current_award]

classification_award = classification.loc[classification['awards'].isin(current_award['award_fixed_id'])]

replace_null_others(classification_award, 'employee_rate_type_code', 'Other')

#get employee type to filter data with


with st.form('employee_type'):
    employee_type = st.selectbox(
        'employee_type', options=classification_award['employee_rate_type_code'].unique(), key='employee_type_form')
    submit_1 = st.form_submit_button(label='submit')
    if submit_1:
        st.write('you have submitted ', employee_type)

classification_award = classification_award.loc[
    classification_award["employee_rate_type_code"] == employee_type]

st.write(classification_award)

# get parent_classification_name  to filter data with
replace_null_others(classification_award, 'parent_classification_name', 'Other')

with st.form('parent_form'):
    parent_form = st.selectbox(
        'parent_award_form', options=classification_award['parent_classification_name'].unique(), key='parent_form')
    submit_2 = st.form_submit_button(label='submit')
    if submit_2:
        st.write('you have submitted ', parent_form)

classification_award = classification_award.loc[
    classification_award["parent_classification_name"] == parent_form]
replace_null_others(classification_award, 'classification', 'other')

# get classification_child_form  to filter data with
with st.form('classification_child_form'):
    classification_child_form = st.selectbox(
        'child_form', options=classification_award['classification'].unique(), key='child_form')
    submit_3 = st.form_submit_button(label='submit')
    if submit_3:
        st.write('you have submitted ', classification_child_form)
classification_award = classification_award.loc[
    classification_award["classification"] == classification_child_form]

# final results of filtered data


st.write(classification_award['base_rate'],
         classification_award['base_rate_type'], classification_award['calculated_rate'], classification_award['calculated_rate_type'])

st.write(classification_award)

table_df = classification_award[[
    'base_rate', 'base_rate_type', 'calculated_rate', 'calculated_rate_type']]

st.write(table_df)

#### BUGS TO FIX
#### REMOVE NA VALUES 
#### if classification parent has only NA values should be skipped
