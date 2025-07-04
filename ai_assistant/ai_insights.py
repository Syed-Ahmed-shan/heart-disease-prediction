# ai_assistant/ai_insights.py

import openai
import os

# ✅ Set your OpenAI API key
client = openai.OpenAI(api_key="your-openai-api-key-here")  # Replace with your actual key

# 🧠 Function to generate report
def generate_health_report(patient_data):
    prompt = f"""
    A patient has the following heart health indicators:\n
    Age: {patient_data['age']}, Sex: {patient_data['sex']}, 
    Chest Pain Type: {patient_data['cp']}, Resting BP: {patient_data['trestbps']}, 
    Cholesterol: {patient_data['chol']}, Fasting Blood Sugar: {patient_data['fbs']}, 
    ECG: {patient_data['restecg']}, Max Heart Rate: {patient_data['thalach']}, 
    Exercise Angina: {patient_data['exang']}, Oldpeak: {patient_data['oldpeak']}, 
    Slope: {patient_data['slope']}, Ca: {patient_data['ca']}, Thal: {patient_data['thal']}.

    Based on these, explain in plain language the possible health risk.
    """

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",  # or "gpt-4"
        messages=[{"role": "user", "content": prompt}],
        max_tokens=200,
        temperature=0.7
    )
    return response.choices[0].message.content

# 🧪 Example use
if __name__ == "__main__":
    sample = {
        'age': 54, 'sex': 1, 'cp': 0, 'trestbps': 130,
        'chol': 250, 'fbs': 0, 'restecg': 1, 'thalach': 140,
        'exang': 1, 'oldpeak': 2.3, 'slope': 1, 'ca': 0, 'thal': 2
    }

    report = generate_health_report(sample)
    print(" AI Health Report:\n")
    print(report)