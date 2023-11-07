#########################################################
# Dependencies
#########################################################
from flask import Flask, jsonify
import numpy as np
import pandas as pd
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func, desc
from pathlib import Path
import pickle

# CORS
from flask_cors import CORS

# Ignore warnings
import warnings
warnings.simplefilter(action='ignore')

#########################################################
# Database Setup
#########################################################

# Load data from CSV file into pandas DataFrame
csv = Path('model_openbox_risks.csv')
risk_df = pd.read_csv(csv)

#########################################################
# Functions
#########################################################

# Determine risk
def openbox_get_risk(risk_df, state, age_bracket, mental_illness, employment, arrest, autism):
    # Filter based on state
    filtered_df = risk_df.loc[risk_df['State']==state,:]

    risk_age = filtered_df[age_bracket].values[0]

    # Default values
    risk_mental = 1
    risk_employment = 1
    risk_arrest = 1
    risk_autism = 1

    if mental_illness == '1':
        risk_mental = filtered_df['Mental_Illness_Risk'].values[0]
    elif mental_illness == '0':
        risk_mental = 1

    if employment == '1':
        risk_employment = 1
    elif employment == '0':
        risk_employment = filtered_df['Unemployment_Risk'].values[0]

    if arrest == '1':
        risk_arrest = filtered_df['Arrest_Risk'].values[0]
    elif arrest == '1':
        risk_arrest = 1

    if autism == '1':
        risk_autism = filtered_df['Autism_Risk'].values[0]
    elif autism == '1':
        risk_autism = 1

    return [risk_age, risk_mental, risk_employment, risk_arrest, risk_autism]

#########################################################
# Flask Setup
#########################################################
app = Flask(__name__)
CORS(app)

@app.route("/")
def api_home():
    return "Make America Safe... Again?"

#########################################################
# Flask Dynamic Routes
#########################################################

@app.route("/api/v1.0/openbox/<state>/<age_bracket>/<mental_illness>/<employment>/<arrest>/<autism>")
def api_openbox(state, age_bracket, mental_illness, employment, arrest, autism):

    total_tisk = openbox_get_risk(risk_df, state, age_bracket, mental_illness, employment, arrest, autism)

    return jsonify({'Risk': total_tisk})

@app.route("/api/v1.0/blackbox/<id>/<Age>/<Gender>/<Race>/<Immigrant>/<Education>/<RelStatus>/<Employed>/<Work>/<MilService>/<Arrested>/<ParentDivorce>/<SES>/<MentalIllness>/<MentalIllnessHistory>/<Autism>/<HealthIssues>")
def api_blackbox(id, Age, Gender, Race, Immigrant, Education, RelStatus, Employed, Work, MilService, Arrested, ParentDivorce, SES, MentalIllness, MentalIllnessHistory, Autism, HealthIssues):

    # Create a DataFrame to hold the data
    input_data = pd.DataFrame([{
        'Age': Age,
        'Gender': Gender,
        'Race': Race,
        'Immigrant': Immigrant,
        'Education': Education.replace("+", "/"),
        'RelStatus': RelStatus.replace("+", "/"),
        'Employed': Employed,
        'Work': Work,
        'MilService': MilService,
        'Arrested': Arrested,
        'ParentDivorce': ParentDivorce,
        'SES': SES,
        'MentalIllness': MentalIllness,
        'MentalIllnessHistory': MentalIllnessHistory,
        'Autism': Autism,
        'HealthIssues': HealthIssues
    }])

    # Get dummies
    dummies_df = pd.get_dummies(input_data.drop(columns=['Age']))
    X = pd.concat([input_data['Age'], dummies_df], axis=1)

    # Get features from dataset
    dataset_features = X.columns

    # Load model from file
    with open('blackbox.model','rb') as f:
        model_1 = pickle.load(f)

    # Get names of necessary features
    model_features = model_1.feature_names_in_

    # Create empty list to store missing features
    missing_features = []

    # Create empty list to store extra features
    extra_features = []

    # Check if the dataset is missing features
    if len(dataset_features) < len(model_features):

        # Loop through model features
        for feature in model_features:
            # Check if feature is missing and add missing feature to the list
            if feature not in dataset_features:
                missing_features.append(feature)

    # Check if the dataset has too many features
    elif len(dataset_features) > len(model_features):

        # Loop through dataset features
        for feature in dataset_features:
            # Check if feature is missing and add missing feature to the list
            if feature not in model_features:
                extra_features.append(feature)

    # If the number of features is the same, make sure they are identical
    if len(dataset_features) == len(model_features):
        
        # Loop through dataset features
        for feature in dataset_features:
            # Check if feature is missing and add missing feature to the list
            if feature not in model_features:
                extra_features.append(feature)

        # Loop through model features
        for feature in model_features:
            # Check if feature is missing and add missing feature to the list
            if feature not in dataset_features:
                missing_features.append(feature)


    # Add missing features to dataset with value of 0
    for mf in missing_features:
        X[mf] = 0

    # Drop extra features from DataSet
    X = X.drop(columns=extra_features)
    
    # Data Preparation
    X = X.values

    # Return classification (1 or 0) and probability of individual of being classified 1
    return jsonify({'ID': id,
                    'Classification': model_1.predict(X).tolist(),
                    'Probability': 100*model_1.predict_proba(X)[0,1].tolist()})


#########################################################
# Run App
#########################################################
if __name__ == "__main__":
    app.run(debug=True)