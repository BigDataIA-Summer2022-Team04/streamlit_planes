import streamlit as st
import datetime
import requests
import os
import json
from main_page import MultiApp
from pages import home, maps, states, data, abhi, aircrafts, typeaircrafts, typeengines # import your app modules here

st.set_page_config(page_title="Spy Plane Dashboard", page_icon="✈️", layout="wide", initial_sidebar_state="collapsed")

if 'if_logged' not in st.session_state:
    st.session_state['if_logged'] = False
    st.session_state['access_token'] = ''

logout_button = st.button(label = 'Logout', disabled=False)

if logout_button:
    st.session_state['if_logged'] = False
    


if st.session_state['if_logged'] == False:
    # logout_button = st.button(label = 'Logout', disabled=True)
    with st.form(key = 'login', clear_on_submit=True):
        st.subheader("Login")
        username = st.text_input('Your Email ✉️')
        password = st.text_input("Your Password", type="password")
        submit = st.form_submit_button("Submit")
        if submit:
            url = "https://api.anandpiyush.com/login"
            payload={'username': username, 'password': password}
            response = requests.request("POST", url, data=payload)
            if response.status_code == 200:
                json_data = json.loads(response.text)
                # st.text(json_data["access_token"])
                st.session_state['access_token'] = json_data["access_token"]
                st.session_state['if_logged'] = True
                st.text("Login Successful")
                # logout_button.enabled = True
            else:
                st.text("Invalid Credentials ⚠️")
# else :
if st.session_state['if_logged'] == True:
    app = MultiApp()
    st.markdown("""
    # Spy Plane & FAA Registration Dashboard
    Welcome to the Interactive Dashboard
    """)

    # Add all your application here
    app.add_app("Home", home.app)
    app.add_app("State Wise", states.app)
    app.add_app("Maps", maps.app)
    app.add_app("Data", data.app)
    app.add_app("Spy or Not Spy", abhi.app)
    app.add_app("Aircrafts in General", aircrafts.app)
    app.add_app("Find Aircrafts", typeaircrafts.app)
    app.add_app("Explore Engine", typeengines.app)
    # The main app
    app.run()

