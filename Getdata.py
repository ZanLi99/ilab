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
        print(result)
    return data


if __name__ == "__main__":
    print(get_data())
