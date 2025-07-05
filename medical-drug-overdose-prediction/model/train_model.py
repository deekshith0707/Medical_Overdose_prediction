import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report
import joblib

# Load dataset
df = pd.read_csv('dataset.csv')

X = df[['Age', 'Dosage', 'Duration', 'PriorOverdose']]
y = df['OverdoseRisk']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save Model
joblib.dump(model, 'model/overdose_model.pkl')
print("Model saved successfully.")
