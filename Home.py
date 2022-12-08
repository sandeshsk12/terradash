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
st.markdown('# TerraDash')
st.sidebar.success("select a page above")

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)


st.markdown('## Introduction')
st.markdown(
    """
    ### What is LUNA 2.0?
        As proposed by Kwon, the Terra blockchain underwent a hard fork, with the launch of Terra 2.0 and the old 
        LUNA tokens being renamed as terra classic (LUNC). Kwon’s fork proposal passed with 65.5% majority approval.
        The snapshot for Terra 2.0 provided by Kwon gives an idea of how the chain upgrade would work and states that 
        the new Terra will be created without the algorithmic stablecoin. 
        The Terra Builders Alliance has provided technical details on integration, 
        decentralised applications (dApps) migration, and a guide to rebranding the original Terra chain as ‘Terra Classic’.
        The old token was renamed terra classic (LUNC), and while the original Cosmos chain will continue to operate, 
        the option to mint or burn coins will be disabled. The new blockchain was launched on 28 May 2022.
    """
)
st.markdown(
    """
    ##  Objective?
         Rebuild the great Terradash, a dazzling dashboard full of analytic insights providing an overview of the entire Terra ecosystem
    """
)
st.markdown(
    """
    ## glossary
    1. Users : A distinct wallet address. A single human can hold multiple wallets however, the number of wallets are considered as users
    2. New user : Users who made their first transaction on the given day
    3. Success ratio : What percentage of transactions are successful.
    4. Active users : A wallet is considered active in the given week if he/she makes a transaction on atleast 3 days of the given week. 
    5. Wallet age : The number of months passed since wallet's first transaction
    """
)

st.markdown(
    """
    ## Methodology 
    Data from Flipside's terra.core tables have been used for building this dashboard. As this is a dashboard bounty, the amount of explaination
    given is kept to a minimum. 
    
    ### Sections
    1. Overview
    2. Transactions

        a. Overview of today's transactions

        b. Number of transactions 

        c. Transaction fee per transaction

        d. Transaction fee per week

        e. Transaction fee per block

        f. Average TPS 

        g. Average block time

        h. Transaction success ratio

    3. wallets

        a. Overview of wallets

        b. Users over time 

        c. Active vs All users

        d. New vs Existing users

        e. Wallets age
    """
)
st.markdown(
    """
    # Conclusion

    1. The number of weekly transaction has been consistently hovering around 50k a week

    2. The transaction fee has reduced considerable in the last few weeks, with it now being clost to 0.02 uluna. 

    3. Each block consists of 1 or 2 transactions which implies that terra is not running at full capacity.

    4. 6 secords or 6000 milliseconds is the average block time on terra

    5. Around 90% of the transactions always go through.

    6. Only 5% of the users are active uers while 95% are inactive

    7. In the recent weeks, Terra onboards close to 500 new users every week which makes up about 5% of theusers. 

    8. Around half of the wallets are more than 6 months old. These wre all created when the hard fork occured.
    """
)

st.markdown("""
# Twitter link

https://twitter.com/Sandesh_K_12/status/1600701296381554689?s=20&t=CpYReqiPJAE7K285lK4GLA
"""
)




