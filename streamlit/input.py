import streamlit as st
from st_session import initialize_st
from model import filter_job
from function import selectawards, input


    
initialize_st()
input()

st.write(st.session_state['input'])

selectawards()


st.dataframe(filter_job())