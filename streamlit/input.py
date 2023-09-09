import streamlit as st
from st_session import initialize_st
from model import filter_job
from function import input,select_class


    
initialize_st()
input()
st.write(st.session_state['input'])
#selectawards()
#st.write(st.session_state['current_award'])
st.dataframe(filter_job())

select_class()