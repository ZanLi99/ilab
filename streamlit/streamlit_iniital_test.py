import streamlit as st
import pandas as pd
## loads in the data
awards = pd.read_csv('./streamlit/awards.csv')
classification = pd.read_csv('./streamlit/classification.csv')
## find potential awards
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

with st.form('parent_form'):
    parent_form = st.selectbox(
        'parent_award_form', options=classification_award['parent_classification_name'].unique(), key='parent_form')
    submit_2 = st.form_submit_button(label='submit')
    if submit_2:
        st.write('you have submitted ', parent_form)

classification_award = classification_award.loc[
    classification_award["parent_classification_name"] == parent_form]

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
#### BUGS TO FIX
#### REMOVE NA VALUES 
#### if classification parent has only NA values should be skipped
#### there can be duplicate values due to different version numbers of the same award