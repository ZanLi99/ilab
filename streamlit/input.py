import streamlit as st
import datetime



def inputjob():
    st.title("What's your job?")
    user_input = st.text_input("your job", "")
    st.write("What's your role:", user_input)
    st.session_state['user_input'] = user_input

def work_type():
    st.title("What type of your job?")
    type = st.selectbox("", ("Full Time","Part Time","Casual"))
    st.session_state['work_type'] = type
    st.write("Your type of work:", type)

def work_time_everyday():
    st.title("What's your worktime of everyday?")
    worktime_Start = st.time_input('Start time', datetime.time(8, 00))
    worktime_End = st.time_input('End time', datetime.time(17, 00))
    Lunch_breack = st.number_input('Lunch break (minutes):',0)

    st.session_state['worktime_Start'] = worktime_Start
    st.session_state['worktime_End'] = worktime_End
    st.session_state['Lunch_breack'] = Lunch_breack

    st.write('Your worktime:', worktime_Start, "to", worktime_End,
             ", and you have", Lunch_breack, "minutes for lunch break.")

def salary():
    st.title( "What's your salary?")
    salary_type = st.radio(
       "",
        key="visibility",
        options=["Anuual", "Daily", "Hourly","Weekly"],
    )
    st.session_state['salary_type'] = salary_type

    User_salary = st.number_input("Your salary:",0)
    st.session_state['User_salary'] = User_salary

def worktime():
    st.title("What's your worktime?")

    today = datetime.datetime.now()

    jan_1 = datetime.date(today.year-3, 1, 1)
    dec_31 = datetime.date(today.year+1, 12, 31)

    worktime = st.date_input(
        "Select your vacation for next year",
        (today,today + datetime.timedelta(days=1)),
        jan_1,
        dec_31,
        format="MM.DD.YYYY",
    )
    st.session_state['worktime'] = worktime
    st.write("What's your worktime:", worktime[0], "to", worktime[1])


