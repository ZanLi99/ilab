import streamlit as st
import datetime
import matplotlib.pyplot as plt

import pandas as pd
from st_session import initialize_st
from function import select_class, select_rate_type, base_rate, calculate_penalty,overtime,get_holiday_df,chooseholiday,calculate_weekend,calculate_salary
from input import inputjob,worktime,work_type,work_time_everyday,salary,choosecountry,part_time_input,salary_type
import random



st.session_state['country'] = pd.read_csv('./country.csv')
st.session_state['awards'] = pd.read_csv('./awards.csv')
st.session_state['classification'] = pd.read_csv('./classification.csv')
st.session_state['classification'] = st.session_state['classification'].apply(lambda x: x.astype(str).str.lower() if x.dtype == "object" else x)
st.session_state['selection_class'] = st.session_state['classification']['classification'].drop_duplicates()
st.session_state['merged'] = pd.read_csv('./merge_classification_penalty.csv')

initialize_st()
#st.write(st.session_state['classification'])

#tab1, tab2 = st.tabs(["penalty", "WageCraft Hospitality Award"])

#with tab1:
    #st.header("penalty")
page = st.sidebar.selectbox("Select Page", ["Salary", "WageCraft Hospitality Award"])

if page == "Salary" or page == "Casual":
    st.header("Salary")
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

