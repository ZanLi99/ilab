import streamlit as st
import datetime
import pandas as pd
from function import get_holiday, get_holiday_df

from input import work_type


def part_time_salary():
    st.title( "What's your salary?")
    User_salary = st.number_input("Your salary:",0)
    st.session_state['User_salary'] = User_salary

def part_time_date_salary():
    if len(st.session_state['worktime']) >=2:
        st.write(st.session_state['worktime'])
        start_date = st.session_state['worktime'][0]
        end_date = st.session_state['worktime'][1]

        date_range = pd.date_range(start_date, end_date)
        public_holiday = pd.to_datetime(st.session_state['holiday']['date'])

        #st.write(public_holiday)
        df = pd.DataFrame({
            'Year': date_range.year,
            'Month': date_range.month,
            'Day': date_range.day,
            'DayOfWeek': date_range.day_name(),
        })
        df['Month'] = df['Month'].map({1: 'January', 2: 'February', 3: 'March', 4: 'April', 5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September', 10: 'October', 11: 'November', 12: 'December'})
        df['7am-7pm'] = 0
        df['7pm-00:00'] = 0
        df['00:00-7pm'] = 0
        date_df = st.data_editor(
        df,
        column_config={
            "worktime": st.column_config.NumberColumn(
                min_value=0,
                max_value=24,
                step=1,
            ),
        },
        hide_index=True,
        )

        # percent_rate = int
        # if st.session_state['age'] == "16 years of age and under":
        #         percent_rate = 0.45
        # if st.session_state['age'] =="17 years of age":
        #     percent_rate = 0.5
        # elif st.session_state['age'] ==  "18 years of age":
        #     percent_rate = 0.6
        # elif st.session_state['age'] =="19 years of age":
        #     percent_rate = 0.7
        # elif st.session_state['age'] =="20 years of age and above":
        #     percent_rate = 0.85
        # else :
        #     percent_rate = 1

        # regular_salary = sum(date_df['7am-7pm'] * st.session_state['User_salary'] * percent_rate)
        # penalty_salary = (sum(date_df['7pm-00:00'] * st.session_state['User_salary']*2.62) + (sum(date_df['00:00-7pm'] * st.session_state['User_salary'])*3.92)* percent_rate)
        # st.write(sum(date_df['7am-7pm'] * st.session_state['User_salary']))

        # date_df['Date'] = pd.to_datetime(date_df['Year'].astype(str) + date_df['Month'] + date_df['Day'].astype(str), format="%Y%B%d")
        # weekly_summary = date_df.groupby(pd.Grouper(key='Date', freq='W-SUN'))[['7am-7pm','7pm-00:00','00:00-7pm']].sum()
        
        # st.write(weekly_summary)
        total_hours = 0
        weekly_wages = 0

        overtime_rate_1 = 1.5  
        overtime_rate_2 = 2.0 

        part_time_rate = {
            '7am-7pm': 1,
            '7pm-00:00': 2.62,
            '00:00-7pm': 3.93
        }
        if st.session_state['work_type'] == "Part Time":
            basic_rate = 1
            Saturday = 1.25
            Sunday = 1.5
            holiday = 2.25
        else:
            basic_rate = 1.25
            Saturday = 1.5
            Sunday = 1.75
            holiday_rate = 2.5
        
        
        df_copy = date_df.copy()
        df_copy['Date'] = pd.to_datetime(df_copy['Year'].astype(str) + df_copy['Month'] + df_copy['Day'].astype(str), format="%Y%B%d")

        for index, row in df_copy.iterrows():
            if row['Date'].date() in public_holiday:
                holiday_rate = holiday
            else:
                holiday_rate = 1
            if row['DayOfWeek'] == 'Saturday':
                public_rate = Saturday
            if row['DayOfWeek'] == 'Sunday':
                public_rate = Sunday
            else:
                public_rate = 1
            daily_wages = 0
            for column in ['7am-7pm', '7pm-00:00', '00:00-7pm']:
                hours = row[column] * basic_rate 
                rate = part_time_rate[column] * public_rate * holiday_rate

                if total_hours < 38:
                    if total_hours + hours <= 38:
                        daily_wages += hours * rate
                    else:
                        remaining_hours = 38 - total_hours
                        daily_wages += remaining_hours * rate
                        daily_wages += 2*overtime_rate_1 * rate
                        overtime = (hours - remaining_hours - 2)
                        if overtime >= 0:
                            daily_wages+=overtime * overtime_rate_2 * rate
                        if overtime < 0:
                            daily_wages+=overtime * overtime_rate_1 * rate
                else:
                    if total_hours + hours <= 40:
                        daily_wages += hours * rate * overtime_rate_1
                    else:
                        if total_hours < 40:
                            remaining_hours = 40 - total_hours
                            daily_wages += remaining_hours * rate * overtime_rate_1
                            daily_wages += (hours - remaining_hours) * rate * overtime_rate_2 
                        else:
                            daily_wages += hours * rate * overtime_rate_2 

                total_hours += hours

            weekly_wages += daily_wages
            df_copy.at[index, 'Daily_Wages'] = daily_wages
            df_copy.at[index, 'Weekly_Wages'] = weekly_wages
            if row['DayOfWeek'] == 'Sunday':
                total_hours = 0
                weekly_wages = 0

        total_salary = sum(df_copy['Daily_Wages'] * st.session_state['User_salary'])

        #st.write(df_copy)
        st.write('Your total salary is:', total_salary)
