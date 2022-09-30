import streamlit as st
import pandas as pd

import plotly.express as px


st.sidebar.header("Calgary Crime Data")

DATA_URL = "https://data.calgary.ca/api/views/848s-4m4z/rows.csv?accessType=DOWNLOAD"

@st.cache
def get_data():
    df = pd.read_csv(DATA_URL)
    df[['lat', 'lon']] = df['Community Center Point'].str.split( ',', expand=True)
    df[['x', 'lat']] = df.lat.str.split('(', expand = True)
    df[['lon','y']] = df.lon.str.split(')', expand = True)
    df.drop(['ID', 'Community Center Point', 'Date', 'x', 'y'], axis=1, inplace = True)
    df.lat = df.lat.apply(float)
    df.lon = df.lon.apply(float)
    print(df.dtypes)
    return df

data = get_data()

dfCrimeResCount = data[['Year', 'Sector', 'Crime Count', 'Resident Count']].groupby(['Year', 'Sector']).sum().reset_index()
fig = px.line(dfCrimeResCount, x="Resident Count", y="Crime Count", color='Sector', text="Year")
fig.update_traces(textposition="bottom right")
st.plotly_chart(fig, use_container_width=True)

dfCrimeCount = data[['Sector', 'Year', 'Crime Count']].groupby(['Year', 'Sector']).sum().reset_index()

fig = px.bar(dfCrimeCount, x="Year", y="Crime Count", color="Sector", barmode="group")
st.plotly_chart(fig, use_container_width=True)

fig = px.line(dfCrimeCount, x="Year", y="Crime Count", color='Sector')
st.plotly_chart(fig, use_container_width=True)
