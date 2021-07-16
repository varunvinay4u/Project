#!/usr/bin/env python
# coding: utf-8

# In[6]:


import streamlit as st
import pandas as pd
import numpy as np
import pickle
import datetime


# In[8]:


st.write("""
# Weather Prediction
""")

WeatherPred = open('weather.pkl', 'rb')
classifier = pickle.load(WeatherPred)
today = datetime.date.today()


# In[9]:


precip = {0: 'Rain',1: 'Snow'}
options = list(range(len(precip)))
PrecipType = st.selectbox("Select Precipitation type: ", options=list(precip.keys()), format_func=lambda x: precip[x])
date=st.date_input('Date: ', today)
#st.write(date)
date=str(date)
date=date.split('-')
day=int(date.pop(2))
month=int(date.pop(1))
year=int(date.pop(0))
time=st.time_input('Time: ')
time=str(time)
time=time.split(':')
minute=int(time.pop(1))
hour=int(time.pop(0))
Temp = st.number_input("Enter Temperature (C): ",)
AppTemp = st.number_input("Enter Apparent Temperature (C): ",)
Humidity = st.number_input("Enter Humidity: ",)
WindSpeed = st.number_input("Enter WindSpeed (km/h): ",)
WindBear = st.number_input("Enter Wind Bearing (degrees): ",)
Visibility = st.number_input("Enter Visibility (km): ",)
CloudCover = st.number_input("Enter Cloud Cover: ",)
Pressure = st.number_input("Enter Pressure (millibars): ",)


# In[12]:


submit = st.button('Check')


# In[13]:


if submit:
    with st.spinner("Checking.."):
        result = classifier.predict([[PrecipType,Temp,AppTemp,Humidity,WindSpeed,WindBear,Visibility,CloudCover,Pressure,year,month,day,hour,minute]])
        st.write(result)
 


# In[ ]:




