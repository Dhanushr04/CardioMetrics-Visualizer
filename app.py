from flask import Flask, render_template, request, jsonify
import numpy as np
import pickle

app = Flask(__name__)

model = pickle.load(open('model/heart_model.pkl', 'rb'))
scaler = pickle.load(open('model/scaler.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        features = [float(x) for x in request.form.values()]
        scaled = scaler.transform([features])
        prediction = model.predict(scaled)[0]
        prob = model.predict_proba(scaled)[0][prediction] * 100
        return jsonify({
            'prediction': 'High Risk' if prediction else 'Low Risk',
            'probability': round(prob, 2)
        })
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)
