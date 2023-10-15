import streamlit as st
import datetime
import matplotlib.pyplot as plt
import plotly.express as px

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
    # number = st.number_input("input work hours", value=0)
    pt_worktime_Start = st.time_input('Start time', datetime.time(8, 00))
    pt_worktime_End = st.time_input('End time', datetime.time(17, 00))

    st.session_state['pt_worktime_Start'] = pt_worktime_Start
    st.session_state['pt_worktime_End'] = pt_worktime_End

    start_datetime = datetime.datetime(2000, 1, 1, pt_worktime_Start.hour, pt_worktime_Start.minute)
    end_datetime = datetime.datetime(2000, 1, 1, pt_worktime_End.hour, pt_worktime_End.minute)
    time_difference = end_datetime - start_datetime
    hours_difference = time_difference.total_seconds() / 3600

    # time_difference = datetime.combine(datetime.min, pt_worktime_End) - datetime.combine(datetime.min, pt_worktime_Start)
    st.write(f"You worked {hours_difference:.2f} hours on {d}.")


    if st.button("A new day"):
        st.session_state['part_time_list'].append(hours_difference)
        st.session_state['part_time_day'].append(d)
    for i in range(0,len(st.session_state['part_time_list'])):
        st.write('You worked', st.session_state['part_time_list'][i],'hours at',st.session_state['part_time_day'][i])

    # Calculate overtime hours based on a 38-hour workweek
    total_hours_week = sum(st.session_state.part_time_list)
    # overtime_hours = max(total_hours_week - 38, 0)

    if st.session_state.part_time_day:
        # for i in range(1,min(len(st.session_state.part_time_day), 8),  1):
        #     if abs((st.session_state.part_time_day[0] - st.session_state.part_time_day[-i])).days < 7:
        #         st.write(st.session_state.part_time_day[-i])
        #         st.write(st.session_state.part_time_day[0])
        #         st.write(abs((st.session_state.part_time_day[0] - st.session_state.part_time_day[-i]).days))
        #         overtime_hours = max(total_hours_week - 38, 0)
        #         st.session_state['overtime_hours'] = overtime_hours
        #     else:
        #         st.write("hi")
        #         overtime_hours = st.session_state['overtime_hours']
        #         st.write(st.session_state.part_time_day[-i])
        #         st.write(st.session_state.part_time_day[0])
        #         break

        if st.session_state.part_time_day:
            for i in range(1, min(len(st.session_state.part_time_day), 8), 1):
                if abs((st.session_state.part_time_day[-1] - st.session_state.part_time_day[-i])).days >= 7:
                    st.write("hi")
                    overtime_hours = st.session_state['overtime_hours']
                    st.write(st.session_state.part_time_day[-i])
                    st.write(st.session_state.part_time_day[-1])
                    break
                else:
                    st.write(st.session_state.part_time_day[-i])
                    st.write(st.session_state.part_time_day[-1])
                    st.write(abs((st.session_state.part_time_day[-1] - st.session_state.part_time_day[-i]).days))
                    overtime_hours = max(total_hours_week - 38, 0)
                    st.session_state['overtime_hours'] = overtime_hours


        # Calculate additional salary for overtime
    additional_salary = 0
    if st.session_state['overtime_hours'] > 0:
        if overtime_hours <= 2:
            additional_salary = overtime_hours * 1.5 * st.session_state.User_salary
        else:
            additional_salary = 2 * 1.5 * st.session_state.User_salary + (
                        overtime_hours - 2) * 2.0 * st.session_state.User_salary

    # Display overtime hours and additional salary
    st.write(f"Overtime hours: {st.session_state['overtime_hours']:.2f} hours.")
    st.write(f"Additional salary for overtime: ${additional_salary:.2f}")

    weekend_dates = []
    for index, date in enumerate(st.session_state['part_time_day']):
        if date.weekday() == 5 or date.weekday() == 6: 
            weekend_dates.append(index)
    #st.write(weekend_dates)
    sum_hours_holiday = 0
    if weekend_dates:
        for i in weekend_dates:
            if total_hours_week > 38:
                sum_hours_holiday += st.session_state['part_time_list'][i] * (
                            2 - st.session_state['penalty_rate'] / 100)
            else:
                sum_hours_holiday += st.session_state['part_time_list'][i]

    sum_hours = sum(st.session_state['part_time_list']) - sum_hours_holiday
    st.write('You worked total',sum_hours,'hours on weekday and ',sum_hours_holiday,'hours in holiday')

    # Calculate salary components
    sum_salary = round(st.session_state['User_salary'] * sum_hours)
    sum_holiday = round(st.session_state['User_salary'] * st.session_state['penalty_rate']/100 * sum_hours_holiday)
    #st.write(st.session_state['User_salary'],st.session_state['penalty_rate'])
    #st.write(sum_salary + sum_holiday)

    # Calculate total salary
    total_salary = st.session_state['User_salary'] * total_hours_week + additional_salary + sum_holiday
    st.write(f"Total salary: ${total_salary:.2f}")

    if sum_salary != 0 or sum_holiday != 0:
            sizes = [st.session_state['User_salary'] * total_hours_week, additional_salary, sum_holiday]
            labels = ['Basic Salery','Overtime Penalty', 'Holiday Penalty']
            fig, ax = plt.subplots(figsize=(6, 6))
            ax.pie(sizes, labels=labels,autopct='%1.1f%%', shadow=True, startangle=140)
            ax.axis('equal')
            legend_labels = [f'{label}: {size}' for label, size in zip(labels, sizes)]
            ax.legend(legend_labels, loc='upper right', bbox_to_anchor=(1.3, 1))

            ax.set_title('Combination of part-time salary')
            st.pyplot(fig)

def penalty_input():
    pass 

    st.write("What's your worktime:", worktime[0], "to", worktime[1])


def age():
    st.title("What's your age?")

    age = st.selectbox("", ("16 years of age and under", "17 years of age",
                                            "18 years of age", "19 years of age", "20 years of age and above"))
    st.session_state['age'] = age
    st.write("Your age:", age)
