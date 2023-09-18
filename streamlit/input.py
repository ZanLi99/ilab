import streamlit as st
from st_session import initialize_st
from model import filter_job
from function import input, select_class, select_rate_type, base_rate, calculate_penalty,overtime



    
initialize_st()
input()
#st.write(st.session_state['input'])
#selectawards()
#st.write(st.session_state['current_award'])
#st.dataframe(filter_job())

select_class()

calculate_penalty()
#st.dataframe(filter_job())

select_rate_type()

overtime()

# base_rate(st.session_state.get('user_salary', None), st.session_state.get('current_rate_type', None))

