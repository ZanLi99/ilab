# Create a new DataFrame to save the dataset
import pandas as pd
import numpy as np
from API import get_awards,get_data,get_holiday, hoilday_country
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
            counts = json.loads(get_data(i,'pay-rates',1,1))["_meta"]["result_count"]
            for j in range(1,(counts//100+2)):          
                json_string = get_data(i,'pay-rates',j,100).decode('utf-8')
                data = json.loads(json_string)
                results = data.get('results', [])
                for dict in results:
                        dict['awards'] = i
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
                for dict in results:
                        dict['awards'] = i
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
                for dict in results:
                        dict['awards'] = i
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
                for dict in results:
                        dict['awards'] = i
                for result in results:
                    temp.append(result)
                    
        temp = pd.DataFrame(temp)
        temp.to_csv('./streamlit/allowance.csv', index=False)
    return temp

# def clauseID():
#     csv_file_path = "./streamlit/awards.csv"
#     flag = False
#     if os.path.exists(csv_file_path):   
#         df = pd.read_csv(csv_file_path)  
#         if "award_fixed_id" in df.columns:
#             flag = True
#     if flag == False:
#         awards()

#     if flag == True:
#         temp = []
#         for i in df['award_fixed_id']:
#             counts = json.loads(get_data(i,'classifications',1,1))["_meta"]["result_count"]
#             for j in range(1,(counts//100+2)):          
#                 json_string = get_data(i,'classifications',j,100).decode('utf-8')
#                 data = json.loads(json_string)
#                 results = data.get('results', [])
#                 for dict in results:
#                         dict['awards'] = i
#                 for result in results:
#                     temp.append(result)
                    
    temp = pd.DataFrame(temp)
    temp.to_csv('./streamlit/clause.csv', index=False)
    return temp

def merge_classification_penalty():
    classification = pd.read_csv('./streamlit/classification.csv')
    penalty = pd.read_csv('./streamlit/penalty.csv')
    
    classification = classification.drop_duplicates()
    penalty = penalty.drop_duplicates()


    A = classification[["classification_fixed_id","base_pay_rate_id","base_rate_type","base_rate","classification"]]
    B = penalty[["clause_description","penalty_description","rate","base_pay_rate_id","penalty_fixed_id","employee_rate_type_code"]]

    A = A.drop_duplicates()
    B = B.drop_duplicates()

    merged_df = A.merge(B, on='base_pay_rate_id', how='inner')
    merged_df.dropna(subset=["base_pay_rate_id"], axis=0, inplace=True)
    merged_df.to_csv('./streamlit/merge_classification_penalty.csv', index=False)

def get_country():
    country = hoilday_country()
    country = pd.DataFrame(country)
    country.to_csv('./streamlit/country.csv', index=False)
    return country

def get_holiday():
    csv_file_path = "./streamlit/country.csv"
    flag = False
    if os.path.exists(csv_file_path):   
        df = pd.read_csv(csv_file_path)  
        if "countryCode" in df.columns:
            flag = True
    if flag == False:
        get_country()
    if flag == True:
        print(df['countryCode'])


get_holiday()

# awards()
# classification()
# penalty()
# ex_allowance()
# allowance()
#clauseID()
# merge_classification_penalty()
# get_country()
 


