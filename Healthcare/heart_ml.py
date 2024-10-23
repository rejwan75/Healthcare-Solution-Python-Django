import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import joblib

# Load the dataset
heart_data = pd.read_csv('./heart_disease_data.csv')

# Prepare the data
X = heart_data.drop(columns='target', axis=1)
Y = heart_data['target']

X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, stratify=Y, random_state=2)

# Train the model
model = LogisticRegression(max_iter=1000)
model.fit(X_train, Y_train)

# Save the model
joblib.dump(model, 'heart_disease_model.pkl')
joblib.dump(X.columns, 'model_columns.pkl')
