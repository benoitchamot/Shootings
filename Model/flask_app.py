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

# CORS
from flask_cors import CORS

# Ignore warnings
import warnings
warnings.simplefilter(action='ignore')

# Import local modules
from model_blacbox import predict_with_blackbox

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

    classification, probability = predict_with_blackbox(Age, Gender, Race, Immigrant, Education, RelStatus, Employed, Work, MilService, Arrested, ParentDivorce, SES, MentalIllness, MentalIllnessHistory, Autism, HealthIssues)

    # Return classification (1 or 0) and probability of individual of being classified 1
    return jsonify({'ID': id,
                    'Classification': classification,
                    'Probability': probability})

#########################################################
# Run App
#########################################################
if __name__ == "__main__":
    app.run(debug=True)