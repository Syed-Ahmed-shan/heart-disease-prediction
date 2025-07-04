📚 Project Documentation
📁 Folder Structure:

heart_project/
│
├── data/
│   └── heart.csv               # Dataset used
│
├── models/
│   └── predict_heart_disease.py  # Core prediction logic
│
├── README.md                   # Project overview (optional)
📌 1. Dataset Info
Source: UCI Heart Disease Dataset

Records: 303 rows

Features:

Feature	Description
age	Age of the patient
sex	1 = male, 0 = female
cp	Chest pain type (0–3)
trestbps	Resting blood pressure
chol	Serum cholesterol
fbs	Fasting blood sugar > 120 mg/dl
restecg	Resting ECG results
thalach	Max heart rate achieved
exang	Exercise induced angina
oldpeak	ST depression induced by exercise
slope	Slope of peak exercise ST segment
ca	Number of major vessels (0–3)
thal	Thalassemia (0 = normal; 1 = fixed defect; 2 = reversible defect)
target	1 = heart disease, 0 = no disease

📌 2. Core Technologies Used
🐍 Python 3

📦 pandas, matplotlib, seaborn for data handling and visualization

🤖 sklearn for model building

🧪 LogisticRegression for binary classification

📌 3. Key Code Modules
🔍 Correlation Heatmap
python
Copy
Edit
sns.heatmap(df.corr(), annot=True, cmap="coolwarm")
🏗️ Model Training
python
Copy
Edit
model = LogisticRegression(max_iter=1000)
model.fit(X_train, y_train)
📊 Evaluation
python
Copy
Edit
accuracy_score(y_test, y_pred)
classification_report(y_test, y_pred)
confusion_matrix(y_test, y_pred)

📌 4. Model Performance
Achieved ~85% accuracy on test data

Confusion matrix used to visualize false positives & negatives

Classification report with precision, recall, F1-score

📝 Future Improvements
Integrate with a Flask/Django web app for user input

Add SHAP or LIME explainability for model transparency

Store predictions in a SQLite or PostgreSQL DB

Build a responsive frontend using React or HTML/CSS

