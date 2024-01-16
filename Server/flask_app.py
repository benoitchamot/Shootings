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

def create_data_dict(row):
# Create a dictionary from a row
	return {'Age': row.Age,
			   'Gender': row.Gender,
			   'Race': row.Race,
			   'Immigrant': row.Immigrant,
			   'Education': row.Education,
			   'RelStatus': row.RelStatus,
			   'Employed': row.Employed,
			   'Work': row.Work,
			   'MilService': row.MilService,
			   'Arrested': row.Arrested,
			   'ParentDivorce': row.ParentDivorce,
			   'SES': row.SES,
			   'MentalIllness': row.MentalIllness,
			   'MentalIllnessHistory': row.MentalIllnessHistory,
			   'Autism': row.Autism,
               'HealthIssues': row.HealthIssues,
               'Classification': row.Classification,
               'Probability': row.Probability}

def predict_with_blackbox():
    # Load model from file
    with open('blackbox.model','rb') as f:
        model_1 = pickle.load(f)

    with open('../Server/blackbox.scaler','rb') as f:
        X_scaler = pickle.load(f)

    # Open session to the database
    session = Session(bind=engine_blackbox)

    # Get all data from table
    all_rows = session.query(analysis)

	# Loop through the measurements
    for row in all_rows:    
    	# Add the data to a dictionary
        row_dict = create_data_dict(row)

        # Create a DataFrame to hold the data
        input_data = pd.DataFrame([row_dict])

        # Get dummies
        dummies_df = pd.get_dummies(input_data.drop(columns=['Age']))
        X = pd.concat([input_data['Age'], dummies_df], axis=1)

        # Get features from dataset
        dataset_features = X.columns

        # Get names of features
        model_features = X_scaler.get_feature_names_out() 

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
                # Check if feature is extra and add extra feature to the list
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

        # Make sure the features are in the correct order
        X = X[model_features]
        
        # Data Preparation
        X = X.values

        # Scale features
        X = X_scaler.transform(X)

        # Get classification and probability from model
        classification = int(model_1.predict(X).tolist()[0])
        probability = 100*model_1.predict_proba(X)[0,1].tolist()

        # Get id of current row
        current_row_id = row.shooter_id

        # Add classification and probability to row in database
        update_record = session.query(analysis).filter(analysis.shooter_id == current_row_id).first()
        update_record.Classification = classification
        update_record.Probability = probability

        # Commit changes
        session.commit()

	# Close session
    session.close()

    return 0


def get_blackbox_data():
    # Open session to the database
    session = Session(bind=engine_blackbox)

    # Get all data from table
    all_rows = session.query(analysis)

    # Create empty lists
    rows_dicts = []

	# Loop through the measurements
    for row in all_rows:    
    	# Add the data to a dictionary
        mov_dict = create_data_dict(row)

		# Append the data to the list of dictionary
        rows_dicts.append(mov_dict)

	# Close session
    session.close()

    return rows_dicts


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

### GET DATA IN DATABASE
@app.route("/api/v1.0/blackbox/get")
def api_blackbox_get():
    
    rows_dicts = get_blackbox_data()

    if len(rows_dicts) > 0:
		# Return jsonified dictionary
        return jsonify(rows_dicts)
    else:
        return jsonify({'Error': 'No data found.'})
    
@app.route("/api/v1.0/blackbox/count")
def api_blackbox_count():
    rows_dicts = get_blackbox_data()

    return str(len(rows_dicts))
    
### RUN MODEL
@app.route("/api/v1.0/blackbox/identify")
def api_blackbox_identify():
    print('Run BlackBox Model...')

    # Run classification model on database table
    predict_with_blackbox()

    # Get all data from datavase
    rows_dicts = get_blackbox_data()

    # Return data as JSON
    if len(rows_dicts) > 0:
		# Return jsonified dictionary
        return jsonify(rows_dicts)
    else:
        return jsonify({'Error': 'No data found.'})

### CLEAR DATABASE
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

    total_risk = openbox_get_risk(state, age_bracket, mental_illness, employment, arrest, autism)

    return jsonify({'Risk': total_risk})

@app.route("/api/v1.0/blackbox/<Age>/<Gender>/<Race>/<Immigrant>/<Education>/<RelStatus>/<Employed>/<Work>/<MilService>/<Arrested>/<ParentDivorce>/<SES>/<MentalIllness>/<MentalIllnessHistory>/<Autism>/<HealthIssues>")
def api_blackbox(Age, Gender, Race, Immigrant, Education, RelStatus, Employed, Work, MilService, Arrested, ParentDivorce, SES, MentalIllness, MentalIllnessHistory, Autism, HealthIssues):

    # Add line to database
    # Open session to the database
    session = Session(bind=engine_blackbox)

    # Add data to database
    session.add(analysis(
        Age = Age,
        Gender = Gender,
        Race = Race,
        Immigrant = Immigrant,
        Education = Education.replace("+", "/"),
        RelStatus = RelStatus.replace("+", "/"),
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

    return "0"

#########################################################
# Run App
#########################################################
if __name__ == "__main__":
    app.run(debug=True)