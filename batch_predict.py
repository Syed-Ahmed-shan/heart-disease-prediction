import pandas as pd
import joblib
import os
from ai_assistant.offline_health_report import generate_offline_report
from ai_assistant.pdf_report_generator import save_report_to_pdf  # ✅ NEW

# ✅ Ensure output folders exist
os.makedirs('output', exist_ok=True)
os.makedirs('output/reports', exist_ok=True)

# Load model
model = joblib.load('models/heart_disease_model.pkl')

# Load batch data
df = pd.read_csv('data/heart.csv')

# Remove extra columns if present
if 'target' in df.columns:
    df = df.drop(columns=['target'])

# Ensure correct column order
expected_features = ['age', 'sex', 'chest pain type', 'resting bp s',
                     'cholesterol', 'fasting blood sugar', 'resting ecg',
                     'max heart rate', 'exercise angina', 'oldpeak', 'ST slope']
df = df[expected_features]

# Predict
df['target'] = model.predict(df)

# AI reports
df['ai_report'] = df.apply(generate_offline_report, axis=1)

# Save batch CSV
df.to_csv('output/batch_results.csv', index=False)
print(" Batch prediction saved to output/batch_results.csv")

# ✅ Save each report as PDF
for idx, row in df.iterrows():
    save_report_to_pdf(patient_id=idx + 1, report_text=row['ai_report'])

print(" Individual PDF reports saved in output/reports/")
