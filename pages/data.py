import streamlit as st
import requests
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def app():

    def fetch(session, url):
        try:
            header = {}
            st.write(st.session_state['access_token'])
            token = st.session_state['access_token']
            header['Authorization'] = f"Bearer {token}"
            st.write(header)
            result = session.get(url, headers=header)
            return result.status_code,result.json()
        except Exception:
            return {}

    st.title("Jui's API")
    session = requests.Session()
    #Function1
    st.subheader("**Get_Popular_Engine_Count :hammer_and_wrench::gear::** ")
    st.markdown('This function gives the aggregate details of flights with graph based on the count of engine used in them. From which we can get the data of popular engines used.')
    submitted1 = st.button(label="Search",key=1)
    if submitted1:
        st.write("Response")
        # response_code,data = fetch(session,"https://api.anandpiyush.com/get_popular_engine_count")
        url = "https://api.anandpiyush.com/get_popular_engine_count"
        headers = {}
        headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            da=pd.read_json(response.text)
            fig2=plt.figure()
            sns.barplot(x='NAME', y='COUNT_ENGINE_TYPE', data=da)
            plt.xticks(rotation=90)
            st.pyplot(fig2)
        else:
            st.error("Error")
    
    #Function2
    st.subheader("**Get_Company_Address :round_pushpin::**")	
    st.markdown('This function gives the complete address of the registered company based on the flight ID. Accepts N_Number as input and returns records of flight number, company name, street, street2, city, state, zip code, region, country.')
    N_NUMBER = st.text_input("N_NUMBER", key="index")
    submitted2 = st.button(label="Search",key=2)
    if submitted2:
        st.write("Response")
        url = f"https://api.anandpiyush.com/get_company_address?N_NUMBER={N_NUMBER}"
        headers = {}
        headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            st.json(response.text)
        else:
            st.error("Error")
    
    #Function3
    st.subheader("**Flight_Details_Between_Years :small_airplane::date: :**")	
    st.markdown('This function accepts two date values as an input and return the details of flight for which engine were manufactured between those particular year.')
    start_date = st.text_input("Start Date", key="index1")
    end_date = st.text_input("End Date", key="index2")
    submitted3 = st.button(label="Search",key=3)
    if submitted3:
        url = f"https://api.anandpiyush.com/flight_details_between_years?start_date={start_date}&end_date={end_date}"
        headers = {}
        headers['Authorization'] = f"Bearer {st.session_state['access_token']}"
        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            da=pd.read_json(response.text)
            u=da.groupby(['YEAR_MFR'])['YEAR_MFR'].count().reset_index(name='Count_Of_Flights')
            #u.columns=["Year","Count"]
            u["YEAR_MFR"]=u["YEAR_MFR"].str.slice(0,4)

            fig2=plt.figure()
            sns.barplot(x='YEAR_MFR', y='Count_Of_Flights', data=u)
            plt.xticks(rotation=0)
            st.pyplot(fig2)
        else:
            st.error("Error")
    

