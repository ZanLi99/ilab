import pandas as pd

awards = pd.read_csv('./streamlit/awards.csv')


classification = pd.read_csv('./streamlit/classification.csv')

current_award = awards.loc[awards["name"] == 'Black Coal Mining Industry Award 2020']
classification_award = classification.loc[classification['awardID'].isin(current_award['award_id'])]
classification_award = classification_award.loc[classification_award["employeeRateTypeCode"] == 'AD']
classification_award = classification_award.loc[classification_award['parentClassificationName'] == 'Group A']
classification_award = classification_award.loc[classification_award['classification'] == 'Tracer']

