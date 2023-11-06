# This module contains functions that are commonly used in classification projects (supervised learning)
# ---
# Author: Benoit Chamot
# Date: 13/10/2023
# ---

import pandas as pd
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score

def get_precision(cm):
# Calculate the recall for a given confusion matrix
    TP = cm[0,0]
    FN = cm[0,1]
    FP = cm[1,0]
    TN = cm[1,1]

    precision_0 = TP/(TP+FP)
    precision_1 = TN/(TN+FN)

    return precision_0, precision_1

def get_recall(cm):
# Calculate the recall for a given confusion matrix
    TP = cm[0,0]
    FN = cm[0,1]
    FP = cm[1,0]
    TN = cm[1,1]

    recall_0 = TP/(TP+FN)
    recall_1 = TN/(TN+FP)

    return recall_0, recall_1

def model_performance(y_test, predictions, print_result):
# Print the accuracy, confusion matrix and classification report
    # Calculating the confusion matrix
    cm = confusion_matrix(y_test, predictions)
    cm_df = pd.DataFrame(
        cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"]
    )

    # Calculate the accuracy score
    acc_score = accuracy_score(y_test, predictions)

    # Calculate precision and recall
    precision_0, precision_1 = get_precision(cm)
    recall_0, recall_1 = get_recall(cm)

    # Save metrics in dictionary
    metrics_dict = {
        'accuracy': acc_score,
        'precision_0': precision_0,
        'precision_1': precision_1,
        'recall_0': recall_0,
        'recall_1': recall_1
    }

    # Displaying results
    if print_result:
        print("Confusion Matrix:")
        print(cm_df)
        print('---')
        print(f"Accuracy Score : {acc_score}")
        print('---')
        print("Classification Report:")
        print(classification_report(y_test, predictions))

    return metrics_dict