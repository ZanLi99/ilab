import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def base_rate(salary, type):
    contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'],
                                                                                 case=False, na='ignore')
    temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()

    classification = st.session_state["classification"]
    classification = classification[classification['classification'].isin(temp)]

    classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
    classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
    classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')

    st.session_state['base_rate_type'] = classification['base_rate_type'].drop_duplicates()

    classification['base_rate_annual'] = classification.apply(
        lambda row: row['base_rate'] * 40 * 52 if row['base_rate_type'] == 'hourly' else
        row['base_rate'] * 12 if row['base_rate_type'] == 'monthly' else
        row['base_rate'] * 5 * 52 if row['base_rate_type'] == 'daily' else
        row['base_rate'] * 52 if row['base_rate_type'] == 'weekly' else
        row['base_rate'], axis=1)

    st.session_state['classification_annual_rate'] = classification
    st.dataframe(st.session_state['classification_annual_rate'])

    # Convert user input to a numeric value
    user_salary = float(salary) if salary else None

    current_rate_type = type
    # Calculate the annual salary based on the rate type
    if user_salary is not None and current_rate_type is not None:
        if current_rate_type == 'Hourly':
            user_salary_annual = user_salary * 40 * 52
        elif current_rate_type == 'Monthly':
            user_salary_annual = user_salary * 12
        elif current_rate_type == 'Daily':
            user_salary_annual = user_salary * 5 * 52
        elif current_rate_type == 'Weekly':
            user_salary_annual = user_salary * 52
        else:
            # Handle the case where rate type is not recognized
            user_salary_annual = user_salary
    else:
        user_salary_annual = None

    # Group the DataFrame by 'classification' and calculate the mean of 'base_rate_annual'
    average_annual_rate = classification.groupby('classification')['base_rate_annual'].mean().reset_index()

    # Create a bar chart to show the average base_rate_annual for each classification
    fig, ax = plt.subplots()
    ax.bar(average_annual_rate['classification'], average_annual_rate['base_rate_annual'])

    # Add a horizontal line for the user input value
    if user_salary_annual is not None:
        ax.axhline(user_salary_annual, color='red', linestyle='--', label='Current Salary')

    # Set labels and legend
    ax.set_xlabel('Classification')
    ax.set_ylabel('Base Rate Annual')
    plt.xticks(rotation=90)
    ax.legend()

    st.write("Salary (Annual):", user_salary_annual)

    # Display the plot using st.pyplot
    st.pyplot(fig)

def base_rate_c(salary, type, weekday, holiday):
    contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'],
                                                                                 case=False, na='ignore')
    temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()

    classification = st.session_state["classification"]
    classification = classification[classification['classification'].isin(temp)]

    classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
    classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
    classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')

    st.session_state['base_rate_type'] = classification['base_rate_type'].drop_duplicates()

    classification['base_rate_annual'] = classification.apply(
        lambda row: row['base_rate'] * 40 * 52 if row['base_rate_type'] == 'hourly' else
        row['base_rate'] * 12 if row['base_rate_type'] == 'monthly' else
        row['base_rate'] * 5 * 52 if row['base_rate_type'] == 'daily' else
        row['base_rate'] * 52 if row['base_rate_type'] == 'weekly' else
        row['base_rate'], axis=1)

    st.session_state['classification_annual_rate'] = classification
    st.dataframe(st.session_state['classification_annual_rate'])

    # Convert user input to a numeric value
    user_salary = float(salary) if salary else None
    weekday = float(weekday) if weekday else None
    holiday = float(holiday) if holiday else None

    current_rate_type = type
    # Calculate the annual salary based on the rate type
    if user_salary is not None and current_rate_type is not None:
        if current_rate_type == 'Hourly':
            user_salary_annual = user_salary * weekday + user_salary * holiday * 2.5
        elif current_rate_type == 'Daily':
            user_salary_annual = user_salary * weekday + user_salary * holiday * 2.5
        else:
            # Handle the case where rate type is not recognized
            user_salary_annual = user_salary
    else:
        user_salary_annual = None

    # Group the DataFrame by 'classification' and calculate the mean of 'base_rate_annual'
    average_annual_rate = classification.groupby('classification')['base_rate_annual'].mean().reset_index()

    # Create a bar chart to show the average base_rate_annual for each classification
    fig, ax = plt.subplots()
    ax.bar(average_annual_rate['classification'], average_annual_rate['base_rate_annual'])

    # Add a horizontal line for the user input value
    if user_salary_annual is not None:
        ax.axhline(user_salary_annual, color='red', linestyle='--', label='Current Salary')

    # Set labels and legend
    ax.set_xlabel('Classification')
    ax.set_ylabel('Base Rate Annual')
    plt.xticks(rotation=90)
    ax.legend()

    st.write("Salary (Annual):", user_salary_annual)

    # Display the plot using st.pyplot
    st.pyplot(fig)

