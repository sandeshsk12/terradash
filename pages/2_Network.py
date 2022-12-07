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
st.markdown('# Transactions')
st.sidebar.success("Do not collapse the sidebar")
# st.sidebar.success("select a page above")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)





# Row A

st.image(Image.open('luna.jpeg'),width=50)
a1, a2, a3 = st.columns(3)



number_of_wallets = "https://node-api.flipsidecrypto.com/api/v2/queries/012648ae-a89d-4504-93eb-68faf37fb394/data/latest"
number_of_wallets = pd.read_json(number_of_wallets)
a1.metric("Number of Transactions", number_of_wallets['NUMBER_OF_TRANSACTIONS'])
a2.metric("Number of blocks", number_of_wallets['NUMBER_OF_BLOCKS'])
a3.metric("Total Fees (uluna)", (number_of_wallets['TOTAL_FEES']))


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



st.markdown('## Average transaction fee per transaction')
average_transaction_fee_per_treansaction_weekly_fig = px.area(
    stats,
    x='DATE',
    y='AVG_FEE_PER_TRANSACTION_PER_DAY',
    title='average transaction fee per treansaction weekly fig',
    labels={'DATE':'Date','AVG_FEE_PER_TRANSACTION_PER_DAY':'transaction fees per transaction'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

average_transaction_fee_per_treansaction_weekly_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
average_transaction_fee_per_treansaction_weekly_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(average_transaction_fee_per_treansaction_weekly_fig)


st.markdown('## Transaction fee per week')
total_transaction_fee_per_week_fig = px.area(
    stats,
    x='DATE',
    y='TOTAL_FEE_PER_DAY',
    title='Total transaction fee weekly',
    labels={'DATE':'Date','TOTAL_FEE_PER_DAY':'transaction fees'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

total_transaction_fee_per_week_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
total_transaction_fee_per_week_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(total_transaction_fee_per_week_fig)







