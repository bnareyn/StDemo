import streamlit as st
import pandas as pd

import plotly.express as px

DATA_URL = 'https://www.kaggle.com/datasets/pantanjali/unemployment-dataset/download?datasetVersionNumber=1'

st.sidebar.header("Employment Data")

@st.cache
def get_data():
    df = pd.read_csv(DATA_URL, encoding = 'latin1')
    return df

data = get_data()
data