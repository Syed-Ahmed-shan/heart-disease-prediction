import streamlit as st
import pandas as pd
import joblib
import os
import matplotlib.pyplot as plt
import seaborn as sns
from ai_assistant.offline_health_report import generate_offline_report
from ai_assistant.pdf_report_generator import save_report_to_pdf

# Load model
model = joblib.load('models/heart_disease_model.pkl')
os.makedirs('output/reports', exist_ok=True)

st.set_page_config(page_title="Heart Health AI", layout="centered")
st.title("🩺 AI-Powered Heart Disease Prediction Dashboard")

# =========================
# 1️⃣ Manual Form Entry
# =========================
st.header("🧾 Enter Patient Details Manually")

with st.form("manual_entry_form"):
    age = st.number_input("Age", 1, 120, 30)
    sex = st.selectbox("Sex", ["Male", "Female"])
    cp = st.selectbox("Chest Pain Type", [0, 1, 2, 3])
    trestbps = st.number_input("Resting Blood Pressure", 80, 200, 120)
    chol = st.number_input("Cholesterol", 100, 400, 200)
    fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl", [0, 1])
    restecg = st.selectbox("Resting ECG Results", [0, 1, 2])
    thalach = st.number_input("Max Heart Rate Achieved", 60, 220, 150)
    exang = st.selectbox("Exercise-induced Angina", [0, 1])
    oldpeak = st.number_input("ST Depression (Oldpeak)", 0.0, 10.0, 1.0, step=0.1)
    slope = st.selectbox("Slope of ST Segment", [0, 1, 2])
    submit = st.form_submit_button("🔍 Predict Manually")

if submit:
    sample = {
        'age': age,
        'sex': 1 if sex == "Male" else 0,
        'chest pain type': cp,
        'resting bp s': trestbps,
        'cholesterol': chol,
        'fasting blood sugar': fbs,
        'resting ecg': restecg,
        'max heart rate': thalach,
        'exercise angina': exang,
        'oldpeak': oldpeak,
        'ST slope': slope
    }

    input_df = pd.DataFrame([sample])
    prediction = model.predict(input_df)[0]
    sample['target'] = int(prediction)

    st.subheader("Prediction Result")
    st.success("Heart Disease Detected" if prediction == 1 else "No Disease")

    report = generate_offline_report(sample)
    st.subheader("AI Health Summary")
    st.text(report)

    pdf_path = f"output/reports/patient_manual.pdf"

    save_report_to_pdf("manual", report)
    with open(pdf_path, "rb") as file:
        st.download_button("📄 Download PDF Report", file, "manual_patient_report.pdf", mime="application/pdf")

# =========================
# 2️⃣ Upload CSV for Batch
# =========================
st.header("📤 Upload Health Report CSV")

uploaded_file = st.file_uploader("Upload CSV (Batch patients)", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    required_cols = ['age', 'sex', 'chest pain type', 'resting bp s',
                     'cholesterol', 'fasting blood sugar', 'resting ecg',
                     'max heart rate', 'exercise angina', 'oldpeak', 'ST slope']

    if not all(col in df.columns for col in required_cols):
        st.error("❌ Uploaded CSV is missing required columns.")
    else:
        df = df[required_cols]
        df['target'] = model.predict(df)
        df['ai_report'] = df.apply(generate_offline_report, axis=1)

        st.success("✅ Batch Prediction Completed")

        for idx, row in df.iterrows():
            st.subheader(f"📌 Patient {idx+1}")
            st.write(f"**Prediction:** {'Heart Disease Detected' if row['target'] == 1 else 'No Disease'}")
            st.text(row['ai_report'])

            pdf_path = f"output/reports/patient_{idx+1}.pdf"
            save_report_to_pdf(idx + 1, row['ai_report'])

            with open(pdf_path, "rb") as file:
                st.download_button(
                    label="📄 Download PDF Report",
                    data=file,
                    file_name=f"patient_{idx+1}_report.pdf",
                    mime="application/pdf"
                )

        # =========================
        # 📊 Visualizations
        # =========================
        st.header("📈 Batch Data Insights")
        col1, col2 = st.columns(2)

        with col1:
            fig, ax = plt.subplots()
            sns.countplot(data=df, x='target', ax=ax)
            ax.set_xticklabels(['No Disease', 'Disease'])
            ax.set_title("Heart Disease Prediction Count")
            st.pyplot(fig)

        with col2:
            fig2, ax2 = plt.subplots()
            sns.histplot(df['age'], bins=10, kde=True, ax=ax2)
            ax2.set_title("Age Distribution")
            st.pyplot(fig2)
