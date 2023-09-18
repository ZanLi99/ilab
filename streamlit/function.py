import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from base_rate import base_rate, base_rate_c, base_rate_p
from datetime import datetime, timedelta



import dash
from dash import dcc
from dash import html
from dash.dependencies import Input, Output


def input():
    st.title("input")
    user_input = st.text_input("your text", "")
    st.write("What's your role:", user_input)
    st.session_state['input'] = user_input

def select_class():
    classification = st.session_state['classification'][st.session_state['classification']['classification'].str.contains(st.session_state['input'], case=False, na='ignore')]
    classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
    temp = classification['classification']
    temp = temp.drop_duplicates()
    temp = sorted(temp)
    with st.form('sub_class'):
        selected_values = st.multiselect("what classification do you fall under", temp)
        submit = st.form_submit_button(label='class_submit')
        if submit:
            st.session_state['current_class'] = []
            st.session_state['current_class'].extend(selected_values)
        st.write('you have submitted ', st.session_state['current_class'])


def calculate_penalty():
    if st.session_state['input']:
        filtered_df = st.session_state['merged'][st.session_state['merged']['classification'].str.contains(st.session_state['input'], case=False)]
        average_rate = filtered_df['rate'].mean()
        st.session_state['penalty_rate'] = average_rate
        st.write(st.session_state['penalty_rate'])



def select_rate_type():
    tab1, tab2 = st.tabs(["Full Time / Part Time", "Casual"])
    with tab1:
        base_rate_type = {"Annual", "Monthly", "Weekly", "Daily", "Hourly"}

        with st.form('base_rate'):
            current_rate_type = st.selectbox('What type of base rate', options=sorted(base_rate_type), key='base_rate')
            submitted = st.form_submit_button(label='Submit')

            if submitted:
                st.session_state['current_rate_type'] = current_rate_type

                st.write('You have submitted ', current_rate_type)
                if current_rate_type == "Hourly":
                    st.write("For Full Time worker, normally 40hours * 52weeks = 2080hours annually")
                if current_rate_type == "Daily":
                    st.write("For Full Time worker, normally 5days * 52weeks = 260days annually")

        user_salary = st.text_input("What is your salary? ", "")
        if user_salary:
            st.session_state['user_salary'] = user_salary
        #penalty_hours = st.text_input("How many hours of your penalty? ", "")
        st.write("Salary:", user_salary, "(", current_rate_type, ")")
        #st.write("Penalty:", penalty_hours, "(","hours",")")

        if current_rate_type == "Daily" or current_rate_type == "Hourly":
            # Create a layout with two columns
            col1, col2 = st.columns(2)
            with col1:
                if current_rate_type == "Daily":
                    weekday = st.text_input("How many working days on weekday in total?", "260")
                    st.write("Days:", weekday)
                if current_rate_type == "Hourly":
                    weekday = st.text_input("How many working hours on weekday in total?", "2080")
                    st.write("Hours:", weekday)

            with col2:
                if current_rate_type == "Daily":
                    holiday = st.text_input("How many working days on holiday in total?", "0")
                    st.write("Days:", holiday)
                if current_rate_type == "Hourly":
                    holiday = st.text_input("How many working hours on holiday in total?", "0")
                    st.write("Hours:", holiday)


        # Store the user's salary in session state
        st.session_state['user_salary'] = user_salary
        st.session_state['current_rate_type'] = current_rate_type
        if current_rate_type == "Daily" or current_rate_type == "Hourly":
            base_rate_p(st.session_state.get('user_salary', None), st.session_state.get('current_rate_type', None),
                      weekday, holiday)
        else:
            base_rate(st.session_state.get('user_salary', None), st.session_state.get('current_rate_type', None))



    with tab2:
        base_rate_type = {"Daily", "Hourly"}

        with st.form('base_rate_c'):
            current_rate_type_p = st.selectbox('What type of base rate', options=sorted(base_rate_type), key='base_rate_c')

            submitted = st.form_submit_button(label='Submit')

            if submitted:
                st.session_state['current_rate_type'] = current_rate_type_p
                st.write('You have submitted ', current_rate_type)


        user_salary_p = st.text_input("What is your salary? (Casual)", "")
        if user_salary_p:
            st.session_state['user_salary'] = user_salary_p

        #penalty_hours_p = st.text_input("How many hours of your penalty ? ", "")

        st.write("Salary:", user_salary_p, "(", current_rate_type_p, ")")
        #st.write("Penalty:", penalty_hours_p, "(","hours",")")

        # Create a layout with two columns
        col1, col2 = st.columns(2)
        with col1:
            if current_rate_type_p == "Daily":
                weekday = st.text_input("How many working days on weekday in total?", "0", key = "casual_daily_weekday")
                st.write("Days:", weekday)
            if current_rate_type_p == "Hourly":
                weekday = st.text_input("How many working hours on weekday in total?", "0", key = "casual_hourly_weekday")
                st.write("Hours:", weekday)

        with col2:
            if current_rate_type_p == "Daily":
                holiday = st.text_input("How many working days on holiday in total?", "0", key = "casual_daily_holiday")
                st.write("Days:", holiday)
            if current_rate_type_p == "Hourly":
                holiday = st.text_input("How many working hours on holiday in total?", "0", key = "casual_hourly_holiday")
                st.write("Hours:", holiday)

        # Store the user's salary in session state
        st.session_state['user_salary_p'] = user_salary_p
        st.session_state['current_rate_type_p'] = current_rate_type_p

        base_rate_c(st.session_state.get('user_salary_p', None), st.session_state.get('current_rate_type_p', None), weekday, holiday)

