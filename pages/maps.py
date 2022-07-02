import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
import io

from PIL import Image

def app():
    st.header('Histogram Registration Count')
    st.subheader('Please select a State from the list')
    selected_state = st.selectbox("USA State Code", ('ALL', 'TX', 'CA', 'FL', 'DE', 'WA', 'AK', 'IL', 'GA', 'OH', 'AZ', 'MI', 'OR', 'NY', 'UT', 'CO', 'MN', 'NC', \
        'PA', 'WI', 'OK', 'TN', 'KS', 'MO', 'VA', 'IN', 'AL', 'NV', 'MT', 'LA', 'ID', 'IA', 'AR', 'MA', 'NJ', 'NM', 'SC', \
        'MS', 'MD', 'NE', 'KY', 'ND', 'CT', 'SD', 'WY', 'NH', 'ME', 'WV', 'HI', 'VT', 'RI', 'DC', 'AP', 'AE', 'AA'), index=0)
    values = st.slider('Select year range', 1910, 2017, (1940, 1970))
    start_year = values[0]
    end_year = values[1]
    bucket = st.slider('Buckets', min_value = 2, max_value = 10, step=1)
    go_btn = st.button(label = 'Go', disabled=False)
    with st.spinner('Generating Histogram...'):
        if go_btn:
            st.subheader('Top Aircraft Registration Type')
            url = f"https://api.anandpiyush.com/plot/histogram?states={selected_state}&start_year={start_year}&end_year={end_year}&buckets={bucket}"
            headers = {}
            headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                i = Image.open(io.BytesIO(response.content))
                st.image(i)
            else:
                st.write("API Service Unavailable for Registration")
    st.success('Done!')

    st.header('Geo Map Registration Count')
    st.subheader('Please select a State from the list')
    selected_states = st.selectbox("USA State Code", ('ALL', 'TX', 'CA', 'FL', 'DE', 'WA', 'AK', 'IL', 'GA', 'OH', 'AZ', 'MI', 'OR', 'NY', 'UT', 'CO', 'MN', 'NC', \
        'PA', 'WI', 'OK', 'TN', 'KS', 'MO', 'VA', 'IN', 'AL', 'NV', 'MT', 'LA', 'ID', 'IA', 'AR', 'MA', 'NJ', 'NM', 'SC', \
        'MS', 'MD', 'NE', 'KY', 'ND', 'CT', 'SD', 'WY', 'NH', 'ME', 'WV', 'HI', 'VT', 'RI', 'DC', 'AP', 'AE', 'AA'), key= 'maps_list', index=0)
    values = st.slider('Select year range', 1911, 2017, (1940, 1970), key= 'maps_slider')
    start_year = values[0]
    end_year = values[1]
    go_btn_m = st.button(label = 'Go', key='Go_Map', disabled=False)
    with st.spinner('Generating Map...'):
        if go_btn_m:
            url = f"https://api.anandpiyush.com/plot/map?states={selected_states}&start_year={start_year}&end_year={end_year}"
            headers = {}
            headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                i = Image.open(io.BytesIO(response.content))
                st.image(i)
            else:
                st.write("API Service Unavailable for Map")
    st.success('Done!')

    