import joblib
import numpy as np

# Load the trained model
model = joblib.load("timing_classifier.pkl")

def classify_timing(time_ns):
    """Classify a new timing measurement."""
    time_ns = np.array([[time_ns]])  # Reshape for model input
    prediction = model.predict(time_ns)[0]

    # Interpret prediction
    if prediction == 0:
        return "🔴 Insecure (Early Exit Detected)"
    else:
        return "🟢 Constant-Time (Secure)"

# CLI Loop
if __name__ == "__main__":
    print("=== Timing Classifier CLI ===")
    
    while True:
        try:
            user_input = input("\nEnter timing measurement (ns) or 'exit' to quit: ")
            if user_input.lower() == "exit":
                break

            time_ns = float(user_input)
            result = classify_timing(time_ns)
            print(f"Prediction: {result}")

        except ValueError:
            print("⚠️ Please enter a valid number.")
