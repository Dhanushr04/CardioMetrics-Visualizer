# HeartWise: Heart Disease Risk Predictor

A simple, responsive machine learning web app built with Flask that predicts the risk of heart disease using patient data. It’s powered by logistic regression and a clean Bootstrap-based UI.

## 🎯 Project Goals
- Predict if a person is at risk of heart disease using health attributes.
- Offer a user-friendly, mobile-responsive interface.
- Visualize prediction results clearly using charts.
- Easily train the model with your own CSV dataset (`heart.csv`).

## 🧰 Tech Stack

| Layer     | Technology                        |
|-----------|-----------------------------------|
| Frontend  | HTML, Bootstrap 5, JavaScript, Chart.js |
| Backend   | Python Flask                      |
| ML Model  | Logistic Regression (scikit-learn)|
| Data Prep | pandas, StandardScaler            |
| Dataset   | `heart.csv` (from UCI / Kaggle)   |
| Deployment| Localhost / Render / Heroku       |

## 📁 Folder Structure

```
HeartWise_CustomDataset/
├── app.py                 → Flask app to run the web server
├── train_model.py         → Script to train and save the ML model
├── heart.csv              → Dataset used for training (user-provided)
│
├── /model/
│   ├── heart_model.pkl    → Trained logistic regression model
│   └── scaler.pkl         → Preprocessing scaler
│
├── /templates/
│   └── index.html         → Responsive Bootstrap form
│
└── /static/
    └── style.css (optional)
```

## 🧪 How It Works
1. **User Input**: Form collects 13 features like age, sex, cholesterol, etc.
2. **Preprocessing**: Inputs are scaled using the same StandardScaler from training.
3. **Prediction**: Logistic regression predicts risk (0 = Low, 1 = High).
4. **Output**: Displays risk label and donut chart for confidence score.

## 🧠 Features
✅ Responsive form layout (Bootstrap grid)  
✅ Real-time prediction via Fetch API (no page reload)  
✅ Simple and interpretable logistic regression  
✅ Chart.js donut chart for clear result visualization  
✅ Easily extendable to other ML models (like XGBoost)  
✅ Custom CSV training with `train_model.py`  

## 📊 Input Features Required

| Feature Name | Description |
|--------------|-------------|
| age          | Age of the patient |
| sex          | 1 = male, 0 = female |
| cp           | Chest pain type (0–3) |
| trestbps     | Resting blood pressure |
| chol         | Serum cholesterol (mg/dl) |
| fbs          | Fasting blood sugar > 120 mg/dl |
| restecg      | Resting ECG result |
| thalach      | Max heart rate achieved |
| exang        | Exercise-induced angina |
| oldpeak      | ST depression induced by exercise |
| slope        | Slope of peak exercise ST segment |
| ca           | Number of major vessels (0–3) |
| thal         | 3 = normal, 6 = fixed defect, 7 = reversible defect |