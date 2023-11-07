import pandas as pd
import pickle

# Ignore warnings
import warnings
warnings.simplefilter(action='ignore')

def predict_with_blackbox(Age, Gender, Race, Immigrant, Education, RelStatus, Employed, Work, MilService, Arrested, ParentDivorce, SES, MentalIllness, MentalIllnessHistory, Autism, HealthIssues):

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

    # Make sure the features are in the correct order
    X = X[model_features]
    
    # Data Preparation
    X = X.values

    classification = model_1.predict(X).tolist()
    probability = 100*model_1.predict_proba(X)[0,1].tolist()

    return classification, probability

    