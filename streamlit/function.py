import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def input():
    st.title("input")
    user_input = st.text_input("your text", "")
    st.write("What's your input:", user_input)
    st.session_state['input'] = user_input

def select_class():
    contains_doctor = st.session_state['classification']['classification'].str.contains(st.session_state['input'], case=False, na='ignore')
    temp = st.session_state['classification'][contains_doctor]['classification'].drop_duplicates()
    with st.form('sub_class'):
        selected_values = st.multiselect("what classification do you fall under", temp)
        submit = st.form_submit_button(label='class_submit')
        if submit:
            st.session_state['current_class'] = []
            st.session_state['current_class'].extend(selected_values)
            st.write('you have submitted ', st.session_state['current_class'])




def select_rate_type():
    base_rate_type = {"Annual", "Monthly", "Weekly", "Daily", "Hourly"}

    with st.form('base_rate'):
        current_rate_type = st.selectbox('What type of base rate', options=sorted(base_rate_type), key='base_rate')
        submitted = st.form_submit_button(label='Submit')

        if submitted:
            st.write('You have submitted ', current_rate_type)

    user_salary = st.text_input("What is your salary", "")
    st.write("Salary:", user_salary, "(", current_rate_type, ")")

    # Store the user's salary in session state
    st.session_state['user_salary'] = user_salary
    st.session_state['current_rate_type'] = current_rate_type
    # st.dataframe(st.session_state['classification_annual_rate'])

def base_rate():
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
    user_salary = float(st.session_state["user_salary"]) if st.session_state["user_salary"] else None

    current_rate_type = st.session_state.get('current_rate_type', None)
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

    # Display the plot using st.pyplot
    st.pyplot(fig)




    # # Group the DataFrame by 'classification' and calculate the mean of 'base_rate_annual'
    # average_annual_rate = classification.groupby('classification')['base_rate_annual'].mean().reset_index()
    #
    # # Create a bar chart to show the average base_rate_annual for each classification
    # st.bar_chart(average_annual_rate, x="classification", y="base_rate_annual")