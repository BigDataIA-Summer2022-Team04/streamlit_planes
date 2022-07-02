import streamlit as st
import numpy as np
import pandas as pd
import requests
import json
import matplotlib.pyplot as plt
from io import BytesIO

def app():
    st.header('Get Registration, Aircraft and Engine State Wise')
    st.subheader('Please select a State from the list')
    selected_state = st.selectbox("USA State Code", ('TX', 'CA', 'FL', 'DE', 'WA', 'AK', 'IL', 'GA', 'OH', 'AZ', 'MI', 'OR', 'NY', 'UT', 'CO', 'MN', 'NC', \
        'PA', 'WI', 'OK', 'TN', 'KS', 'MO', 'VA', 'IN', 'AL', 'NV', 'MT', 'LA', 'ID', 'IA', 'AR', 'MA', 'NJ', 'NM', 'SC', \
        'MS', 'MD', 'NE', 'KY', 'ND', 'CT', 'SD', 'WY', 'NH', 'ME', 'WV', 'HI', 'VT', 'RI', 'DC', 'AP', 'AE', 'AA'), index=0)
    
    go_btn = st.button(label = 'Go', disabled=False)
    with st.spinner('Generating ...'):
        if go_btn:
            st.subheader('Top Aircraft Registration Type')
            url = f"https://api.anandpiyush.com/data/registrant?user_list={selected_state}&if_records=false"
            headers = {}
            headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                df = pd.read_json(response.text)
                df.iloc[5,0] = 'N-C Corp.'
                fig = plt.figure(figsize=(6, 8))
                plt.bar( df['TYPE_REGISTRANT'], df['count'])
                plt.xticks(rotation = 90)
                plt.title(f"Count of Flight Registration for {selected_state} state ")
                buf = BytesIO()
                fig.savefig(buf, format="png")
                st.image(buf)
            else:
                st.write("API Service Unavailable for Registration")
            
            st.subheader('Top Aircraft Type')
            url = f"https://api.anandpiyush.com/data/aircraft?user_list={selected_state}&if_records=false"
            headers = {}
            headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                df = pd.read_json(response.text)
                fig = plt.figure(figsize=(6, 8))
                df = df[df['count'] >= 100]
                plt.bar( df['TYPE_AIRCRAFT'], df['count'])
                # plt.xticks(rotation = 90)
                # plt.title(f"Count of Flight Registration for state")

                # df.iloc[5,0] = 'N-C Corp.'
                # fig = plt.figure(figsize=(6, 8))
                # plt.bar( df['TYPE_REGISTRANT'], df['count'])
                plt.xticks(rotation = 90)
                plt.title(f"Count of Aircraft type for {selected_state} state ")
                buf = BytesIO()
                fig.savefig(buf, format="png")
                st.image(buf)
            else:
                st.write("API Service Unavailable for Aircraft")
            
            st.subheader('Top Engine Type')
            url = f"https://api.anandpiyush.com/data/engine?user_list={selected_state}&if_records=false"
            headers = {}
            headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
            response = requests.request("GET", url, headers=headers)
            if response.status_code == 200:
                df = pd.read_json(response.text)
                fig = plt.figure(figsize=(6, 8))
                df = df[df['count'] >= 100]
                plt.bar( df['TYPE_ENGINE'], df['count'])
                plt.xticks(rotation = 90)
                plt.title(f"Count of Engine type for {selected_state} state ")
                buf = BytesIO()
                fig.savefig(buf, format="png")
                st.image(buf)
            else:
                st.write("API Service Unavailable For Engine")
    st.success('Done!')


