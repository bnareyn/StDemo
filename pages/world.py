import streamlit as st
import plotly.figure_factory as ff

import numpy as np

import plotly.graph_objects as go

fig = go.Figure(go.Scattergeo())
fig.update_layout(height=300, margin={"r":0,"t":0,"l":0,"b":0})

st.plotly_chart(fig, use_container_width=True)

start_time = st.slider(
    "When do you start?",
    min_value = 1990,
    max_value = 2100,
    value= 2010)
st.write("Start time:", start_time)