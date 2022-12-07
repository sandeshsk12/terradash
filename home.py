import streamlit as st 
import seaborn as sns
import plotly.express as px
from shroomdk import ShroomDK
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
import time
from plotly.subplots import make_subplots

from urllib.request import urlopen 
import json
import requests
from PIL import  Image
from dash import Dash, dcc




st.set_page_config(page_title="Data Explorer", layout="wide",initial_sidebar_state="expanded")
st.markdown('# Introduction')
st.sidebar.success("select a page above")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)

# st.markdown(
#     """
# <style>
# [data-testid="stMetricValue"] {
#     font-size: 50px;
# }
# </style>
# """,
#     unsafe_allow_html=True,
# )

gas_url='https://fcd.terra.dev/v1/txs/gas_prices'
response=requests.get(gas_url)
data = response.text
data_json=json.loads(data)
data=data_json["uluna"]
st.write(data)

# Row A
st.write(str(st.markdown("Gas")))
a1, a2, a3 = st.columns(3)
a1.image(Image.open('luna.jpeg'))
a2.metric(label="Gas", value=data, delta="-8%")
a3.metric("Humidity", "86%", "4%")


fig = px.line(x=[1,2,3,4],y=[1,2,3,4])
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')

c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    plost.time_hist(
    data=seattle_weather,
    date='date',
    x_unit='week',
    y_unit='day',
    color='temp_max',
    aggregate='median',
    legend=None)
with c2:
    st.markdown('### Bar chart')
    plost.donut_chart(
        data=stocks,
        theta='q2',
        color='company')


# fig.show()
st.write(fig)
seattle_weather = pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date'])
stocks = pd.read_csv('https://raw.githubusercontent.com/dataprofessor/data/master/stocks_toy.csv')
c1, c2 = st.columns((7,3))
with c1:
    st.markdown('### Heatmap')
    fig = px.line(x=[1,2,3,4],y=[1,2,3,4])
    fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(231,242,240,255)',})
    st.write(fig)
with c2:
    st.markdown('### Bar chart')
    fig = px.line(x=[1,2,3,4],y=[1,2,3,4])
    fig.update_layout({'plot_bgcolor': 'rgba(231,242,240,255)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
    st.write(fig)


url = "https://node-api.flipsidecrypto.com/api/v2/queries/8efb6e8a-184b-41e0-af5c-d060ef7ff307/data/latest"
df = pd.read_json(url)
fig = px.line(df,x='HOUR',y='PRICE')
my_button=list(
    [
        dict(args=['y','PRICE'],label='BarPlot',method='restyle'),
        dict(args=['y','P'],label='Scatterplot',method='restyle')
    ]
)
fig.update_layout(
    updatemenus=[dict(type='buttons',buttons=my_button,direction='left',
    pad={'r':0.2,'t':0.1},
    showactive=True,
    xanchor='left',x=0.4,
    yanchor='top',y=0.95)]

)

# fig["layout"].pop("updatemenus")
fig.update_layout({'plot_bgcolor': 'rgba(231,242,240,255)','paper_bgcolor': 'rgba(0, 0, 0, 0)',})
st.write(fig)
st.write(df)
dcc.RadioItems(['New York City', 'Montreal','San Francisco'], 'Montreal')
