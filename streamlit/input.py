import streamlit as st
import datetime


def inputjob():
    # The interface of input user's job
    # st.session_state['user_input'] -> Save the job of inputting

    st.title("What's your job?")
    user_input = st.text_input("your job", "")
    st.write("What's your role:", user_input)
    st.session_state['user_input'] = user_input

def work_type():
    # The interface of input job's type
    # st.session_state['work_type'] -> save the type of work

    st.title("What type of your job?")
    type = st.selectbox("", ("Full Time","Part Time","Casual"))
    st.session_state['work_type'] = type
    st.write("Your type of work:", type)

def work_time_everyday():
    # The interface of input user's worktime of everyday
    # st.session_state['worktime_Start'] is the start time 
    # st.session_state['worktime_End'] -> The end time
    # st.session_state['Lunch_breack'] -> The break time / lunch time

    st.title("What's your worktime of everyday?")
    worktime_Start = st.time_input('Start time', datetime.time(8, 00))
    worktime_End = st.time_input('End time', datetime.time(17, 00))
    Lunch_breack = st.number_input('Lunch break (minutes):',0)

    st.session_state['worktime_Start'] = worktime_Start
    st.session_state['worktime_End'] = worktime_End
    st.session_state['Lunch_breack'] = Lunch_breack

    st.write('Your worktime:', worktime_Start, "to", worktime_End,
             ", and you have", Lunch_breack, "minutes for lunch break.")

def work_time_weekday():
    # The interface of input user's worktime of weekday

    st.title("What's your working hours on weekday?")
    working_hour = st.number_input('Total working hours', 0)
    over_time_1 = st.number_input('Working over time (First 2 hours) (minutes):',0)
    over_time_2 = st.number_input('Working over time (After 2 hours) (minutes):', 0)

    working_hour_holiday = st.number_input('Total working hours', 0)
    over_time__holiday_1 = st.number_input('Working over time (First 2 hours) (minutes):', 0)
    over_time__holiday_2 = st.number_input('Working over time (After 2 hours) (minutes):', 0)

    st.session_state['working_hour_weekday'] = working_hour
    st.session_state['over_time_weekday_1'] = over_time_1
    st.session_state['over_time_weekday_2'] = over_time_2

    st.session_state['working_hour_holiday'] = working_hour_holiday
    st.session_state['over_time_holiday_1'] = over_time__holiday_1
    st.session_state['over_time_holiday_2'] = over_time__holiday_2

    st.write('Your working hours on weekday:', working_hour,
             ", and you have work over time", over_time_1, " minutes on first 2 hours and ", over_time_2,
             " after 2 hours")
    st.write('Your working hours on holiday:', working_hour_holiday,
             ", and you have work over time ", over_time__holiday_1, " minutes on first 2 hours and ", over_time__holiday_2,
             " hours after 2 hours")

def work_time_weekend():
    # The interface of input user's worktime of weekend

    st.title("What's your working hours on weekend?")
    working_hour = st.number_input('Total working hours', 0)
    over_time_1 = st.number_input('Working over time (First 2 hours) (minutes):',0)
    over_time_2 = st.number_input('Working over time (After 2 hours) (minutes):', 0)

    st.session_state['working_hour_weekend'] = working_hour
    st.session_state['over_time_weekend_1'] = over_time_1
    st.session_state['over_time_weekend_2'] = over_time_2

    st.write('Your working hours on weekend:', working_hour,
             ", and you have work over time", over_time_1, "minutes on first 2 hours and ", over_time_2,
             "after 2 hours")


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


def age():
    st.title("What's your age?")

    age = st.selectbox("", ("16 years of age and under", "17 years of age",
                                            "18 years of age", "19 years of age", "20 years of age and above"))
    st.session_state['age'] = age
    st.write("Your age:", age)
