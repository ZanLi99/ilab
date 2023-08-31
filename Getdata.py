# Create a new DataFrame to save the dataset
import pandas as pd
import numpy as np
from API import get_awards, get_classification
import json
import os

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
    temp.to_csv('./Files/awards.csv')
    return temp


# read awardid from awards.csv, if there is no awards.csv, creating it.
def classification():
    csv_file_path = "./Files/awards.csv"
    flag = False
    if os.path.exists(csv_file_path):   
        df = pd.read_csv(csv_file_path)  
        if "award_fixed_id" in df.columns:
            flag = True
    if flag == False:
        awards()
    flag = True
    if flag == True:
        temp = []
        for i in df['award_fixed_id']:
            counts = json.loads(get_classification(i,1,1))["_meta"]["result_count"]
            for j in range(1,(counts//100+2)):          
                json_string = get_classification(i,j,100).decode('utf-8')
                data = json.loads(json_string)
                results = data.get('results', [])
                for result in results:
                    temp.append(result)
    temp = pd.DataFrame(temp)
    temp.to_csv('./Files/classification.csv')
    return temp

# awards()
# classification()

 


