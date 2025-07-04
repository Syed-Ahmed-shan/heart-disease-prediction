# train_model.py

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

# Load dataset
data_path = os.path.join('data', 'heart.csv')
df = pd.read_csv(data_path)

# Features and Target
X = df.drop('target', axis=1)
y = df['target']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save the model
model_dir = 'models'
os.makedirs(model_dir, exist_ok=True)
joblib.dump(model, os.path.join(model_dir, 'heart_disease_model.pkl'))

print("✅ Model trained and saved successfully!")
