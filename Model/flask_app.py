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

# Path to databases
ob_db_path1 = Path('openbox_db.sqlite')
ob_db_path2 = Path('blackbox_db.sqlite')

# Create engine to openbox_db.sqlite
print("Connecting to openbox_db...")
engine_openbox = create_engine(f"sqlite:///{ob_db_path1}")
print("Connected.")

# Reflect the database into a new model
print("Reflecting database...")
Base_openbox = automap_base()
print("Done.")

# Reflect the tables
print("Reflecting tables...")
try:
	Base_openbox.prepare(engine_openbox, reflect=True)
	print("Done.")
except Exception as inst:
    print(f"\nError: {inst}")
    print("\n*** HINT: please run script from within Server directory ***\n")
    quit()

# Save references to each table
riskmatrix = Base_openbox.classes.riskmatrix

# Create engine to blackbox_db.sqlite
print("Connecting to blackbox_db...")
engine_blackbox = create_engine(f"sqlite:///{ob_db_path2}")
print("Connected.")

# Reflect the database into a new model
print("Reflecting database...")
Base_blackbox = automap_base()
print("Done.")

# Reflect the tables
print("Reflecting tables...")
try:
	Base_blackbox.prepare(engine_blackbox, reflect=True)
	print("Done.")
except Exception as inst:
    print(f"\nError: {inst}")
    print("\n*** HINT: please run script from within Server directory ***\n")
    quit()

# Save references to each table
shooters = Base_blackbox.classes.shooters
analysis = Base_blackbox.classes.analysis


#########################################################
# Functions
#########################################################

# Determine risk
def openbox_get_risk(state, age_bracket, mental_illness, employment, arrest, autism):

    # Open session to the database
    session = Session(bind=engine_openbox)
    risk_in_state = session.query(riskmatrix).filter(riskmatrix.state == str(state))[0]

    # Get risk for age bracket lookup table
    risk_age_lookup = {
        'Under 10 years old': risk_in_state.age_Under_10,
        '10 to 14 years': risk_in_state.age_10_to_14,
        '15 to 17 years': risk_in_state.age_15_to_17,
        '18 and 19 years': risk_in_state.age_18_and_19,
        '20 years': risk_in_state.age_20,
        '21 years': risk_in_state.age_21,
        '22 to 24 years': risk_in_state.age_22_to_24,
        '25 to 29 years': risk_in_state.age_25_to_29,
        '30 to 34 years': risk_in_state.age_30_to_34,
        '35 to 39 years': risk_in_state.age_35_to_39,
        '40 to 44 years': risk_in_state.age_40_to_44,
        '45 to 49 years': risk_in_state.age_45_to_49,
        '50 to 54 years': risk_in_state.age_50_to_54,
        '55 to 59 years': risk_in_state.age_55_to_59,
        '60 and 61 years': risk_in_state.age_60_and_61,
        '62 to 64 years': risk_in_state.age_62_to_64,
        '65 and 66 years': risk_in_state.age_65_and_66,
        '67 to 69 years': risk_in_state.age_67_to_69,
        '70 to 74 years': risk_in_state.age_70_to_74,
        '75 years and over': risk_in_state.age_75_over
    }
    
    # Get risk for age bracket based on lookup table
    risk_age = risk_age_lookup[age_bracket]

    # Default values
    risk_mental = 1
    risk_employment = 1
    risk_arrest = 1
    risk_autism = 1

    # Update values based on risk matrix
    if mental_illness == '1':
        risk_mental = risk_in_state.mental_illness
    elif mental_illness == '0':
        risk_mental = 1

    if employment == '1':
        risk_employment = 1
    elif employment == '0':
        risk_employment = risk_in_state.unemployment

    if arrest == '1':
        risk_arrest = risk_in_state.arrest
    elif arrest == '1':
        risk_arrest = 1

    if autism == '1':
        risk_autism = risk_in_state.autism
    elif autism == '1':
        risk_autism = 1

    # Close session
    session.close()

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
# Flask Static Routes
#########################################################
@app.route("/api/v1.0/blackbox/clear")
def api_blackbox_clear():
    # Open session to the database
    session = Session(bind=engine_blackbox)

    try:
        # Delete rows in analysis table
        session.query(analysis).delete()

        # Commit changes to session
        session.commit()

        # Close session
        session.close()
        return "0"
    
    except Exception as error:
        # Close session
        session.close()
        print(error)
        return str(error)

#########################################################
# Flask Dynamic Routes
#########################################################

@app.route("/api/v1.0/openbox/<state>/<age_bracket>/<mental_illness>/<employment>/<arrest>/<autism>")
def api_openbox(state, age_bracket, mental_illness, employment, arrest, autism):

    total_tisk = openbox_get_risk(state, age_bracket, mental_illness, employment, arrest, autism)

    return jsonify({'Risk': total_tisk})

@app.route("/api/v1.0/blackbox/<id>/<Age>/<Gender>/<Race>/<Immigrant>/<Education>/<RelStatus>/<Employed>/<Work>/<MilService>/<Arrested>/<ParentDivorce>/<SES>/<MentalIllness>/<MentalIllnessHistory>/<Autism>/<HealthIssues>")
def api_blackbox(id, Age, Gender, Race, Immigrant, Education, RelStatus, Employed, Work, MilService, Arrested, ParentDivorce, SES, MentalIllness, MentalIllnessHistory, Autism, HealthIssues):

    # Add line to database
    # Open session to the database
    session = Session(bind=engine_blackbox)

    # Add data to database
    session.add(analysis(
        Age = Age,
        Gender = Gender,
        Race = Race,
        Immigrant = Immigrant,
        Education = Education,
        RelStatus = RelStatus,
        Employed = Employed,
        Work = Work,
        MilService = MilService,
        Arrested = Arrested,
        ParentDivorce = ParentDivorce,
        SES = SES,
        MentalIllness = MentalIllness,
        MentalIllnessHistory = MentalIllnessHistory,
        Autism = Autism,
        HealthIssues = HealthIssues,
    ))

    # Commit changes to session
    session.commit()

    # Close session
    session.close()

    # Run classification model
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