def base_rate_p(salary, type, weekday, holiday):
    contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'],
                                                                                 case=False, na='ignore')
    temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()

    classification = st.session_state["classification"]
    classification = classification[classification['classification'].isin(temp)]

    classification.dropna(subset=["base_rate_type", "base_rate"], inplace=True)
    classification = classification[~classification['base_rate_type'].isin(['nan', 'engagement rate', 'piece rate'])]
    classification['base_rate_type'] = classification['base_rate_type'].replace('ordinary hourly', 'hourly')

    st.session_state['base_rate_type'] = classification['base_rate_type'].drop_duplicates()

    classification['base_rate_annual'] = classification.apply(
        lambda row: row['base_rate'] * 40 * 52 if row['base_rate_type'] == 'hourly' else
        row['base_rate'] * 12 if row['base_rate_type'] == 'monthly' else
        row['base_rate'] * 5 * 52 if row['base_rate_type'] == 'daily' else
        row['base_rate'] * 52 if row['base_rate_type'] == 'weekly' else
        row['base_rate'], axis=1)

    st.session_state['classification_annual_rate'] = classification
    st.dataframe(st.session_state['classification_annual_rate'])

    # Convert user input to a numeric value
    user_salary = float(salary) if salary else None
    weekday = float(weekday) if weekday else None
    holiday = float(holiday) if holiday else None

    current_rate_type = type
    # Calculate the annual salary based on the rate type
    if user_salary is not None and current_rate_type is not None:
        if current_rate_type == 'Hourly':
            user_salary_annual = user_salary * weekday + user_salary * holiday * 2.25
        elif current_rate_type == 'Daily':
            user_salary_annual = user_salary * weekday + user_salary * holiday * 2.25
        elif current_rate_type == 'Monthly':
            user_salary_annual = user_salary * 12
        elif current_rate_type == 'Weekly':
            user_salary_annual = user_salary * 52
        else:
            # Handle the case where rate type is not recognized
            user_salary_annual = user_salary
    else:
        user_salary_annual = None

    # Group the DataFrame by 'classification' and calculate the mean of 'base_rate_annual'
    average_annual_rate = classification.groupby('classification')['base_rate_annual'].mean().reset_index()

    # Create a bar chart to show the average base_rate_annual for each classification
    fig, ax = plt.subplots()
    ax.bar(average_annual_rate['classification'], average_annual_rate['base_rate_annual'])

    # Add a horizontal line for the user input value
    if user_salary_annual is not None:
        ax.axhline(user_salary_annual, color='red', linestyle='--', label='Current Salary')

    # Set labels and legend
    ax.set_xlabel('Classification')
    ax.set_ylabel('Base Rate Annual')
    plt.xticks(rotation=90)
    ax.legend()

    st.write("Salary (Annual):", user_salary_annual)

    # Display the plot using st.pyplot
    st.pyplot(fig)