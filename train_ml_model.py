import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import joblib

# Load the preprocessed data
df = pd.read_csv("processed_timing_data.csv")

# Encode labels ("insecure" -> 0, "constant" -> 1)
encoder = LabelEncoder()
df["type"] = encoder.fit_transform(df["type"])  

# Split data into features (X) and labels (y)
X = df[["time_ns"]].values
y = df["type"].values

# Split into training and test sets (80% training, 20% testing)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a simple Logistic Regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predict and evaluate
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)

print(f"Model Accuracy: {accuracy * 100:.2f}%")
print(classification_report(y_test, y_pred, target_names=encoder.classes_))

# Save the trained model
joblib.dump(model, "timing_classifier.pkl")
print("Model saved as timing_classifier.pkl")
