# Create a new DataFrame to save the dataset
import pandas as pd
import numpy as np
from API import get_awards,get_data
import json
import os

# allowance: wage-allowances
# classification: classifications
# penalty: penalties
# ex_allowance: expense-allowances

# Because every table has different rows, I need to know the shape of the table.
# And then I can use for to get the data.
# Due to the limitation, I only can get 100 data of every page.
def awards():
    counts = json.loads(get_awards(1,1))["_meta"]["result_count"]
    temp = []
    for i in range(1,(counts//100)+2):
        json_string = get_awards(i,100).decode('utf-8')
        data = json.loads(json_string)
        results = data.get('results', [])
        for result in results:
            temp.append(result)
    temp = pd.DataFrame(temp)
    temp.to_csv('./streamlit/awards.csv', index=False)
    return temp


# read awardid from awards.csv, if there is no awards.csv, creating it.
def classification():
    csv_file_path = "./streamlit/awards.csv"
    flag = False
    if os.path.exists(csv_file_path):   
        df = pd.read_csv(csv_file_path)  
        if "award_fixed_id" in df.columns:
            flag = True
    if flag == False:
        awards()

    if flag == True:
        temp = []
        for i in df['award_fixed_id']:
            counts = json.loads(get_data(i,'classifications',1,1))["_meta"]["result_count"]
            for j in range(1,(counts//100+2)):          
                json_string = get_data(i,'classifications',j,100).decode('utf-8')
                data = json.loads(json_string)
                results = data.get('results', [])
                for result in results:
                    temp.append(result)
    temp = pd.DataFrame(temp)
    temp.to_csv('./streamlit/classification.csv', index=False)
    return temp

def penalty():
    csv_file_path = "./streamlit/awards.csv"
    flag = False
    if os.path.exists(csv_file_path):   
        df = pd.read_csv(csv_file_path)  
        if "award_fixed_id" in df.columns:
            flag = True
    if flag == False:
        awards()

    if flag == True:
        temp = []
        for i in df['award_fixed_id']:
            counts = json.loads(get_data(i,'penalties',1,1))["_meta"]["result_count"]
            for j in range(1,(counts//100+2)):          
                json_string = get_data(i,'penalties',j,100).decode('utf-8')
                data = json.loads(json_string)
                results = data.get('results', [])
                for result in results:
                    temp.append(result)
    temp = pd.DataFrame(temp)
    temp.to_csv('./streamlit/penalty.csv', index=False)
    return temp

def ex_allowance():
    csv_file_path = "./streamlit/awards.csv"
    flag = False
    if os.path.exists(csv_file_path):   
        df = pd.read_csv(csv_file_path)  
        if "award_fixed_id" in df.columns:
            flag = True
    if flag == False:
        awards()

    if flag == True:
        temp = []
        for i in df['award_fixed_id']:
            counts = json.loads(get_data(i,'expense-allowances',1,1))["_meta"]["result_count"]
            for j in range(1,(counts//100+2)):          
                json_string = get_data(i,'expense-allowances',j,100).decode('utf-8')
                data = json.loads(json_string)
                results = data.get('results', [])
                for result in results:
                    temp.append(result)
    temp = pd.DataFrame(temp)
    temp.to_csv('./streamlit/expense-allowance.csv', index=False)
    return temp

def allowance():
    csv_file_path = "./streamlit/awards.csv"
    flag = False
    if os.path.exists(csv_file_path):   
        df = pd.read_csv(csv_file_path)  
        if "award_fixed_id" in df.columns:
            flag = True
    if flag == False:
        awards()

    if flag == True:
        temp = []
        for i in df['award_fixed_id']:
            counts = json.loads(get_data(i,'wage-allowances',1,1))["_meta"]["result_count"]
            for j in range(1,(counts//100+2)):          
                json_string = get_data(i,'wage-allowances',j,100).decode('utf-8')
                data = json.loads(json_string)
                results = data.get('results', [])
                for result in results:
                    temp.append(result)
    temp = pd.DataFrame(temp)
    temp.to_csv('./streamlit/allowance.csv', index=False)
    return temp


# awards()
# classification()
# penalty()
# ex_allowance()
# allowance()


 

