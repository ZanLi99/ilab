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


st.title("多日期选择示例")
st.write("选择日期范围:")

# 显示Dash应用程序的URL
dash_app_url = "http://localhost:8050"  # 替换为您的Dash应用程序的URL
st.markdown(f"您可以 [点击此处]({dash_app_url}) 访问Dash应用程序。")
st.write(f'<iframe src="{dash_app_url}" width="800" height="600"></iframe>', unsafe_allow_html=True)

