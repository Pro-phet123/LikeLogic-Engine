# LikeLogic-Engine 
%%writefile social.py
import json
import requests
import streamlit as st
from streamlit_lottie import st_lottie
import numpy as np
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import load_model
from joblib import dump, load
import h5py
import os
import time



def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
#st.title('OBOT IS A LOUD BOY')# Lottie animation URL
lottie_url = "https://lottie.host/c543af57-8f5a-4777-92f9-dd11e1714ef3/iXyxE3WPrp.json"


# Load Lottie animation
#lottie_json = load_lottie_url(lottie_url)


# Display animation in Streamlit
#if lottie_json is not None:


    # Making the code below run after 6 seconds

   # with st.spinner("# ```LikeLogic-Engine Loading please wait .....🥰```"):

        #st_lottie(lottie_json, speed=6, width=400, height=1000, key="animation")
        #time.sleep(6)

    # Hide the spinner
    #st.spinner()

#else:
    #st.error("Failed to load Lottie animation.")


# Hide the spinner
#st.spinner()

animation1 = st.container()
header = st.container()
dataset = st.container()
animation2 = st.container()
visualisations = st.container()
animation3 = st.container()
model_training = st.container()

@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename)
    return data



def load_lottie_url(url: str):
    r = requests.get(url)
    if r.status_code != 200:
       return None
    return r.json()

with animation1:
        #st.title('OBOT IS A LOUD BOY')# Lottie animation URL
    lottie_url = "https://lottie.host/c543af57-8f5a-4777-92f9-dd11e1714ef3/iXyxE3WPrp.json"


    #Load Lottie animation
    lottie_json = load_lottie_url(lottie_url)


    #Display animation in Streamlit
    if lottie_json is not None:


    #Making the code below run after 6 seconds
        with st.spinner("# ```LikeLogic-Engine Loading please wait .....🥰```"):

            st_lottie(lottie_json, speed=0, width=0, height=00, key="animation1")
            time.sleep(5)

    #Hide the spinner
    st.spinner()

    #else:
       # st.error("Failed to load Lottie animation.")


# Hide the spinner
#st.spinner()

with header:
    st.title('LikeLogic-Engine')
    st.text("LikeLogic-Engine is a web application which\npredicts the Likes ❣ a company's facebook\npost would have daily.")

with dataset:
    st.title("The Dataset")
    st.text("This is a company's facebook post users\ninteraction dataset. It contains 1226\ncolumns/features and 34,328 entries.")
    Users_interactions = get_data("/content/drive/MyDrive/Colab Notebooks/interactions.csv")
    st.write(Users_interactions.head())

with animation2:
    st.title('Visualizations')
    Viz = "https://lottie.host/67a9b0ee-fc84-47e0-b9dc-4eeaa47d4cbc/oG6a51nJui.json"
    lottie_json = load_lottie_url(Viz)
    if lottie_json is not None:
        st_lottie(lottie_json, speed=2, width=0, height=0, key="animation2")

with visualisations:
    # Visualizations dropdown
    st.set_option('deprecation.showPyplotGlobalUse', False)
    #st.title('Visualizations')
    selected_viz = st.selectbox('# Select Visualisation' , ['Likes', 'Unlikes', 'Engagement', 'Video Replays'])

    # Filter data based on user selection
    if selected_viz == 'Likes':
        data_col = 'Daily New Likes'
        title = "Number of People Who Liked the Company's Post Per Day"

    elif selected_viz == 'Unlikes':
        data_col = 'Daily Unlikes'
        title = "Number of People Who Unliked the Company's Post Per Day"

    elif selected_viz == 'Engagement':
        data_col = 'Daily Page Engaged Users'
        title = "Number of People Who Engaged with the Company's Post Per Day"

    elif selected_viz == 'Video Replays':
        data_col = 'Daily Video Repeats'
        title = "Number of People Who Replayed the Company's Post Per Day"

    # Plot selected visualization
    st.subheader(f"{title}")
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x=data_col, y='Date', data=Users_interactions, palette='viridis', hue='Date', legend=False)
    plt.title(title)
    plt.xlabel(data_col)
    plt.ylabel('Date')
    st.pyplot()

with animation3:
    st.title("User's Input")
    st.text("A Linear Regression (LR) algorithm\nwas used to create LikeLogic-Engine's model.")

    User = "https://lottie.host/a94455ff-f844-462b-aa79-ddc5a97f271b/aOluPGaLk7.json"
    lottie_json = load_lottie_url(User)
    if lottie_json is not None:
        st_lottie(lottie_json, speed=2, width=0, height=0, key="animation3")


with model_training:

    st.subheader("PROVIDE THE FOLLOWING DETAILS FOR PREDICTION")

    input_feature_1 = st.number_input('Enter the number of unlikes on a certain post per day:', min_value=0)
    input_feature_2 = st.number_input('Enter the number of times a posted video was replayed per day:', min_value=0)
    input_feature_3 = st.number_input("Enter the number for users who Engaged with the company's Page per day:", min_value=0)

    MAX_VALUE = 10**20  # Replace with your desired maximum value

    if not (0 <= input_feature_1 <= MAX_VALUE and 0 <= input_feature_2 <= MAX_VALUE and 0 <= input_feature_3 <= MAX_VALUE):
        st.warning('Please enter valid numbers for unlikes, video replays, and user engagement.')

loaded_model = load("/content/drive/MyDrive/Colab Notebooks/linear_regression_model.joblib")

submit = st.button('Predict')
if submit:
    # Make sure input features are in the correct format (2D array)
    input_features = [[input_feature_1, input_feature_2, input_feature_3]]

    # Perform prediction
    prediction = loaded_model.predict(input_features)

    # Display the result
    st.subheader("Prediction Result:")
    st.write(f"The predicted number of daily new likes is approximately: {prediction[0]}")

#loaded_model = load("/content/drive/MyDrive/Colab Notebooks/linear_regression_model.joblib")


#submit = st.button('Predict')
#if submit:
    #prediction = loaded_model.predict([[input_feature_1, input_feature_2, input_feature_3]])
    #st.subheader("Prediction Result:")
    #st.write(f"The predicted number of daily new likes is approximately: {prediction[0][0]}")
