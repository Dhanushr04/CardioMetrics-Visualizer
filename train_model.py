import pandas as pd
import pickle
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Load dataset
df = pd.read_csv('heart.csv')
X = df.drop('target', axis=1)
y = df['target']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

model = LogisticRegression()
model.fit(X_train, y_train)

# Save model and scaler
with open('model/heart_model.pkl', 'wb') as f:
    pickle.dump(model, f)

with open('model/scaler.pkl', 'wb') as f:
    pickle.dump(scaler, f)

print("Model trained and saved!")
