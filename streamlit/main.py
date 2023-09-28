import streamlit as st
from st_session import initialize_st
from model import filter_job
from function import select_class, select_rate_type, base_rate, calculate_penalty,overtime
from input import inputjob,worktime,work_type,work_time_everyday,salary

from streamlit_chat import message

initialize_st()
#st.write(st.session_state['classification'])

inputjob()
work_type()
salary()
work_time_everyday()
worktime()


select_class()

#calculate_penalty()


#select_rate_type()

#overtime()