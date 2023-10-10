import streamlit as st
import datetime
import matplotlib.pyplot as plt


def choosecountry():
    # select country
    st.title("Where are you from?")
    user_country = st.selectbox("", st.session_state['country']['name'],index=4)
    st.session_state['user_country'] = st.session_state['country'][st.session_state['country']['name'] == user_country]['countryCode']
    #st.write(st.session_state['user_country'].values)

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

    st.title("What's your job type?")
    type = st.selectbox("", ("Full Time","Part Time","Casual"))
    st.session_state['work_type'] = type
    st.write("Your type of work:", type)
    if type == 'Full Time':
        st.image("./Pictures/Full.png", use_column_width=True)
    if type == 'Part Time':
        st.image("./Pictures/Part.jpg", use_column_width=True)
    if type == 'Casual':
        st.image("./Pictures/Casual.jpg", use_column_width=True)
    return type
    

def work_time_everyday():
    # The interface of input user's worktime of everyday
    # st.session_state['worktime_Start'] is the start time 
    # st.session_state['worktime_End'] -> The end time
    # st.session_state['Lunch_breack'] -> The break time / lunch time

    st.title("Please enter your daily working Start time and End time")
    worktime_Start = st.time_input('Start time', datetime.time(8, 00))
    worktime_End = st.time_input('End time', datetime.time(17, 00))
    Lunch_breack = st.number_input('Lunch break (minutes):',0)

    st.session_state['worktime_Start'] = worktime_Start
    st.session_state['worktime_End'] = worktime_End
    st.session_state['Lunch_breack'] = Lunch_breack

    st.write('Your worktime:', worktime_Start, "to", worktime_End,
             ", and you have", Lunch_breack, "minutes for lunch break.")

def salary_type():
    st.title( "Select the payment frequency you want to calculate?")
    salary_type = st.radio(
       "",
        key="visibility",
        options=["Anuual", "Daily", "Hourly","Weekly"],
    )
    st.session_state['salary_type'] = salary_type

def salary():
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
    if len(worktime) >= 2 and worktime[0] and worktime[1]:
        st.write("What's your worktime:", worktime[0], "to", worktime[1])


def part_time_input():
    d = st.date_input("When did you work?", datetime.date.today())
    number = st.number_input("input work hours", value=0)
    if st.button("A new day"):
        st.session_state['part_time_list'].append(number)
        st.session_state['part_time_day'].append(d)
    for i in range(0,len(st.session_state['part_time_list'])):
        st.write('You worked', st.session_state['part_time_list'][i],'hours at',st.session_state['part_time_day'][i])
    
    weekend_dates = []
    for index, date in enumerate(st.session_state['part_time_day']):
        if date.weekday() == 5 or date.weekday() == 6: 
            weekend_dates.append(index)
    #st.write(weekend_dates)
    sum_hours_holiday = 0
    if weekend_dates:
        for i in weekend_dates:
            sum_hours_holiday += st.session_state['part_time_list'][i]
    sum_hours = sum(st.session_state['part_time_list']) - sum_hours_holiday
    st.write('You worked total',sum_hours,'hours and there are',sum_hours_holiday,'hours in holiday')
    sum_salary = round(st.session_state['User_salary'] * sum_hours)
    sum_holiday = round(st.session_state['User_salary'] * st.session_state['penalty_rate']/100 * sum_hours_holiday)
    #st.write(st.session_state['User_salary'],st.session_state['penalty_rate'])
    #st.write(sum_salary + sum_holiday)
    if sum_salary != 0 or sum_holiday != 0:
            sizes = [sum_salary,sum_holiday]
            labels = ['Basic salery','penalty']
            fig, ax = plt.subplots(figsize=(6, 6)) 
            ax.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
            ax.axis('equal')  
            legend_labels = [f'{label}: {size}' for label, size in zip(labels, sizes)]
            ax.legend(legend_labels, loc='upper right', bbox_to_anchor=(1.3, 1))

            ax.set_title('Combination of part-time salary') 
            st.pyplot(fig)

def penalty_input():
    pass 
