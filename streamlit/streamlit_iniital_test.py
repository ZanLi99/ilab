import streamlit as st
import pandas as pd

awards = pd.read_csv('./streamlit/awards.csv')

classification = pd.read_csv('./streamlit/classification.csv')

award_list = awards['name']
with st.form('award_form'):
    current_award = st.selectbox('what award do you fall under',
                          options=award_list, key='option_award')
    submitted = st.form_submit_button(label='submit')
    if submitted:
        st.write('you have submitted ', current_award)

current_award = awards.loc[awards["name"] == current_award]

classification_award = classification.loc[classification['awardID'].isin(current_award['award_id'])]

with st.form('employee_type'):
    employee_type = st.selectbox(
        'employee_type', options=classification_award['employeeRateTypeCode'].unique(), key='employee_type_form')
    submit_1 = st.form_submit_button(label='submit')
    if submit_1:
        st.write('you have submitted ', employee_type)

classification_award = classification_award.loc[
    classification_award["employeeRateTypeCode"] == employee_type]


with st.form('parent_form'):
    parent_form = st.selectbox(
        'parent_award_form', options=classification_award['parentClassificationName'].unique(), key='parent_form')
    submit_2 = st.form_submit_button(label='submit')
    if submit_2:
        st.write('you have submitted ', parent_form)

classification_award = classification_award.loc[
    classification_award["parentClassificationName"] == parent_form]


with st.form('classification_child_form'):
    classification_child_form = st.selectbox(
        'child_form', options=classification_award['classification'].unique(), key='child_form')
    submit_3 = st.form_submit_button(label='submit')
    if submit_3:
        st.write('you have submitted ', classification_child_form)
classification_award = classification_award.loc[
    classification_award["classification"] == classification_child_form]


st.write(classification_award['baseRate'],
         classification_award['baseRateType'], classification_award['calculatedRate'], classification_award['calculatedRateType'])



#### BUGS TO FIX
#### REMOVE NA VALUES 
#### if classification parent has only NA values should be skipped
####