import pandas as pd
import spacy

# 1. Load trained SpaCy English model
nlp = spacy.load("en_core_web_sm")

# 2. Load anomalies dataset from Week 4
df = pd.read_csv('anomalies_detected_evidence.csv')

# 3. Extract entities from messages
extracted_entities = []

for idx, row in df.iterrows():
    text = str(row['message'])
    doc = nlp(text)
    for ent in doc.ents:
        extracted_entities.append({
            'user_id': row.get('user_id'),
            'timestamp': row.get('timestamp'),
            'is_anomaly': row.get('is_anomaly'),
            'entity_text': ent.text,
            'entity_label': ent.label_
        })

# 4. Save extracted entities to CSV
entities_df = pd.DataFrame(extracted_entities)
entities_df.to_csv('extracted_entities.csv', index=False)

print("Successfully generated 'extracted_entities.csv'.")
print(entities_df.head())