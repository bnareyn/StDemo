import streamlit as st
import pandas as pd

import plotly.express as px

DATA_URL = 'data/employ.csv'

st.sidebar.header("Employment Data")

@st.cache
def get_data():
    df = pd.read_csv(DATA_URL, encoding = 'latin1')
    return df

import plotly.graph_objects as go
import pandas as pd

data = get_data()
#data

df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2014_world_gdp_with_codes.csv')
#df
fig = go.Figure(data=go.Choropleth(
    locations = data['Country Code'],
    z = data['2021'],
    text = data['Country Name'],
    colorscale = 'Blues',
    autocolorscale=False,
    reversescale=True,
    marker_line_color='darkgray',
    marker_line_width=0.5,
    colorbar_ticksuffix = '%',
    colorbar_title = 'Unemployment in %',
))

fig.update_layout(
    title_text='World Unemployment Rate',
    geo=dict(
        showframe=False,
        showcoastlines=False,
        projection_type='equirectangular'
    ),
    annotations = [dict(
        x=0.55,
        y=0.1,
        xref='paper',
        yref='paper',
        text='Source: <a href="https://www.kaggle.com/datasets/pantanjali/unemployment-dataset">\
            Kaggle</a>',
        showarrow = False
    )]
)

st.plotly_chart(fig, use_container_width=True)
