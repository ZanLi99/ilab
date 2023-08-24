# Create a new DataFrame to save the dataset
import pandas as pd
import numpy as np
from API import get_respone
import json


def get_data():
    json_string = get_respone().decode('utf-8')
    data = json.loads(json_string)
    results = data.get('results', [])
    data = []
    for result in results:
        data.append(result)
    data = pd.DataFrame(data)
    return data



print(get_data())