import streamlit as st
import datetime
import matplotlib.pyplot as plt
from PIL import Image
import streamlit as st
import seaborn as sns
import pandas as pd
from st_session import initialize_st

from function import select_class, select_rate_type, base_rate, calculate_penalty,overtime,get_holiday_df,chooseholiday,calculate_weekend,calculate_salary, calculate_overtime_FT
from input import inputjob,worktime,work_type,work_time_everyday,salary,choosecountry,part_time_input,salary_type
import random

# from model import filter_job
from function import select_class, select_rate_type, base_rate, calculate_penalty,overtime
from input import inputjob,worktime,work_type,work_time_everyday,salary, age
from part_time import part_time_salary,part_time_date_salary




st.session_state['country'] = pd.read_csv('./streamlit/files/country.csv')
st.session_state['awards'] = pd.read_csv('./streamlit/files/awards.csv')
st.session_state['classification'] = pd.read_csv('./streamlit/files/classification.csv')
st.session_state['classification'] = st.session_state['classification'].apply(lambda x: x.astype(str).str.lower() if x.dtype == "object" else x)
st.session_state['selection_class'] = st.session_state['classification']['classification'].drop_duplicates()
st.session_state['merged'] = pd.read_csv('./streamlit/files/merge_classification_penalty.csv')



st.write('<div style="text-align: center; font-size: 48px; font-weight: bold;">W.A.G.E.S</div>', unsafe_allow_html=True)


image = Image.open('./streamlit/Pictures/MicrosoftTeams-image.png')
st.image(image, caption='MicrosoftTeams-image')
#st.markdown("---")
st.write('<hr style="border: 2px solid #000;">', unsafe_allow_html=True)

initialize_st()
#st.write(st.session_state['classification'])

#tab1, tab2 = st.tabs(["penalty", "WageCraft Hospitality Award"])

#with tab1:
    #st.header("penalty")
page = st.sidebar.selectbox("WageCraft Hospitality Wage Calculator", ["Calculation", "Prediction"])

if page == "Calculation" :
    #st.header("Salary")
    choosecountry()
    work_type()
    
    if  st.session_state['work_type'] == 'Full Time' :
        #inputjob()
        #age()
        salary_type()
        salary()
        worktime()
        work_time_everyday()
        get_holiday_df()
        chooseholiday() 
        calculate_weekend()
        calculate_penalty()
        calculate_overtime_FT()
        # st.write(st.session_state["overtime_FT"])
        # st.write(st.session_state['full_time_ot_hour'])
        calculate_salary()
    if  st.session_state['work_type'] == 'Part Time' or  st.session_state['work_type'] == "Casual":
        #age()
        #salary()
        #part_time_input()
        part_time_salary()
        worktime()
        with st.expander("Explanation of Working Shift"):
            st.write("Day Shift = 7.00 am to 7.00 pm")
            st.write("Evening Shift = 7.00 pm to midnight")
            st.write("Night Shift = midnight to 7.00 am")
        part_time_date_salary()
        