elif page == "WageCraft Hospitality Award":
    st.header('WageCraft Hospitality Wage Calculator', divider='gray')
    st.subheader('Industries covered by this award include')
    st.write('- Tourist accomodations')
    st.write('- Restaurancts and convention facilities')
    st.write('- nightclubs, function areas')
    st.subheader('Enter Job Information')

    Adult_minimum_rate_weekly = {
        'Introductory': 859.30,
        'level_1': 882.80,
        'level_2': 913.90,
        'level_3': 945.00,
        'level_4': 995.00,
        'level_5': 1057.40,
        'level_6': 1085.60
    }

    Eployee_type_info = {
        'Full time' : 'Full time employees are people that work 38 ordinary hours a week and are a full time employee',
        'Part time' : 'A part time employee has to work between 8 to 38 hours a week and has reasonably predicatble hours of work',
        'Casual'  : 'A casual employee works irregular hours and has no guarantee of work '


    }

    employment_stream = ['Food and beverage', 'kitchen', 'guest services stream', 'admininistration', 'security', 'leisure activities stream',  'maintenance and trades']

    Job_information = {
    'Food and beverage': {                     
                            'level_1': ['picking up glasses, emptying ashtrays,removing food plates,setting and wiping down tables, cleaning and tidying associated areas  ', Adult_minimum_rate_weekly['level_1']],
                            'level_2': ['handling liquor, assisting in the bottle department, waiting duties, recieving money, taking reservations, greeting and seating guessts', Adult_minimum_rate_weekly['level_2']], 
                            'level_3': ['operating a mechanical lifting device,attending a wagering terminal, electronic gaming terminal or similar terminal, mixing drinks, training staff of a lower grade, supervising staff of a lower grade ', Adult_minimum_rate_weekly['level_3']],
                            'level_4': ['completed an apprenticeshop or passed trade tests to do specialised duties', Adult_minimum_rate_weekly['level_4']],
                            'level_5': ['Have appropriate training including supervisory and has the responsiblity of training, co-ordinating and supervising staff', Adult_minimum_rate_weekly['level_5']]},
    'kitchen' :{'Kitchen attendant grade 1 ': ['general cleaning duties or food preperation, assisting employyes that are cooking, assembling ingredients, general pantry duties',  Adult_minimum_rate_weekly['level_1']],
                'Kitchen attendant grade 2 ': ['who has the appropriate level of training, and who is engaged in specialised non-cooking duties in a kitchen or food preparation area or in supervising kitchen attendants.',  Adult_minimum_rate_weekly['level_2']],
                'Kitchen attendant grade 3': [' who has the appropriate level of training, including a supervisory course, and has responsibility for the supervision, training and co-ordination of kitchen attendants of a lower classification.',  Adult_minimum_rate_weekly['level_3']],
                'cook grade 1 ': ['who is engaged in cooking breakfasts and snacks, baking, pastry cooking or butchering.',  Adult_minimum_rate_weekly['level_2']],
                'cook grade 2 ': ['employee who has the appropriate level of training and who performs cooking duties such as baking, pastry cooking or butchering.',  Adult_minimum_rate_weekly['level_3']],
                'cook grade 3 (tradesperson)  ': ['commi chef or equivalent who has completed an apprenticeship or passed the appropriate trade test and who is engaged in cooking, baking, pastry cooking or butchering duties.',  Adult_minimum_rate_weekly['level_4']],
                'cook grade 4 (tradesperson) ': ['demi chef or equivalent who has completed an apprenticeship or passed the appropriate trade test and who is engaged to perform general or specialised cooking, butchering, baking or pastry cooking duties or supervises and trains other cooks and kitchen employees.',  Adult_minimum_rate_weekly['level_5']],
                'cook grade 5 (tradesperson) ': ['chef de partie or equivalent who has completed an apprenticeship or passed the appropriate trade test in cooking, butchering, baking or pastry cooking and who performs any of the following:, general and specialised duties, including supervision or training of kitchen employees',  Adult_minimum_rate_weekly['level_6']],
                },

    'guest service': { 'level_1': ['laundry duties, repairs to clothing, collecting laundry, general cleaning, parking motor vehicles',  Adult_minimum_rate_weekly['level_1']],
                            'level_2': ['cleaning/servicing accomodation areas, receiving and assisting guests at entrance, driving , transfering baggage, cleaning, bulter services',  Adult_minimum_rate_weekly['level_2']],
                            'level_3': ['supervising staff, butler services, major repairs, dry lceaning',  Adult_minimum_rate_weekly['level_3']],
                            'level_4': ['employee who has completed an apprenticeship or passed the appropriate trade test or otherwise has the appropriate level of training to perform the work of a tradesperson in dry cleaning or tailoring or as a butler.',  Adult_minimum_rate_weekly['level_4']],
                            'level_5': [' employee who has the appropriate level of training, including a supervisory course, and has responsibility for the supervision, training and co-ordination of employees engaged in a housekeeping department',  Adult_minimum_rate_weekly['level_5']]},

    #to add front office!!!

    'admininistration': { 'level_1': ['who is required to perform basic clerical and routine office duties such as collating, filing, photocopying and delivering messages.',  Adult_minimum_rate_weekly['level_2']],
                        'level_2': ['employee who is engaged in general clerical or office duties, such as typing, filing, basic data entry and calculating functions.',  Adult_minimum_rate_weekly['level_3']],
                        'level_3': ['info_1',  Adult_minimum_rate_weekly['level_4']],
                        'clerical supervisor': [' employee who has the appropriate level of training, including a supervisory course, and who co-ordinates other clerical staff.',  Adult_minimum_rate_weekly['level_5']], },

    'security': { 'Door person/security officer grade 1': ['who assists in the maintenance of dress standards and good order at an establishment.',  Adult_minimum_rate_weekly['level_2']],
                'Timekeeper/security officer grade 2': ['person who is responsible for the timekeeping of employees, for the security of keys, for the checking in and out of delivery vehicles or the supervision of doorperson/security officer grade 1 employees',  Adult_minimum_rate_weekly['level_3']] },

    'leisure activities stream': { 'Leisure attendant grade 1;': [' person who acts as an assistant instructor or pool attendant or is responsible for the setting up, distribution and care of equipment and the taking of bookings.',  Adult_minimum_rate_weekly['level_2']],
                                    'Leisure attendant grade 2': [' person who has the appropriate level of training and takes classes or directs leisure activities such as sporting areas, health clubs and swimming pool',  Adult_minimum_rate_weekly['level_3']],
                                    'Leisure attendant grade 3': [' a person who has the appropriate level of training and who plans and co-ordinates leisure activities for guests and may supervise other leisure attendant',  Adult_minimum_rate_weekly['level_4']], },

    'Stores stream': { 'Storeperson grade 1': ['employee who receives and stores general and perishable goods and cleans the store area.',  Adult_minimum_rate_weekly['level_2']],
                                'Storeperson grade 2': ['employee who, in addition to the duties for a storeperson grade 1, may also operate mechanical lifting equipment such as a fork-lift or who may perform duties of a more complex nature',  Adult_minimum_rate_weekly['level_3']],
                                'Storeperson grade 3;': ['appropriate levels of training',  Adult_minimum_rate_weekly['level_4']],},

    'maintenance and trades': { 'Handyperson': ['who is not a tradesperson and whose duties include performing routine repair work and maintenance in and about the employer’s premises.',  Adult_minimum_rate_weekly['level_3']],
                                'Fork-lift driver': ['employee who has a recognised fork-lift licence and who is engaged solely to drive a fork-lift vehicle',  Adult_minimum_rate_weekly['level_3']],
                                'Gardener grade 1': ['keeping areas tidy, weeding/watering, trimming, assisting in prepareing areas for play, assisting in green maintinebce/construction, operating a limited range of vehicles',  Adult_minimum_rate_weekly['level_2']],
                                'Gardener grade 2': ['handyperson, supervising, completing records, maintinence for turn, ',  Adult_minimum_rate_weekly['level_3']],
                                'Gardener grade 3 (tradesperson)': ['operating machinery, supervision of employyes, training apprentices, applying fertiliser, fungicides, herbicides, insectisides',  Adult_minimum_rate_weekly['level_4']],
                                'Gardener grade 4 (tradesperson)': ['has the training for grade 3 and is supervising tradespersons, writing reports, general liason with management, performing specialist skills',  Adult_minimum_rate_weekly['level_5']],

    }                       
    }

    stream = st.selectbox('What stream are you part of', employment_stream)
    job_type_2 = st.selectbox('Job Type',Job_information[stream] )
    st.write('This is some of what you are expected to do in this role')
    st.write(Job_information[stream][job_type_2][0])
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
    base_res = (test * Job_information[stream][job_type_2][1])/38
    fixed_overtime = sum(flat_increase)
    var_overtime = sum(percent_increase) * (Job_information[stream][job_type_2][1])/38 * test
    casual_rate = 0
    if job_type == 'Casual':
        casual_rate = 0.25
    casual_bonus = int(casual_rate * (Job_information[stream][job_type_2][1])/38 * test)
    total_res = base_res + fixed_overtime + var_overtime + casual_bonus
    overtime_sum = int(fixed_overtime + var_overtime)
    st.subheader('Payment Results')

    test_res = int(total_res)
    base_res = int(base_res)
    df_list = [[base_res, 'base pay'], [fixed_overtime, 'fixed overtime'], [var_overtime, 'var overtime'], [casual_bonus, 'casual bonus']]
    df = pd.DataFrame(df_list) 

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
    plt.xticks(rotation=45)  
    st.pyplot(plt)


        
    # select_class()


    # calculate_penalty()


    # select_rate_type()

    # overtime()