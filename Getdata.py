# Create a new DataFrame to save the dataset
import pandas as pd
import numpy as np
from API import get_respone
import json


def get_data(name,page,limit):
    json_string = get_respone(name,page,limit).decode('utf-8')
    data = json.loads(json_string)
    results = data.get('results', [])
    data = []
    for result in results:
        data.append(result)
    data = pd.DataFrame(data)
    return data



#print(get_data('awards',1,60))
print(get_data('awards/MA000009/classifications/311/pay-rates',1,60))
get_data('awards/MA000009/classifications/311/pay-rates',1,60).to_csv('MA000009_311.csv', index=False)