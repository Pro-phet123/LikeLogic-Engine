# LikeLogic-Engine

LikeLogic-Engine is a web application that harnesses the power of machine learning to predict the number of likes a company's Facebook post will receive on a daily basis. It empowers you to make data-driven decisions about your social media strategy and maximize engagement with your audience.


## Key Features 

**Interactive Visualizations:** Explore key user interaction metrics with visualizations for likes, unlikes, engagement, and video replays.

**User-Friendly Prediction Interface:** Input a few simple metrics, and the application will instantly predict the expected number of daily likes.

**Linear Regression Model:** The prediction engine leverages a linear regression model trained on a comprehensive dataset of Facebook post interactions.


## Prerequisites
Before running the project, ensure you have the following software installed on your system:
Python 3.9: You can download and install Python 3.9 from the official Python
website (https://www.python.org/downloads/).


## To Setup Locally


**1. Clone this project repository :**


```bash
git clone https://github.com/Pro-phet123/LikeLogic-Engine.git
```

**2. Change into the project directory :**

```bash
Cd social.py/ 
```

**3. Install Project Dependencies :**

```bash
pip install streamlit streamlit-lottie numpy seaborn tensorflow matplotlib pandas keras joblib
```

**4. Run The Web Application :**

```bash
streamlit run social.py 
```


# About The Web Application

## Link To The Web Application (Deployed Using Streamlit):


## Using The Web Application 

**1. Explore Visualizations:** Choose a metric from the dropdown menu to visualize its trends over time.

**2. Provide Input for Prediction:** Enter the following values:

Number of unlikes per day.

Number of video replays per day.

Number of users who engaged with the page per day.

**3. Click Predict:** The application will display the predicted number of daily likes.


## Dataset

The application utilizes a sample of a dataset gotten from Kaggle of Facebook post interactions, it containing 1226 features and 34,328 entries.

## Model

The prediction model is a linear regression model trained on the provided dataset.

## Technology Stack

Python

Streamlit

Lottie

NumPy

Seaborn

TensorFlow

Matplotlib

Pandas

Keras

Joblib


## Some Informations To Note

The ```linear_regression_model.joblib``` file contains the trained machine learning model.

The ```interactions.csv``` file contains the Facebook post interactions dataset.

## Contact

For any questions or feedback, please reach out to [Name: Olalemi Olaoluwakintan, E-mail: olalemiolaoluwakintan@gmail.com].

