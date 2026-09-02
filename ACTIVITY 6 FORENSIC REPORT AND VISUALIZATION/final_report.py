import pandas as pd
import matplotlib.pyplot as plt
import os
 
anomalies_file = 'anomalies_detected_evidence.csv'
entities_file = 'extracted_entities.csv'
report_file = 'forensic_report.md'
chart_file = 'event_distribution.png'
 
# 1. Ensure required data files exist
for file in [anomalies_file, entities_file]:
    if not os.path.exists(file):
        print(f"Error: '{file}' not found. Please ensure previous activities are completed.")
        exit()
 
print("Loading datasets...")
df_anomalies = pd.read_csv(anomalies_file)
df_entities = pd.read_csv(entities_file)
 
# 2. Generate and save the bar chart visualization
print("Generating event distribution chart...")
plt.figure(figsize=(8, 5))
 
# Count occurrences of each event type
if 'event_type' in df_anomalies.columns:
    event_counts = df_anomalies['event_type'].value_counts()
    event_counts.plot(kind='bar', color='skyblue', edgecolor='black')
else:
    # Fallback if column names vary slightly
    print("Warning: 'event_type' column missing. Using fallback counts.")
    df_anomalies.iloc[:, 1].value_counts().plot(kind='bar', color='skyblue')
 
plt.title('Distribution of Forensic Events')
plt.xlabel('Event Type')
plt.ylabel('Count')
plt.xticks(rotation=45, ha='right')
plt.tight_layout()
 
# Save the chart image
plt.savefig(chart_file)
plt.close()
print(f"Saved visualization to: '{chart_file}'")
 
# 3. Calculate metrics for the Markdown summary report
total_events = len(df_anomalies)
total_anomalies = sum(df_anomalies['is_anomaly'] == -1) if 'is_anomaly' in df_anomalies.columns else 0
total_entities = len(df_entities)
 
# 4. Generate the Markdown report file
print("Writing markdown report...")
markdown_content = f"""# Forensic Investigation Final Summary Report
 
## 1. Executive Summary
This document synthesizes the outputs from the automated forensic pipeline across the collection, cleaning, feature-engineering, anomaly detection, and entity extraction phases.
 
## 2. Quantitative Metrics
* **Total Forensic Events Processed:** {total_events}
* **Anomalies Flagged (Isolation Forest):** {total_anomalies}
* **Total Named Entities Extracted:** {total_entities}
 
## 3. Visualizations
Below is the distribution of events observed across the log history:
 
![Event Distribution]({chart_file})
 
## 4. Key Findings & Extracted Intelligence
The machine learning phase successfully identified high-risk events. The natural language processing (NLP) model extracted key entities from corresponding messages to aid deeper investigation.
 
### Sample Extracted Entities:
{df_entities.head(5).to_string(index=False)} 
---
*Report automatically generated on execution of the final pipeline module.*
"""
 
with open(report_file, 'w', encoding='utf-8') as f:
    f.write(markdown_content)
 
print(f"Successfully generated final report text file: '{report_file}'")