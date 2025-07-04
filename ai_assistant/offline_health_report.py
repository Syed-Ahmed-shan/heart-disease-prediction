def generate_offline_report(patient):
    age = patient.get('age', 0)
    gender = 'Male' if patient['sex'] == 1 else 'Female'
    report = f"🩺 Patient Report (Age {age}, Gender: {gender})\n"
    report += "-" * 60 + "\n"

    # Observations
    if patient['cholesterol'] > 240:
        report += "- High cholesterol level.\n"
    else:
        report += "- Cholesterol is within safe range.\n"

    if patient['resting bp s'] > 130:
        report += "- Elevated resting blood pressure.\n"
    else:
        report += "- Blood pressure is normal.\n"

    if patient['max heart rate'] < 120:
        report += "- Low maximum heart rate — potential concern.\n"
    else:
        report += "- Healthy heart rate response.\n"

    if patient['exercise angina'] == 1:
        report += "- Shows signs of exercise-induced angina.\n"

    if patient['oldpeak'] > 2:
        report += "- ST depression is significant — needs monitoring.\n"

    # AI Prediction
    report += "\n🧠 AI Model Prediction: "
    if patient['target'] == 1:
        report += "Heart Disease Detected\n"
        report += "Risk Level: HIGH\n"

        # Recommendations
        report += "\n📝 Health Recommendations\n"
        report += "-" * 26 + "\n"

        # ➤ Age-wise diet & medicine
        if age < 40:
            report += "\n💡 Diet Plan:\n"
            report += "- Avoid fried food, red meat, processed snacks.\n"
            report += "- Eat oats, greens, walnuts, fruits, fish (omega-3).\n"
            report += "- Salt intake < 2g/day.\n"

            report += "\n🏃 Exercise Routine:\n"
            report += "- 30 min brisk walk, 5 days/week.\n"
            report += "- Light resistance training, yoga & pranayama.\n"

            report += "\n💊 Medication:\n"
            report += "- Ecosprin 75–150mg (after breakfast)\n"
            report += "- Atorvastatin 10–20mg (at bedtime)\n"
            report += "- Metoprolol 25–50mg if BP is high\n"
            report += "- Ramipril 2.5–5mg if diabetes/BP present\n"

        elif 40 <= age <= 60:
            report += "\n💡 Diet Plan:\n"
            report += "- Mediterranean/DASH diet, more greens & pulses.\n"
            report += "- Less red meat, oil (max 4 tsp/day), sweets.\n"

            report += "\n🏃 Exercise Routine:\n"
            report += "- 30–45 mins walk, 5–6 days/week.\n"
            report += "- Light cycling/swimming if tolerated.\n"

            report += "\n💊 Medication:\n"
            report += "- Aspirin 75–150mg (if advised)\n"
            report += "- Atorvastatin 20–40mg if LDL > 100\n"
            report += "- Amlodipine or Ramipril for BP\n"
            report += "- Clopidogrel 75mg as antiplatelet\n"

        else:  # age > 60
            report += "\n💡 Diet Plan:\n"
            report += "- Light & easy-to-digest food.\n"
            report += "- High-fiber (soups, porridge, fruits).\n"
            report += "- Reduce salt/sugar intake. Stay hydrated.\n"

            report += "\n🏃 Exercise Routine:\n"
            report += "- Walk 20–30 min/day (or 10 min x 3).\n"
            report += "- Chair yoga, breathing exercises.\n"

            report += "\n💊 Medication:\n"
            report += "- Aspirin 75mg (low dose)\n"
            report += "- Atorvastatin or Rosuvastatin 10mg\n"
            report += "- Metoprolol 25mg (if needed)\n"
            report += "- Furosemide if fluid retention\n"

        report += "\n🧘 Lifestyle Tips:\n"
        report += "- Avoid smoking/alcohol, manage stress.\n"
        report += "- Sleep 7–8 hrs/day, do meditation.\n"
        report += "- Regular heart, kidney, and liver checkups.\n"

    else:
        report += "No Heart Disease\n"
        report += "Risk Level: LOW\n"

        report += "\n✅ You're healthy! Maintain a heart-safe lifestyle.\n"
        report += "🧘 Lifestyle Tips:\n"
        report += "- Balanced diet & hydration.\n"
        report += "- 30 min light walk/yoga daily.\n"
        report += "- 7–8 hrs sleep, low stress.\n"
        report += "- Annual checkups after age 35.\n"

    return report
