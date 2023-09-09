from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import streamlit as st
import pandas as pd
def filter_job():
    
    user_input = st.session_state['input']
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(st.session_state['classification']['classification'].dropna())

    user_vector = vectorizer.transform([user_input])
    similarities = cosine_similarity(user_vector, tfidf_matrix)

    similarity_threshold = 0.5

    similar_jobs_index = [i for i, sim in enumerate(similarities[0]) if sim >= similarity_threshold]

    similar_jobs = st.session_state['classification'].iloc[similar_jobs_index]['classification'].tolist()
    similar_jobs = pd.DataFrame({
        'describe': similar_jobs
    })
    similar_jobs = similar_jobs.drop_duplicates()
    return similar_jobs
