import streamlit as st
import datetime
import pandas as pd

#st.time_input(datetime.time)
st.set_page_config(page_title='WageCraft Hospitality Award')


st.header('WageCraft Hospitality Wage Calculator', divider='gray')
st.subheader('Input Job information')
Adult_minimum_rate_weekly = {
    'Introductory': 859.30,
    'level_1': 882.80,
    'level_2': 913.90,
    'level_3': 945.00,
    'level_4': 995.00,
    'level_5': 1057.40,
    'level_6': 1085.60
}
level = st.selectbox('What is your job level', Adult_minimum_rate_weekly)

input_job_type = ['Casual', 'Part time', 'Full time']
job_type = st.selectbox('What is your employment type', input_job_type)
st.subheader('Input Day of Work Information')
age = st.number_input('How old are you in years')
d = st.date_input("What is the date of the day you worked ", datetime.date(2023, 9, 18))
time_1 = st.time_input('What time did you start work', step=3600, key='time_1')
time_2 = st.time_input(
    'What time did you finish that work', step=3600, key='time_2')
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
    print(percent_rate)
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
    print(percent_rate)
    return percent_rate

junior_employee_office_payment(17.8)
flat_increase = []
percent_increase = []


def penelty_rate_hours(time_1, date_1, time_2, date_2):
    initial_date = datetime.datetime.combine(date_1, time_1)
    final_date = datetime.datetime.combine(date_2, time_2)
    date_7am = datetime.datetime(
        final_date.year, final_date.month, final_date.day, 7)
    date_7pm = datetime.datetime(
        final_date.year, final_date.month, final_date.day, 7)

    if initial_date.weekday() == 6:
        len_hours = final_date - initial_date
        len_hours = (len_hours.seconds)/3600
        percent_increase.append(0.75)
    elif initial_date.weekday() == 5:
        len_hours = final_date - initial_date
        len_hours = (len_hours.seconds)/3600
        percent_increase.append(len_hours * 0.5)
    elif initial_date < date_7am < final_date or final_date < date_7am:
        len_early = date_7am - initial_date
        len_early = (len_early.seconds)/3600
        flat_increase.append(len_early * 3.93)
    elif final_date > date_7am > initial_date or initial_date > date_7pm:
        len_late = date_7am - final_date
        len_late = (len_late.seconds)/3600
        flat_increase.append(len_late * 2.62)
    else:
        pass


penelty_rate_hours(time_1, d, time_2, d)
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
st.bar_chart(data=df, y='pay', x='type of bonus')
