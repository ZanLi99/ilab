import streamlit as st
from st_session import initialize_st
from model import filter_job
from function import select_class, select_rate_type, base_rate, calculate_penalty,overtime,get_holiday_df,chooseholiday,calculate_weekend
from input import inputjob,worktime,work_type,work_time_everyday,salary,choosecountry

from streamlit_chat import message

initialize_st()
#st.write(st.session_state['classification'])
choosecountry()

inputjob()
work_type()
salary()
work_time_everyday()
worktime()

get_holiday_df()
chooseholiday()
calculate_weekend()
select_class()


#calculate_penalty()


#select_rate_type()

#overtime()