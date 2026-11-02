"""Predict one delivery, from the command line."""
import pandas as pd
from delivery import load_model

def main():
    model = load_model("model.joblib")
    df = pd.DataFrame([{
        "distance_km": 7.0,
        "prep_time_min": 25.0,
        "traffic_level": 3,
        "rain": 0
    }])
    pred = model.predict(df)[0]
    print(f"PREDICTION: {pred:.1f}")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
