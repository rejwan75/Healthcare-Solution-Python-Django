# ml_model.py

import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
import joblib

# Load dataset
diabetes_dataset = pd.read_csv("diabetes.csv")

# Preprocess the data
X = diabetes_dataset.drop(columns='Outcome', axis=1)
Y = diabetes_dataset['Outcome']

scaler = StandardScaler()
scaler.fit(X)
X = scaler.transform(X)

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the model
classifier = svm.SVC(kernel='linear')
classifier.fit(X_train, Y_train)

# Save the model and scaler
joblib.dump(classifier, 'classifier.pkl')
joblib.dump(scaler, 'scaler.pkl')

def predict_diabetes(input_data):
    # Load the model and scaler
    classifier = joblib.load('classifier.pkl')
    scaler = joblib.load('scaler.pkl')
    
    # Convert input data to numpy array and reshape
    input_data_as_numpy_array = np.asarray(input_data)
    input_data_reshaped = input_data_as_numpy_array.reshape(1, -1)
    
    # Standardize the input data
    std_data = scaler.transform(input_data_reshaped)
    
    # Make a prediction
    prediction = classifier.predict(std_data)
    
    return 'The person is diabetic' if prediction[0] == 1 else 'The person is not diabetic'
