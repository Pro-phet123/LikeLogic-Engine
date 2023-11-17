#LikeLogic-Engine
import streamlit as st
import numpy as np
import seaborn as sns
import tensorflow as tf
import matplotlib.pyplot as plt
import pandas as pd
from keras.models import load_model
import h5py
import os

header = st.container()
dataset = st.container()
visualisations = st.container()
model_training = st.container()

@st.cache_data
def get_data(filename):
    data = pd.read_csv(filename)
    return data

with header:
    st.title('LikeLogic-Engine')
    st.text('In my project, I created a web app that informs (a Prediction) a company\n the amount of likes they will get for their post per day.')

# Set the background image
st.markdown(
    """
    <style>
        body {
            background-image: url('media.jpg');
            background-size: cover;
        }
    </style>
    """,
    unsafe_allow_html=True
)

with dataset:
    st.header("The company's facebook dataset of their user interactions")
    st.text("The company's facebook dataset of their user interactions contains 1226 columns/features and 34,328 entries")
    Users_interactions = get_data('interactions.csv')
    st.write(Users_interactions.head())

with visualisations:
    st.header('visualisation')
    st.subheader("The number of people who liked the company's post per day")
    sns.set(style="whitegrid")
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Daily New Likes', y='Date', data=Users_interactions, palette='viridis')
    plt.title('Number of People Who Liked the Company\'s Post Per Day')
    plt.xlabel('Daily New Likes')
    plt.ylabel('Date')
    st.pyplot()

    # Add other visualizations here...

with model_training:
    st.subheader("**Company's Input For Prediction**")
    st.text("A LinearRegression (LR) algorithm, \nwas used to create the model for prediction.")
    st.text("PROVIDE YOUR TRANSACTION DETAILS FOR PREDICTION.")
    
    # Transaction types mapping
    transaction_types = {
        1: 'CASH_OUT',
        2: 'PAYMENT',
        3: 'CASH_IN',
        4: 'TRANSFER',
        5: 'DEBIT'
    }

    input_feature_1 = st.selectbox('Select transaction type', list(transaction_types.values()))
    input_feature_2 = st.number_input('Enter ', min_value=0.0)
    input_feature_3 = st.number_input('Enter current account balance', min_value=0.0)
    input_feature_4 = st.number_input('Enter account balance after the transaction', min_value=0.0)

    # Convert transaction type to numeric
    transaction_type_numeric = list(transaction_types.keys())[list(transaction_types.values()).index(input_feature_1)]

model_path = 'linear_regression_model.h5'
with h5py.File(model_path, 'r') as model_file:
    model = tf.keras.models.load_model(model_file)

    submit = st.button('Predict')
    if submit:
        prediction = model.predict([[transaction_type_numeric, input_feature_2, input_feature_3, input_feature_4]])
        threshold = 0.39727665
        if prediction[0][0] <= threshold:
            st.write('This transaction is **fraudulent**.')
        else:
            st.write('This transaction is **non-fraudulent**.')
