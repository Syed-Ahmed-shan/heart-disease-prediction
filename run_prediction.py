import pandas as pd
import joblib
from ai_assistant.offline_health_report import generate_offline_report

# Load the model
model = joblib.load('models/heart_disease_model.pkl')

# 🔄 Ask user for input dynamically
def get_patient_data():
    print("\n Enter Patient Details:")
    sample = {
        'age': int(input("Age: ")),
        'sex': int(input("Sex (1 = Male, 0 = Female): ")),
        'chest pain type': int(input("Chest Pain Type (0–3): ")),
        'resting bp s': int(input("Resting Blood Pressure: ")),
        'cholesterol': int(input("Cholesterol: ")),
        'fasting blood sugar': int(input("Fasting Blood Sugar (1 = True, 0 = False): ")),
        'resting ecg': int(input("Resting ECG (0–2): ")),
        'max heart rate': int(input("Max Heart Rate: ")),
        'exercise angina': int(input("Exercise Angina (1 = Yes, 0 = No): ")),
        'oldpeak': float(input("Oldpeak (ST depression): ")),
        'ST slope': int(input("ST Slope (0–2): "))
    }
    return sample

# 🔁 Get input from user
sample = get_patient_data()

# Convert to DataFrame
input_df = pd.DataFrame([sample])

# Predict
prediction = model.predict(input_df)[0]
sample['target'] = int(prediction)

# Result
print(f"\n Prediction: {' Disease Detected' if prediction == 1 else ' No Disease'}")

# AI Report
report = generate_offline_report(sample)
print("\n AI Health Summary:\n")
print(report)
