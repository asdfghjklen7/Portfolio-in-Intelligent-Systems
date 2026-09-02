import pandas as pd
 
# Load the cleaned evidence from Week 2
df = pd.read_csv('cleaned_evidence.csv', parse_dates=['timestamp'])
 
# Extract new features
df['hour_of_day'] = df['timestamp'].dt.hour
df['day_of_week'] = df['timestamp'].dt.day_name() # or dt.day depending on your implementation
df['is_weekend'] = df['timestamp'].dt.dayofweek >= 5
 
# Save the enhanced data
df.to_csv('feature_engineered_evidence.csv', index=False)