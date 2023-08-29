# Create a new DataFrame to save the dataset
import pandas as pd
import numpy as np
from API import get_respone, get_salary
import json

def awards(page,limit):
    json_string = get_respone(page,limit).decode('utf-8')
    data = json.loads(json_string)
    results = data.get('results', [])
    data = []
    for result in results:
        data.append(result)
    data = pd.DataFrame(data)
    return data



def get_data(awardCode,classificationID,page,limit):
    json_string = get_salary(awardCode,classificationID,page,limit).decode('utf-8')
    data = json.loads(json_string)
    results = data.get('results', [])
    data = []
    for result in results:
        data.append(result)
    data = pd.DataFrame(data)
    return data



a = awards(50,60)
print(a.columns)

#json_string = get_salary(1,1,1,10).decode('utf-8')

def salary():
    temp = []
    for j in range(30):
        for i in range(j*500,j*500+500):
            df_['awardFixedID'][i]
            df_['classificationFixedID'][i]
            temp.append(get_data(df_['awardFixedID'][i],df_['classificationFixedID'][i],1,1))
        time.sleep(100)
    time.sleep(100)   
    for i in range(15000,15220):
            df_['awardFixedID'][i]
            df_['classificationFixedID'][i]
            temp.append(get_data(df_['awardFixedID'][i],df_['classificationFixedID'][i],1,1))