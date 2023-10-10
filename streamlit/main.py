import streamlit as st
import datetime
import matplotlib.pyplot as plt

import pandas as pd
from st_session import initialize_st
from function import select_class, select_rate_type, base_rate, calculate_penalty,overtime,get_holiday_df,chooseholiday,calculate_weekend,calculate_salary
from input import inputjob,worktime,work_type,work_time_everyday,salary,choosecountry,part_time_input,salary_type
import random


from streamlit_chat import message

initialize_st()
#st.write(st.session_state['classification'])

#tab1, tab2 = st.tabs(["penalty", "WageCraft Hospitality Award"])

#with tab1:
    #st.header("penalty")
page = st.sidebar.selectbox("Select Page", ["Page 1", "Page 2"])

if page == "Page 1":
    st.header("Page 1")
    choosecountry()
    inputjob()
    type = work_type()
    if type == 'Full Time':
        salary_type()
        salary()
        work_time_everyday()
        worktime()
        get_holiday_df()
        chooseholiday() 
        calculate_weekend()
        calculate_penalty()
        calculate_salary()
    if type == 'Part Time':
        salary()
        part_time_input()

elif page == "Page 2":
    st.header("Page 2")
    #st.header("WageCraft Hospitality Award")
    #st.set_page_config(page_title='WageCraft Hospitality Award')


    st.header('WageCraft Hospitality Wage Calculator', divider='gray')
    st.subheader('Input Job information')

    st.subheader('These are some examples of jobs that are covered under this award')
    st.write('- waiters and waitresses')
    st.write('- kitchen hands')

    Adult_minimum_rate_weekly = {
        'Introductory': 859.30,
        'level_1': 882.80,
        'level_2': 913.90,
        'level_3': 945.00,
        'level_4': 995.00,
        'level_5': 1057.40,
        'level_6': 1085.60
    }


    job_level_info = {
        'Introductory': 'Introductory level is for an employee who enters the hospitality industry and does not demonstrate the competency requirements of level 1. The employee remains at Introductory level for up to 3 months while undertaking appropriate training and being assessed for competency to move to level 1. At the end of that period, the employee moves to level 1 unless the employee and the employer mutually agree that further training of up to 3 months is required for the employee to achieve the necessary competency.',
        'level_1': 'Level 1 involves employees in any of the following activities: picking up glasses - emptying ashtrays - removing food plates -setting and wiping down tablescleaning - tidying associated areas',
        'level_2': 'Level 2 involves someone who is engaged in any of the following: handling liqueor, recieving money, attending a snack bar, delivery duties, taking reservations, greeting and seeating guests, undertaking',
        'level_3': 'Level 3 involves someone who does level 2 taks along side any of the following, operating a mechanical lifting device, attending a terminal, full control of liquor store, mixing drinks, training or supervising employees of a lower grade',
        'level_4': 'Level 4 involves an employee who has completed an an apprenticeship or carries out specialised skilled duties ina fine dinging room/restaurant',
        'level_5': 'level 5 involves a appropriate level of training and is responsible for supervision, training and co-ordination of food and beverage of one or more bars',
        'level_6': 'level 6 involves you being a chef'


    }

    Eployee_type_info = {
        'Full time' : 'Full time employees are people that work 38 ordinary hours a week and are a full time employee',
        'Part time' : 'A part time employee has to work between 8 to 38 hours a week and has reasonably predicatble hours of work',
        'Casual'  : 'A casual employee works irregular hours and has no guarantee of work '


    }


    level = st.selectbox('What is your job level', Adult_minimum_rate_weekly)
    st.write(job_level_info[level])
    input_job_type = ['Casual', 'Part time', 'Full time']
    job_type = st.selectbox('What is your employment type', input_job_type)
    st.write(Eployee_type_info[job_type])

    st.subheader('Input Day of Work Information')
    age = st.number_input('How old are you in years')
    d = st.date_input("What is the date of the day you worked ", datetime.date(2023, 9, 18))
    time_1 = st.time_input('What time did you start work', step=3600, key='time_1')
    time_2 = st.time_input(
        'What time did you finish that work', step=3600, key='time_2')

    break_1 = st.checkbox('Did you have a break this shift', key = 'break_1')




    def combine_time_seconds(time_1, date_1, time_2, date_2):
        date = datetime.datetime.combine(date_1, time_1)
        date_2 = datetime.datetime.combine(date_2, time_2)
        date_diff = date_2 - date
        date_diff = date_diff.seconds
        return date_diff


    def combine_time_hours(time_1, date_1, time_2, date_2):
        date = datetime.datetime.combine(date_1, time_1)
        date_2 = datetime.datetime.combine(date_2, time_2)
        date_diff = date_2 - date
        date_diff = date_diff.seconds
        date_diff = date_diff/3600
        return date_diff

    test = combine_time_hours(time_1, d, time_2, d)

    def junior_employee_payment(age):
        percent_rate = int
        if age <17:
            percent_rate = 0.5
        elif age < 18:
            percent_rate = 0.6
        elif age < 19:
            percent_rate = 0.7
        elif age < 20:
            percent_rate = 0.85
        else :
            percent_rate = 1
        return percent_rate

    def junior_employee_office_payment(age):
        percent_rate = int
        if age < 16:
            percent_rate = 0.45
        elif age < 17:
            percent_rate = 0.55
        elif age < 18:
            percent_rate = 0.65
        elif age < 19:
            percent_rate = 0.75
        elif age < 20:
            percent_rate = 0.90
        else:
            percent_rate = 1
        return percent_rate

    junior_employee_office_payment(17.8)
    flat_increase = []
    percent_increase = []

    total_hours = int
    def penelty_rate_hours(time_1, date_1, time_2, date_2):
        initial_date = datetime.datetime.combine(date_1, time_1)
        final_date = datetime.datetime.combine(date_2, time_2)
        date_7am = datetime.datetime(
            final_date.year, final_date.month, final_date.day, 7)
        date_7pm = datetime.datetime(
            final_date.year, final_date.month, final_date.day, 7)
        len_hours = final_date - initial_date
        len_hours = (len_hours.seconds)/3600

        if initial_date.weekday() == 6:
            percent_increase.append(0.75)
        elif initial_date.weekday() == 5:
            percent_increase.append(len_hours * 0.5)
        elif initial_date < date_7am < final_date or final_date < date_7am:
            flat_increase.append(len_hours * 3.93)
        elif final_date > date_7am > initial_date or initial_date > date_7pm:
            flat_increase.append(len_hours * 2.62)
        else:
            pass

        penelty_rate_hours.total_hours = len_hours 

    break_taken = []

    def break_inputs():
        if 5 < penelty_rate_hours.total_hours < 6 & break_1 == True:
            st.write('For a shift between 5-6 hours long you are entitled to a  30 minute unpaid meal break')
        if 5 < penelty_rate_hours.total_hours < 6 & break_1 == False:
            st.write('For a shift between 5-6 hours long you are entitled to a  30 minute unpaid meal break ')
        if 6 < penelty_rate_hours.total_hours < 8 & break_1 == True:
            st.write('for a shift between 6-8 hours long you are entitled to a 30 minute unpaid meal break between the 2nd hour and 6th hour of the shift')
        if 6 < penelty_rate_hours.total_hours < 8 & break_1 == False:
            st.write('for a shift between 6-8 hours long you are entitled to a 30 minute unpaid meal break between the 2nd hour and 6th hour of the shift')
        if 8 < penelty_rate_hours.total_hours < 10 & break_1 == True:
            st.write('for a shift between 8-10 hours long you are entitled to a 30 minute unpaid meal break between the 2nd hour and 6th hour of the shift and 1 20 minute paid break or 2 10 minute paid breaks')
        if 8 < penelty_rate_hours.total_hours < 10 & break_1 == False:
            st.write('for a shift between 8-10 hours long you are entitled to a 30 minute unpaid meal break between the 2nd hour and 6th hour of the shift and 1 20 minute paid break or 2 10 minute paid breaks')
        if penelty_rate_hours.total_hours > 10 & break_1 == True:
            st.write('for a shift between 8-10 hours long you are entitled to a 30 minute unpaid meal break between the 2nd hour and 6th hour of the shift 2 20 minute paid breaks')
        if penelty_rate_hours.total_hours > 10 & break_1 == False:
            st.write('for a shift between 8-10 hours long you are entitled to a 30 minute unpaid meal break between the 2nd hour and 6th hour of the shift 2 20 minute paid breaks')

    penelty_rate_hours(time_1, d, time_2, d)
    break_inputs()

    age_penelty = junior_employee_payment(age)
    test = age_penelty * test
    base_res = (test * Adult_minimum_rate_weekly[level])/38
    fixed_overtime = sum(flat_increase)
    var_overtime = sum(percent_increase) * (Adult_minimum_rate_weekly[level])/38 * test
    casual_rate = 0
    if job_type == 'Casual':
        casual_rate = 0.25
    casual_bonus = int(casual_rate * (Adult_minimum_rate_weekly[level])/38 * test)
    total_res = base_res + fixed_overtime + var_overtime + casual_bonus
    overtime_sum = int(fixed_overtime + var_overtime)
    st.subheader('Payment Results')

    test_res = int(total_res)
    base_res = int(base_res)
    df_list = [[base_res, 'base pay'], [fixed_overtime, 'fixed overtime'], [var_overtime, 'var overtime'], [casual_bonus, 'casual bonus']]
    df = pd.DataFrame(df_list) 

    st.write('you should have earned a minimum of ',  f'${test_res}', 'over this time period' )
    st.write('This is made up of the combination of ', f'${base_res}' ,'in base pay and ' f'{overtime_sum}' ,'in overtime pay')
    st.write('You are receiving ', f'${casual_bonus}' ' for being a casual employee')
    df.columns = ['pay', 'type of bonus']
    df = df[df.pay > 0]
    #st.bar_chart(data=df, y='pay', x='type of bonus')
    plt.figure(figsize=(8, 6))
    plt.bar(df['type of bonus'], df['pay'])
    plt.xlabel('Type of Bonus')
    plt.ylabel('Pay')
    plt.title('Bonus Distribution')
    plt.xticks(rotation=45)  # 可选：旋转 x 轴标签，以适应较长的标签

    # 显示 Matplotlib 图形在 Streamlit 中
    st.pyplot(plt)


        
    # select_class()


    # calculate_penalty()


    # select_rate_type()

    # overtime()