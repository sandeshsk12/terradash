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
st.markdown('# Wallets')
st.sidebar.success("Do not collapse the sidebar")
# st.sidebar.success("select a page above")


with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)





# Row A

# st.image(Image.open('luna.jpeg'),width=50)
a1, a2, a3 = st.columns(3)



active_wallets = "https://node-api.flipsidecrypto.com/api/v2/queries/d1bdd659-c149-4d01-9c17-3b935dcf7792/data/latest"
active_wallets = pd.read_json(active_wallets).sort_values(by='DATE',ascending=False)
a1.metric('Number of users (This week) ',active_wallets.iloc[0,2])
a2.metric('Number of Active users (This week)',active_wallets.iloc[0,1])


new_users = "https://node-api.flipsidecrypto.com/api/v2/queries/a8409feb-4c91-44b5-ae9c-f011eab30012/data/latest"
new_users = pd.read_json(new_users).sort_values(by='DATE',ascending=False)
a3.metric("Number of New Wallets", new_users.iloc[0,1]
        
)


st.markdown('## Users')
stats='https://node-api.flipsidecrypto.com/api/v2/queries/386e354e-562e-435d-8751-567563957301/data/latest'
stats=pd.read_json(stats).sort_values(by='DATE',ascending=True)
NUMBER_OF_UNIQUE_WALLETS_fig = px.area(
    stats,
    x='DATE',
    y='NUMBER_OF_UNIQUE_WALLETS',
    title='Number of users',
    labels={'DATE':'Date','NUMBER_OF_UNIQUE_WALLETS':'Number of users'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)
NUMBER_OF_UNIQUE_WALLETS_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
NUMBER_OF_UNIQUE_WALLETS_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(NUMBER_OF_UNIQUE_WALLETS_fig)

st.markdown('## Active vs all users')
active_v_all='https://node-api.flipsidecrypto.com/api/v2/queries/d1bdd659-c149-4d01-9c17-3b935dcf7792/data/latest'
active_v_all=pd.read_json(active_v_all).sort_values(by='DATE',ascending=True)
active_v_all_fig = px.bar(
    active_v_all,
    x='DATE',
    y=['ACTIVE_USERS','ALL_USERS'],
    title='Number of users',
    labels={'DATE':'Date','ACTIVE_USERS':'Number of users'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)
active_v_all_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
active_v_all_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(active_v_all_fig)

st.markdown('## New vs existing users')
new_vs_existing='https://node-api.flipsidecrypto.com/api/v2/queries/a8409feb-4c91-44b5-ae9c-f011eab30012/data/latest'
new_vs_existing=pd.read_json(new_vs_existing).sort_values(by='DATE',ascending=True)
new_vs_existing_fig = px.bar(
    new_vs_existing,
    x='DATE',
    y=['EXISTING_USERS','NEW_USERS_COUNT'],
    title='Number of users',
    labels={'DATE':'Date','EXISTING_USERS':'Number of users'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)
new_vs_existing_fig.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
new_vs_existing_fig.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(new_vs_existing_fig)

st.markdown('## Wallets age')
age_of_wallets='https://node-api.flipsidecrypto.com/api/v2/queries/3f8c6385-7f5e-4ce0-a265-d0a983859443/data/latest'
age_of_wallets=pd.read_json(age_of_wallets)
age_of_wallets = px.pie(
    age_of_wallets,
    values='CNT',
    names='AGE',
    title='Distribution of wallets age',
    # labels={'DATE':'Date','EXISTING_USERS':'Number of users'},
    color_discrete_sequence=px.colors.qualitative.Vivid,
    width=1368)
age_of_wallets.update_layout({'plot_bgcolor': 'rgba(0, 0, 0, 0)','paper_bgcolor': 'rgba(215,215,215,255)',})
age_of_wallets.update_layout(xaxis=dict(showgrid=False),yaxis=dict(showgrid=False))
st.write(age_of_wallets)


st.markdown(
    """
    # Resources 

    1. Number of users : https://app.flipsidecrypto.com/velocity/queries/386e354e-562e-435d-8751-567563957301

    2. Number of new users : https://app.flipsidecrypto.com/velocity/queries/54e00538-842d-407b-b5ce-f8519e0d03bd

    3. Active users : https://app.flipsidecrypto.com/velocity/queries/d1bdd659-c149-4d01-9c17-3b935dcf7792

    4. New vs existing users : https://app.flipsidecrypto.com/velocity/queries/a8409feb-4c91-44b5-ae9c-f011eab30012

    5. Wallet age : https://app.flipsidecrypto.com/velocity/queries/3f8c6385-7f5e-4ce0-a265-d0a983859443
    """
)