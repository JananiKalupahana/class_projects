import streamlit as st
import numpy as np
import pandas as pd

st.set_page_config(page_title="Demo_Predict delay", 
                   page_icon="")

st.markdown("# Predict flight delay for your flight")

st.write(
    """Enter your flight data and use the predict button to get prediction"""
)

#function to load model
def load_model():
    model = "D:/Classes/term2/class_projects/models/RandomForest.pk1"
    return model

#function to get airport list based on departing country
def get_airport_list_by_country(country):
    #get a list based on country
    codes = ['DEL', '', '']
    return codes

#function to match delay
def get_all_features_using_user_input(user_input):
    #code to match input
    #features = find matching feature_row 
    return None

#function to predict delay
def predict(data, model):
    delay =  model.predcit(data)
    return delay

arrival_airport_list = get_airport_list_by_country('india')

col1, col2= st.columns(2)
with col1:
    departing_country = st.selectbox('departure_country', ['ABC', 'CDE', 'EFG'])
    depart_airport_list = get_airport_list_by_country(departing_country)
    flight_number = st.text_input('flight number')
col3, col4 = st.columns(2)
with col3:
    depart = st.selectbox('departing airport', depart_airport_list)
    dep_date = st.date_input("Departing date")
with col4:
    arrival = st.selectbox('arrival airport', arrival_airport_list)
    dep_time = st.time_input("Departing time")

if st.button('Predcit Delay'):
    # model = load_model()
    # user_input = [departing_country, flight_number, depart, arrival, dep_date, dep_time]
    # row = get_all_features_using_user_input(user_input)
    # value = predict(row)
    st.text(f"Predicted Delay:")