elif page == "Prediction":
    #st.set_page_config(page_title='WageCraft Hospitality Award')

    st.header('WageCraft Hospitality Wage Calculator', divider='gray')
    st.subheader('Some of the Industries covered by this award include', help = 'To help find out what industry you are in use [This link](https://www.fairwork.gov.au/employment-conditions/awards/awards-summary/ma000009-summary)')
    st.write('- Tourist accomodations')
    st.write('- restaurants and convention facilities')
    st.write('- nightclubs function areas')
    st.subheader('Enter Job Information', divider='gray')

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
                            'level 1': ['picking up glasses, emptying ashtrays,removing food plates,setting and wiping down tables, cleaning and tidying associated areas  ', Adult_minimum_rate_weekly['level_1']],
                            'level 2': ['handling liquor, assisting in the bottle department, waiting duties, recieving money, taking reservations, greeting and seating guessts', Adult_minimum_rate_weekly['level_2']], 
                            'level 3': ['operating a mechanical lifting device,attending a wagering terminal, electronic gaming terminal or similar terminal, mixing drinks, training staff of a lower grade, supervising staff of a lower grade ', Adult_minimum_rate_weekly['level_3']],
                            'level 4': ['completed an apprenticeshop or passed trade tests to do specialised duties', Adult_minimum_rate_weekly['level_4']],
                            'level 5': ['Have appropriate training including supervisory and has the responsiblity of training, co-ordinating and supervising staff', Adult_minimum_rate_weekly['level_5']]},
    'Kitchen' :{'Kitchen attendant grade 1 ': ['general cleaning duties or food preperation, assisting employyes that are cooking, assembling ingredients, general pantry duties',  Adult_minimum_rate_weekly['level_1']],
                'Kitchen attendant grade 2 ': ['who has the appropriate level of training, and who is engaged in specialised non-cooking duties in a kitchen or food preparation area or in supervising kitchen attendants.',  Adult_minimum_rate_weekly['level_2']],
                'Kitchen attendant grade 3': [' who has the appropriate level of training, including a supervisory course, and has responsibility for the supervision, training and co-ordination of kitchen attendants of a lower classification.',  Adult_minimum_rate_weekly['level_3']],
                'Cook grade 1 ': ['who is engaged in cooking breakfasts and snacks, baking, pastry cooking or butchering.',  Adult_minimum_rate_weekly['level_2']],
                'Cook grade 2 ': ['employee who has the appropriate level of training and who performs cooking duties such as baking, pastry cooking or butchering.',  Adult_minimum_rate_weekly['level_3']],
                'Cook grade 3 (tradesperson)  ': ['commi chef or equivalent who has completed an apprenticeship or passed the appropriate trade test and who is engaged in cooking, baking, pastry cooking or butchering duties.',  Adult_minimum_rate_weekly['level_4']],
                'Cook grade 4 (tradesperson) ': ['demi chef or equivalent who has completed an apprenticeship or passed the appropriate trade test and who is engaged to perform general or specialised cooking, butchering, baking or pastry cooking duties or supervises and trains other cooks and kitchen employees.',  Adult_minimum_rate_weekly['level_5']],
                'Cook grade 5 (tradesperson) ': ['chef de partie or equivalent who has completed an apprenticeship or passed the appropriate trade test in cooking, butchering, baking or pastry cooking and who performs any of the following:, general and specialised duties, including supervision or training of kitchen employees',  Adult_minimum_rate_weekly['level_6']],
                },

    'Guest Service': { 'level 1': ['laundry duties, repairs to clothing, collecting laundry, general cleaning, parking motor vehicles',  Adult_minimum_rate_weekly['level_1']],
                            'level 2': ['cleaning/servicing accomodation areas, receiving and assisting guests at entrance, driving , transfering baggage, cleaning, bulter services',  Adult_minimum_rate_weekly['level_2']],
                            'level 3': ['supervising staff, butler services, major repairs, dry lceaning',  Adult_minimum_rate_weekly['level_3']],
                            'level 4': ['employee who has completed an apprenticeship or passed the appropriate trade test or otherwise has the appropriate level of training to perform the work of a tradesperson in dry cleaning or tailoring or as a butler.',  Adult_minimum_rate_weekly['level_4']],
                            'level 5': [' employee who has the appropriate level of training, including a supervisory course, and has responsibility for the supervision, training and co-ordination of employees engaged in a housekeeping department',  Adult_minimum_rate_weekly['level_5']]},

    'Admininistration': { 'level 1': ['who is required to perform basic clerical and routine office duties such as collating, filing, photocopying and delivering messages.',  Adult_minimum_rate_weekly['level_2']],
                        'level 2': ['employee who is engaged in general clerical or office duties, such as typing, filing, basic data entry and calculating functions.',  Adult_minimum_rate_weekly['level_3']],
                        'level 3': ['info_1',  Adult_minimum_rate_weekly['level_4']],
                        'Clerical supervisor': [' employee who has the appropriate level of training, including a supervisory course, and who co-ordinates other clerical staff.',  Adult_minimum_rate_weekly['level_5']], },

    'Security': { 'Door person/security officer grade 1': ['who assists in the maintenance of dress standards and good order at an establishment.',  Adult_minimum_rate_weekly['level_2']],
                'Timekeeper/security officer grade 2': ['person who is responsible for the timekeeping of employees, for the security of keys, for the checking in and out of delivery vehicles or the supervision of doorperson/security officer grade 1 employees',  Adult_minimum_rate_weekly['level_3']] },

    'Leisure Activities Stream': { 'Leisure attendant grade 1;': [' person who acts as an assistant instructor or pool attendant or is responsible for the setting up, distribution and care of equipment and the taking of bookings.',  Adult_minimum_rate_weekly['level_2']],
                                    'Leisure attendant grade 2': [' person who has the appropriate level of training and takes classes or directs leisure activities such as sporting areas, health clubs and swimming pool',  Adult_minimum_rate_weekly['level_3']],
                                    'Leisure attendant grade 3': [' a person who has the appropriate level of training and who plans and co-ordinates leisure activities for guests and may supervise other leisure attendant',  Adult_minimum_rate_weekly['level_4']], },

    'Stores Stream': { 'Storeperson grade 1': ['employee who receives and stores general and perishable goods and cleans the store area.',  Adult_minimum_rate_weekly['level_2']],
                                'Storeperson grade 2': ['employee who, in addition to the duties for a storeperson grade 1, may also operate mechanical lifting equipment such as a fork-lift or who may perform duties of a more complex nature',  Adult_minimum_rate_weekly['level_3']],
                                'Storeperson grade 3;': ['appropriate levels of training',  Adult_minimum_rate_weekly['level_4']],},

    'Maintenance and Trades': { 'Handyperson': ['who is not a tradesperson and whose duties include performing routine repair work and maintenance in and about the employer’s premises.',  Adult_minimum_rate_weekly['level_3']],
                                'Fork-lift driver': ['employee who has a recognised fork-lift licence and who is engaged solely to drive a fork-lift vehicle',  Adult_minimum_rate_weekly['level_3']],
                                'Gardener grade 1': ['keeping areas tidy, weeding/watering, trimming, assisting in prepareing areas for play, assisting in green maintinebce/construction, operating a limited range of vehicles',  Adult_minimum_rate_weekly['level_2']],
                                'Gardener grade 2': ['handyperson, supervising, completing records, maintinence for turn, ',  Adult_minimum_rate_weekly['level_3']],
                                'Gardener grade 3 (tradesperson)': ['operating machinery, supervision of employyes, training apprentices, applying fertiliser, fungicides, herbicides, insectisides',  Adult_minimum_rate_weekly['level_4']],
                                'Gardener grade 4 (tradesperson)': ['has the training for grade 3 and is supervising tradespersons, writing reports, general liason with management, performing specialist skills',  Adult_minimum_rate_weekly['level_5']],

    }                       
    }
    input_job_type = ['Casual', 'Part time', 'Full time']

    day_of_week_dict = {
        0 : 'Monday',
        1 : 'Tuesday',
        2 : 'Wednesday',
        3 : 'Thursday',
        4 : 'Friday',
        5 : 'Saturday',
    6 : 'Sunday',
    }



    stream = st.selectbox('What part of hospitality do you work in', employment_stream)
    job_type_2 = st.selectbox('Which of the following best describes your position',Job_information[stream] , help='For more information go to [link](https://library.fairwork.gov.au/award/?krn=MA000009) ')
    st.write('This is some of your job expectations')
    st.write(Job_information[stream][job_type_2][0])
    job_type = st.selectbox('What is your employment type', input_job_type)
    st.write(Eployee_type_info[job_type])
    age = st.number_input('Enter your age in years')
    st.header('Hours worked in the last week', divider='gray')
    d_1 = datetime.datetime.now() - datetime.timedelta(days=6)
    st.subheader(f'Enter Hours for {d_1.day}/{d_1.month}/{d_1.month} ({day_of_week_dict[d_1.weekday()]})')
    time_1_1 = st.time_input('What time did you start work', step=3600, key='time_1_1')
    time_1_2 = st.time_input('What time did you finish that work', step=3600, key='time_1_2')

    d_2 = datetime.datetime.now() - datetime.timedelta(days=5)
    st.subheader(f'Enter Hours for {d_2.day}/{d_2.month}/{d_2.month} ({day_of_week_dict[d_2.weekday()]})')
    time_2_1 = st.time_input('What time did you start work', step=3600, key='time_2_1')
    time_2_2 = st.time_input('What time did you finish that work', step=3600, key='time_2_2')


    d_3 = datetime.datetime.now() - datetime.timedelta(days=4)
    st.subheader(f'Enter Hours for {d_3.day}/{d_3.month}/{d_3.month} ({day_of_week_dict[d_3.weekday()]})')
    time_3_1 = st.time_input('What time did you start work', step=3600, key='time_3_1')
    time_3_2 = st.time_input('What time did you finish that work', step=3600, key='time_3_2')

    d_4 = datetime.datetime.now() - datetime.timedelta(days=3)
    st.subheader(f'Enter Hours for {d_4.day}/{d_4.month}/{d_4.month} ({day_of_week_dict[d_4.weekday()]})')
    time_4_1 = st.time_input('What time did you start work', step=3600, key='time_4_1')
    time_4_2 = st.time_input('What time did you finish that work', step=3600, key='time_4_2')

    d_5 = datetime.datetime.now() - datetime.timedelta(days=2)
    st.subheader(f'Enter Hours for {d_5.day}/{d_5.month}/{d_5.month} ({day_of_week_dict[d_5.weekday()]})')
    time_5_1 = st.time_input('What time did you start work', step=3600, key='time_5_1')
    time_5_2 = st.time_input('What time did you finish that work', step=3600, key='time_5_2')

    d_6 = datetime.datetime.now() - datetime.timedelta(days=1)
    st.subheader(f'Enter Hours for {d_6.day}/{d_6.month}/{d_6.month} ({day_of_week_dict[d_6.weekday()]})')
    time_6_1 = st.time_input('What time did you start work', step=3600, key='time_6_1')
    time_6_2 = st.time_input('What time did you finish that work', step=3600, key='time_6_2')

    d_7 = datetime.datetime.now() 
    st.subheader(f'Enter Hours for {d_7.day}/{d_7.month}/{d_7.month} ({day_of_week_dict[d_7.weekday()]})')
    time_7_1 = st.time_input('What time did you start work', step=3600, key='time_7_1')
    time_7_2 = st.time_input('What time did you finish that work', step=3600, key='time_7_2')

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

    hours_1 = combine_time_hours(time_1_1, d_1, time_1_2, d_1)
    hours_2 = combine_time_hours(time_2_1, d_2, time_2_2, d_2)
    hours_3 = combine_time_hours(time_3_1, d_3, time_3_2, d_3)
    hours_4 = combine_time_hours(time_4_1, d_4, time_4_2, d_4)
    hours_5 = combine_time_hours(time_5_1, d_5, time_5_2, d_5)
    hours_6 = combine_time_hours(time_6_1, d_6, time_6_2, d_6)
    hours_7 = combine_time_hours(time_7_1, d_7, time_7_2, d_7)


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

    break_taken = []

    def break_inputs(penelty_rate_hours, break_1):
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





    columns_2 = ['Day', 'Hours Worked', 'Base wage',  'Hourly pay', 'Penalty rates', 'Casual Bonus', 'Total Pay']
    def get_payment(hours, time_1, d_1, time_2, d_2):
        flat_increase = []
        percent_increase = []
        total_hours = 0
        day_of_week = day_of_week_dict[d_1.weekday()]
        initial_date = datetime.datetime.combine(d_1, time_1)
        final_date = datetime.datetime.combine(d_2, time_2)
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
        total_hours = len_hours 
        age_penalty = junior_employee_payment(age)
        pay = age_penalty * Job_information[stream][job_type_2][1]/38
        hours = age_penalty * len_hours
        base_res = (hours * Job_information[stream][job_type_2][1])/38
        fixed_overtime = sum(flat_increase)
        var_overtime = sum(percent_increase) * (Job_information[stream][job_type_2][1])/38 * hours
        base_pay = (Job_information[stream][job_type_2][1])/38
        casual_rate = 0
        if job_type == 'Casual':
            casual_rate = 0.25
        casual_bonus = round(casual_rate * (Job_information[stream][job_type_2][1])/38 * hours,2)
        total_res = base_res + fixed_overtime + var_overtime + casual_bonus
        overtime_sum = round(fixed_overtime + var_overtime, 2)
        df_list = [day_of_week, total_hours ,pay, base_res, overtime_sum,casual_bonus, total_res]
        df = pd.DataFrame(df_list).T
        return df

    df_1 = get_payment(hours_1, time_1_1, d_1, time_1_2, d_1)
    df_2 = get_payment(hours_2, time_2_1, d_2, time_2_2, d_2)
    df_3 = get_payment(hours_3, time_3_1, d_3, time_3_2, d_3)
    df_4 = get_payment(hours_4, time_4_1, d_4, time_4_2, d_4)
    df_5 = get_payment(hours_5, time_5_1, d_5, time_5_2, d_5)
    df_6 = get_payment(hours_6, time_6_1, d_6, time_6_2, d_6)
    df_7 = get_payment(hours_7, time_7_1, d_7, time_7_2, d_7)
    df = pd.concat([df_1, df_2, df_3, df_4, df_5, df_6, df_7])
    df.columns = columns_2

    st.header('Expected Payment Information', divider ='gray')
    st.write(f'In total you should have earnt ${round(df["Total Pay"].sum(),2)} this week broken down in the following table')
    st.dataframe(df, hide_index=True)
    st.divider()
    columns_2 = ['Day', 'Hours Worked', 'Base Pay',  'Total Pay', 'Penalty rates', 'Casual Bonus']

    st.subheader('The following is a visual represenation of how your pay was calculated')
    fig = sns.barplot(df, x = 'Total Pay', y = 'Day',)
    fig.set(xlabel = 'Amount Paid', ylabel = 'Day of Week')
    fig.set_title('Amount Paid on each day')
    st.pyplot(fig.figure)
    st.divider()

    ls = [[df['Hourly pay'].sum(), 'Hourly pay'], [df['Penalty rates'].sum(), 'Penalty rates'], [df['Casual Bonus'].sum(), 'Casual Bonus']]
    df_2 = pd.DataFrame(ls)
    df_2.columns = ['Payment Amount', 'Payment Type']
    fig = sns.barplot(df_2, x = 'Payment Amount', y = 'Payment Type')
    fig.set_title('Amount Paid by types of pay')
    st.pyplot(fig.figure)

    st.divider()
    with st.expander('Application limitations'):
        st.write(
            'There are some limitations to the Hospitality wage calculator such as not including breaks, public holidays, overtime or superannuation The award does not cover all types of jobs covered in the hospitality award such as office workers or casino workers.     This application is also limited in not allowing you to work past midnight on a day and may use an out of date award. This application does not account for part-time workers that dont have the same regular hours as an fulltime-employee'
    )
        
    st.write('For more information go to [Fairwork Ombudsman](https://library.fairwork.gov.au/award/?krn=MA000009) or to [Australian Payroll Association](https://www.austpayroll.com.au/)')



# inputjob()
# work_type()

# salary()
# work_time_everyday()
# worktime()

        
    # select_class()


    # calculate_penalty()


    # select_rate_type()

    # overtime()