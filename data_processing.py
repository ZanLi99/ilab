import pandas as pd
import numpy as np


def cleaning():
    classification = pd.read_csv('./streamlit/classification.csv')
    penalty = pd.read_csv('./streamlit/penalty.csv')
    
    classification = classification.drop_duplicates()
    penalty = penalty.drop_duplicates()


    A = classification[["classification_fixed_id","base_pay_rate_id"]]
    B = penalty[["clause_description","penalty_description","rate","base_pay_rate_id","penalty_fixed_id","employee_rate_type_code"]]

def classification_clean():
    classification = pd.read_csv('./streamlit/classification.csv')
    classification['classification'] = classification['classification'].astype(str)
    classification['classification'] = classification['classification'].str.lower()
    classification.dropna(subset=['base_rate','base_pay_rate_id','base_rate_type'], axis=0, inplace=True)

    max_versions = classification.groupby(['classification','employee_rate_type_code'])['version_number'].max().reset_index()
    result = classification.merge(max_versions, on=['classification', 'version_number'])
    result.to_csv('./streamlit/classification.csv')
    return result

#cleaning()
#classification_clean()
