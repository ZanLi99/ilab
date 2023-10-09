import streamlit as st
from st_session import initialize_st
from model import filter_job
from function import select_class, select_rate_type, base_rate, calculate_penalty,overtime,get_holiday_df,chooseholiday,calculate_weekend,calculate_salary
from input import inputjob,worktime,work_type,work_time_everyday,salary,choosecountry
from PIL import Image
import random

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
calculate_penalty()
calculate_salary()

if 'number_list' not in st.session_state:
    st.session_state.number_list = []

number = st.number_input("input work hours", value=0)
if st.button("add"):
    st.session_state.number_list.append(number)

# 显示数字列表
st.write("list:", st.session_state.number_list)


       
select_class()


#calculate_penalty()


#select_rate_type()

#overtime()