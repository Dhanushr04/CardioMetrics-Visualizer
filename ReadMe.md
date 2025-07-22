
# ❤️ HeartWise

**HeartWise** is a vibrant, full-stack web application designed to predict heart disease risk and guide users toward better cardiovascular health. It features a user-friendly interface, interactive visualizations, and machine learning integration — all built using Flask (or Django), SQLite/MySQL, HTML, CSS, and JavaScript.

---

## 🚀 Features

- 🔐 **User Authentication** (Login/Signup)
- 🧠 **Heart Disease Prediction** using Machine Learning
- 📊 **Health Analytics Dashboard** with interactive graphs
- 🩺 **Vital Parameter Input** (age, cholesterol, blood pressure, etc.)
- 💬 **Personalized Health Recommendations**
- 📱 **Responsive & Colorful UI** built with Bootstrap
- 📁 **Data Storage** with SQLite/MySQL backend
- ☁️ **Deployed Locally or on Cloud (e.g. Render/Heroku)**

---

## 🛠️ Tech Stack

| Layer         | Technology               |
|---------------|---------------------------|
| Frontend      | HTML5, CSS3, Bootstrap, JS |
| Backend       | Flask / Django            |
| Database      | SQLite / MySQL            |
| ML Model      | Scikit-learn (RandomForest/SVM) |
| Visualization | Chart.js / Matplotlib     |
| Deployment    | Render / Localhost        |

---

## 📦 Installation

1. **Clone the repo**

```bash
git clone https://github.com/Dhanushr04/HeartHealth
cd HeartHealth
```

2. **Install dependencies**

```bash
pip install -r requirements.txt
```

3. **Run the app**

```bash
python app.py   # For Flask
# or
python manage.py runserver   # For Django
```

4. **Access**

Go to `http://localhost:5000` or `http://127.0.0.1:8000` depending on your backend.

---

## 📁 Folder Structure

```
HeartHealth/
├── static/
│   ├── css/
│   ├── js/
│   └── images/
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   └── result.html
├── models.py
├── app.py / manage.py
├── requirements.txt
├── README.md
└── heart_model.pkl
```

---

## 🧪 Sample Inputs

| Feature             | Example Value |
|---------------------|----------------|
| Age                 | 54             |
| Sex                 | Male           |
| Chest Pain Type     | 1              |
| Resting BP          | 130            |
| Cholesterol         | 246            |
| Fasting Blood Sugar | 0              |
| Thalassemia         | 2              |

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you’d like to change.

---

## 📄 License

MIT License © 2025 HeartWise Team

---

## ❤️ Credits

Developed with care to keep your heart healthy.  
ML Model powered by open medical datasets and research.
