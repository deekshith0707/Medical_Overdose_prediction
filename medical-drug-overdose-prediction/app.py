from flask import Flask, render_template, request
import numpy as np
import joblib
from database import init_db, insert_record

app = Flask(__name__)
model = joblib.load('model/overdose_model.pkl')

# Initialize DB at startup
init_db()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        dosage = float(request.form['dosage'])
        duration = float(request.form['duration'])
        prior_overdose = float(request.form['prioroverdose'])
        
        features = [age, dosage, duration, prior_overdose]
        prediction = model.predict([np.array(features)])
        probability = model.predict_proba([np.array(features)])[:,1][0] * 100

        result = "High Risk of Overdose" if prediction[0] == 1 else "Low Risk of Overdose"

        # ✅ Save to Database
        insert_record(age, dosage, duration, prior_overdose, result, round(probability, 2))

        return render_template(
            'index.html',
            prediction_text=result,
            probability=round(probability, 2)
        )
    except Exception as e:
        return f"Error: {e}"

if __name__ == '__main__':
    app.run(debug=True)
