import pandas as pd
import numpy as np


data = pd.read_csv('df_cluster.csv')
songs = data['track_name'].tolist()

import streamlit as st

option = st.selectbox(
     "What's the song you are listening to?",
     songs)

st.write(
    'Here you go:', 
    data[
        (data['track_name'] != option) & \
        (data['k_cluster'] == data[data['track_name'] == option]['k_cluster'].values[0])
    ][['track_name', 'artist_name']]
)