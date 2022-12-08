import streamlit as st 
import seaborn as sns
import plotly.express as px
from shroomdk import ShroomDK
import pandas as pd
from datetime import datetime as dt
import matplotlib.pyplot as plt
import time
from plotly.subplots import make_subplots
# import plost
from urllib.request import urlopen 
import json
import requests
from PIL import  Image





st.set_page_config(page_title="Data Explorer", layout="wide",initial_sidebar_state="expanded")
st.markdown('# Overview')
st.sidebar.success("Do not collapse the sidebar")
# st.sidebar.success("select a page above")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)





# Row A

# st.image(Image.open('luna.jpeg'),width=80)
a1, a2, a3 = st.columns(3)

price_url = "https://node-api.flipsidecrypto.com/api/v2/queries/8efb6e8a-184b-41e0-af5c-d060ef7ff307/data/latest"
price_df = pd.read_json(price_url)
current_price=(price_df.sort_values(by='HOUR',ascending=False).iloc[1,1])
current_price_diff_percent=(price_df.sort_values(by='HOUR',ascending=False).iloc[1,2])
a1.metric("Price" ,  value='$ ' + str((current_price)), delta=str(current_price_diff_percent)+ ' %')

number_of_wallets = "https://node-api.flipsidecrypto.com/api/v2/queries/012648ae-a89d-4504-93eb-68faf37fb394/data/latest"
number_of_wallets = pd.read_json(number_of_wallets)
a2.metric("Number of users", number_of_wallets['NUMBER_OF_WALLETS'])

gas_url='https://fcd.terra.dev/v1/txs/gas_prices'
response=requests.get(gas_url)
data = response.text
data_json=json.loads(data)
data=data_json["uluna"]
a3.metric("Gas price", str(data) + ' uluna')

st.markdown('## Transactions')
stats='https://node-api.flipsidecrypto.com/api/v2/queries/386e354e-562e-435d-8751-567563957301/data/latest'
stats=pd.read_json(stats).sort_values(by='DATE',ascending=True)
number_of_transactions_fig = px.area(
    stats,
    x='DATE',
    y='NUMBER_OF_TRANSACTIONS',
    title='Number of Transactions',
    labels={'DATE':'Date','NUMBER_OF_TRANSACTIONS':'Number of transactions'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)
number_of_transactions_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
number_of_transactions_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(number_of_transactions_fig)


st.markdown('## Unique wallets')
Number_of_unique_wallets_fig = px.area(
    stats,
    x='DATE',
    y='NUMBER_OF_UNIQUE_WALLETS',
    title='Number of unique wallets',
    labels={'DATE':'Date','NUMBER_OF_UNIQUE_WALLETS':'Number of unique wallets'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

Number_of_unique_wallets_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
Number_of_unique_wallets_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(Number_of_unique_wallets_fig)


st.markdown('## New users')
daily_new_users='https://node-api.flipsidecrypto.com/api/v2/queries/54e00538-842d-407b-b5ce-f8519e0d03bd/data/latest'
daily_new_users=pd.read_json(daily_new_users).sort_values(by='DATE',ascending=True)
daily_new_users_fig = px.area(
    daily_new_users,
    x='DATE',
    y='SENDER',
    title='Number of new wallets',
    labels={'DATE':'Date','SENDER':'Number of new wallets'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

daily_new_users_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
daily_new_users_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(daily_new_users_fig)


st.markdown(
    """
    # Resources : 
    
    1. Luna Price : https://app.flipsidecrypto.com/velocity/queries/8efb6e8a-184b-41e0-af5c-d060ef7ff307

    2. Gas price : https://docs.terra.money/learn/fees

    3. Transactions : https://app.flipsidecrypto.com/velocity/queries/386e354e-562e-435d-8751-567563957301

    4. Unique wallets : https://app.flipsidecrypto.com/velocity/queries/386e354e-562e-435d-8751-567563957301

    5. New users : https://app.flipsidecrypto.com/velocity/queries/54e00538-842d-407b-b5ce-f8519e0d03bd
    """
)






