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
a1.metric("Number of Transactions (This week)", number_of_wallets['NUMBER_OF_TRANSACTIONS'])
a2.metric("Number of blocks (This week)", number_of_wallets['NUMBER_OF_BLOCKS'])
a3.metric("Total Fees (uluna) (This week)", (number_of_wallets['TOTAL_FEES']))


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

st.markdown('## Average transaction per block')
average_transactions_per_block = px.area(
    stats,
    x='DATE',
    y='AVG_TXN_PER_BLOCK',
    title='Average transaction per block',
    labels={'DATE':'Date','AVG_TXN_PER_BLOCK':'Number of transactions'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

average_transactions_per_block.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
average_transactions_per_block.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(average_transactions_per_block)

st.markdown('## Average tps per week')
tps='https://node-api.flipsidecrypto.com/api/v2/queries/0dbecbfb-d75e-4c9e-95b0-69ee37d372eb/data/latest'
tps=pd.read_json(tps).sort_values(by='DATE',ascending=True)
average_transactions_per_block = px.bar(
    tps,
    x='DATE',
    y='AVG_TPS',
    title='Average tps per week',
    labels={'DATE':'Date','AVG_TPS':'Number of transactions per second'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

average_transactions_per_block.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
average_transactions_per_block.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(average_transactions_per_block)

st.markdown('## Average block time per week')
abt='https://node-api.flipsidecrypto.com/api/v2/queries/e90c0c6c-6ec3-422b-9c0d-3ed04c4aab85/data/latest'
abt=pd.read_json(abt).sort_values(by='DATE',ascending=True)
average_transactions_per_block = px.bar(
    abt,
    x='DATE',
    y='AVG_BLOCK_TIME_MILLISECONDS',
    title='Average block time per week',
    labels={'DATE':'Date','AVG_BLOCK_TIME_MILLISECONDS':'Block time (ms)'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

average_transactions_per_block.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
average_transactions_per_block.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(average_transactions_per_block)

st.markdown('## Transaction success ratio')
sr='https://node-api.flipsidecrypto.com/api/v2/queries/08d050ee-f687-440c-85c8-8a5bb7279493/data/latest'
sr=pd.read_json(sr).sort_values(by='DATE',ascending=True)
sucess_ratio_fig = px.line(
    sr,
    x='DATE',
    y='S_PERCENTAGE',
    title='Average success ratio (daily)',
    labels={'DATE':'Date','S_PERCENTAGE':'Success rato %'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)

sucess_ratio_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
sucess_ratio_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(sucess_ratio_fig)


st.markdown(
    """
    # Resources : 

    1. Number of transactions : https://app.flipsidecrypto.com/velocity/queries/386e354e-562e-435d-8751-567563957301

    2. Transaction fee per treansaction :https://app.flipsidecrypto.com/velocity/queries/386e354e-562e-435d-8751-567563957301

    3. Transaction fee per week : https://app.flipsidecrypto.com/velocity/queries/386e354e-562e-435d-8751-567563957301

    4. Transaction fee per block : https://app.flipsidecrypto.com/velocity/queries/386e354e-562e-435d-8751-567563957301

    5. Transaction per second : https://app.flipsidecrypto.com/velocity/queries/0dbecbfb-d75e-4c9e-95b0-69ee37d372eb

    6. Block time https://app.flipsidecrypto.com/velocity/queries/e90c0c6c-6ec3-422b-9c0d-3ed04c4aab85

    7. Success ratio : https://app.flipsidecrypto.com/velocity/queries/08d050ee-f687-440c-85c8-8a5bb7279493

    """
)







