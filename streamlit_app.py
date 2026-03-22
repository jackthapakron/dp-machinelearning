import streamlit as st
import pandas as pd

st.title('🎈 Machine learning App')

st.info('This app build a machine learning model!')

df = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/penguins_cleaned.csv')
df