def overtime():
    start_time_str = st.text_input("Start time (format: dd-mm-yyyy)", "")
    end_time_str = st.text_input("End time (format: dd-mm-yyyy)", "")

    try:
        start_time = datetime.strptime(start_time_str, "%d-%m-%Y")
        end_time = datetime.strptime(end_time_str, "%d-%m-%Y")
        st.write("The period time is:", start_time.strftime("%d-%m-%Y"), "to", end_time.strftime("%d-%m-%Y"))

        start_date = datetime.strptime(start_time_str, "%d-%m-%Y")
        end_date = datetime.strptime(end_time_str, "%d-%m-%Y")
    except ValueError:
        st.write("Please correct format: dd-mm-yyyy)")
    
    if st.session_state['current_rate_type'] == "Annual" and st.session_state['user_salary']:
        salary = int(st.session_state['user_salary'])/2080
    if st.session_state['current_rate_type'] == "Monthly" and st.session_state['user_salary']:
        salary = int(st.session_state['user_salary'])/173
    if st.session_state['current_rate_type'] == "Weekly" and st.session_state['user_salary']:
        salary = int(st.session_state['user_salary'])/40
    if st.session_state['current_rate_type'] == "Daily" and st.session_state['user_salary']:
        salary = int(st.session_state['user_salary'])/8
    if st.session_state['current_rate_type'] == "Hourly" and st.session_state['user_salary']:
        salary = int(st.session_state['user_salary'])

    days = st.number_input("How many working hours for your penalty?") 
    
    workday_count = count_workdays(start_date, end_date)
    if workday_count and salary:
        sum_salary = salary * workday_count * 8
        sum_penalty = salary * st.session_state['penalty_rate']/100 * days
        total = sum_salary + sum_penalty

        fig1, ax1 = plt.subplots()
        colors = ['#ff9999','#66b3ff','#99ff99']
        ax1.pie([sum_penalty,total], labels=['penalty','salary'], colors=colors, autopct='%1.1f%%', startangle=90)
        ax1.axis('equal')
        st.pyplot(fig1)


    # st.write("workday:", workday_count)
    # st.write(st.session_state['current_rate_type'])
    # st.write(st.session_state['penalty_rate'])
    # st.write(salary)

