import pandas as pd
from sklearn.ensemble import IsolationForest

# 1. Load feature-engineered evidence
df = pd.read_csv('feature_engineered_evidence.csv')

# 2. Select numerical features for model training
# Converting boolean/categorical columns if necessary
features = df[['hour_of_day', 'is_weekend']].copy()

# 3. Train Isolation Forest model
model = IsolationForest(contamination=0.1, random_state=42)
df['is_anomaly'] = model.fit_predict(features)

# 4. Save results to CSV (-1 indicates anomaly, 1 indicates normal)
df.to_csv('anomalies_detected_evidence.csv', index=False)
print("Successfully generated 'anomalies_detected_evidence.csv'.")
print(f"Total anomalies detected: {(df['is_anomaly'] == -1).sum()}")