def count_workdays(start_date, end_date):
        workdays = 0
        current_date = start_date
        while current_date <= end_date:
            if current_date.weekday() < 5:  
                workdays += 1
            current_date += timedelta(days=1)
        return workdays














# def base_rate(salary, type):
#     contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'],
#                                                                                  case=False, na='ignore')
#     temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()
#
#     classification = st.session_state["classification"]
#     classification = classification[classification['classification'].isin(temp)]
#
#     classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
#     classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
#     classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')
#
#     st.session_state['base_rate_type'] = classification['base_rate_type'].drop_duplicates()
#
#     classification['base_rate_annual'] = classification.apply(
#         lambda row: row['base_rate'] * 40 * 52 if row['base_rate_type'] == 'hourly' else
#         row['base_rate'] * 12 if row['base_rate_type'] == 'monthly' else
#         row['base_rate'] * 5 * 52 if row['base_rate_type'] == 'daily' else
#         row['base_rate'] * 52 if row['base_rate_type'] == 'weekly' else
#         row['base_rate'], axis=1)
#
#     st.session_state['classification_annual_rate'] = classification
#     st.dataframe(st.session_state['classification_annual_rate'])
#
#     # Convert user input to a numeric value
#     user_salary = float(salary) if salary else None
#
#     current_rate_type = type
#     # Calculate the annual salary based on the rate type
#     if user_salary is not None and current_rate_type is not None:
#         if current_rate_type == 'Hourly':
#             user_salary_annual = user_salary * 40 * 52
#         elif current_rate_type == 'Monthly':
#             user_salary_annual = user_salary * 12
#         elif current_rate_type == 'Daily':
#             user_salary_annual = user_salary * 5 * 52
#         elif current_rate_type == 'Weekly':
#             user_salary_annual = user_salary * 52
#         else:
#             # Handle the case where rate type is not recognized
#             user_salary_annual = user_salary
#     else:
#         user_salary_annual = None
#
#     # Group the DataFrame by 'classification' and calculate the mean of 'base_rate_annual'
#     average_annual_rate = classification.groupby('classification')['base_rate_annual'].mean().reset_index()
#
#     # Create a bar chart to show the average base_rate_annual for each classification
#     fig, ax = plt.subplots()
#     ax.bar(average_annual_rate['classification'], average_annual_rate['base_rate_annual'])
#
#     # Add a horizontal line for the user input value
#     if user_salary_annual is not None:
#         ax.axhline(user_salary_annual, color='red', linestyle='--', label='Current Salary')
#
#     # Set labels and legend
#     ax.set_xlabel('Classification')
#     ax.set_ylabel('Base Rate Annual')
#     plt.xticks(rotation=90)
#     ax.legend()
#
#     st.write("Salary (Annual):", user_salary_annual)
#
#     # Display the plot using st.pyplot
#     st.pyplot(fig)
#
# def base_rate_c(salary, type, weekday, holiday):
#     contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'],
#                                                                                  case=False, na='ignore')
#     temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()
#
#     classification = st.session_state["classification"]
#     classification = classification[classification['classification'].isin(temp)]
#
#     classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
#     classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
#     classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')
#
#     st.session_state['base_rate_type'] = classification['base_rate_type'].drop_duplicates()
#
#     classification['base_rate_annual'] = classification.apply(
#         lambda row: row['base_rate'] * 40 * 52 if row['base_rate_type'] == 'hourly' else
#         row['base_rate'] * 12 if row['base_rate_type'] == 'monthly' else
#         row['base_rate'] * 5 * 52 if row['base_rate_type'] == 'daily' else
#         row['base_rate'] * 52 if row['base_rate_type'] == 'weekly' else
#         row['base_rate'], axis=1)
#
#     st.session_state['classification_annual_rate'] = classification
#     st.dataframe(st.session_state['classification_annual_rate'])
#
#     # Convert user input to a numeric value
#     user_salary = float(salary) if salary else None
#
#     current_rate_type = type
#     # Calculate the annual salary based on the rate type
#     if user_salary is not None and current_rate_type is not None:
#         if current_rate_type == 'Hourly':
#             user_salary_annual = user_salary * weekday + user_salary * holiday * 2.5
#         elif current_rate_type == 'Daily':
#             user_salary_annual = user_salary * weekday + user_salary * holiday * 2.5
#         else:
#             # Handle the case where rate type is not recognized
#             user_salary_annual = user_salary
#     else:
#         user_salary_annual = None
#
#     # Group the DataFrame by 'classification' and calculate the mean of 'base_rate_annual'
#     average_annual_rate = classification.groupby('classification')['base_rate_annual'].mean().reset_index()
#
#     # Create a bar chart to show the average base_rate_annual for each classification
#     fig, ax = plt.subplots()
#     ax.bar(average_annual_rate['classification'], average_annual_rate['base_rate_annual'])
#
#     # Add a horizontal line for the user input value
#     if user_salary_annual is not None:
#         ax.axhline(user_salary_annual, color='red', linestyle='--', label='Current Salary')
#
#     # Set labels and legend
#     ax.set_xlabel('Classification')
#     ax.set_ylabel('Base Rate Annual')
#     plt.xticks(rotation=90)
#     ax.legend()
#
#     # Display the plot using st.pyplot
#     st.pyplot(fig)
#
# def base_rate_p(salary, type, weekday, holiday):
#     contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'],
#                                                                                  case=False, na='ignore')
#     temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()
#
#     classification = st.session_state["classification"]
#     classification = classification[classification['classification'].isin(temp)]
#
#     classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
#     classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
#     classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')
#
#     st.session_state['base_rate_type'] = classification['base_rate_type'].drop_duplicates()
#
#     classification['base_rate_annual'] = classification.apply(
#         lambda row: row['base_rate'] * 40 * 52 if row['base_rate_type'] == 'hourly' else
#         row['base_rate'] * 12 if row['base_rate_type'] == 'monthly' else
#         row['base_rate'] * 5 * 52 if row['base_rate_type'] == 'daily' else
#         row['base_rate'] * 52 if row['base_rate_type'] == 'weekly' else
#         row['base_rate'], axis=1)
#
#     st.session_state['classification_annual_rate'] = classification
#     st.dataframe(st.session_state['classification_annual_rate'])
#
#     # Convert user input to a numeric value
#     user_salary = float(salary) if salary else None
#
#     current_rate_type = type
#     # Calculate the annual salary based on the rate type
#     if user_salary is not None and current_rate_type is not None:
#         if current_rate_type == 'Hourly':
#             user_salary_annual = user_salary * weekday + user_salary * holiday * 2.25
#         elif current_rate_type == 'Daily':
#             user_salary_annual = user_salary * weekday + user_salary * holiday * 2.25
#         elif current_rate_type == 'Monthly':
#             user_salary_annual = user_salary * 12
#         elif current_rate_type == 'Weekly':
#             user_salary_annual = user_salary * 52
#         else:
#             # Handle the case where rate type is not recognized
#             user_salary_annual = user_salary
#     else:
#         user_salary_annual = None
#
#     # Group the DataFrame by 'classification' and calculate the mean of 'base_rate_annual'
#     average_annual_rate = classification.groupby('classification')['base_rate_annual'].mean().reset_index()
#
#     # Create a bar chart to show the average base_rate_annual for each classification
#     fig, ax = plt.subplots()
#     ax.bar(average_annual_rate['classification'], average_annual_rate['base_rate_annual'])
#
#     # Add a horizontal line for the user input value
#     if user_salary_annual is not None:
#         ax.axhline(user_salary_annual, color='red', linestyle='--', label='Current Salary')
#
#     # Set labels and legend
#     ax.set_xlabel('Classification')
#     ax.set_ylabel('Base Rate Annual')
#     plt.xticks(rotation=90)
#     ax.legend()
#
#     # Display the plot using st.pyplot
#     st.pyplot(fig)