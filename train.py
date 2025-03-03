import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.ensemble import RandomForestClassifier
import pickle
from nltk_utils import preprocess

# Load and preprocess data
df = pd.read_csv('train_sample.csv')  # Assuming a CSV with 'question1', 'question2', 'is_duplicate'
new_df = df.sample(30000, random_state=2)

# Apply preprocessing from your notebook
new_df['question1'] = new_df['question1'].apply(preprocess)
new_df['question2'] = new_df['question2'].apply(preprocess)

# Combine questions for vectorization
questions = pd.concat([new_df['question1'], new_df['question2']])
cv = CountVectorizer(max_features=3000)
cv.fit(questions)

# Prepare training data
X_train_q1 = cv.transform(new_df['question1']).toarray()
X_train_q2 = cv.transform(new_df['question2']).toarray()
X_train = np.hstack((X_train_q1, X_train_q2))  # Combine features
y_train = new_df['is_duplicate'].values

# Train Random Forest model
rf = RandomForestClassifier(n_estimators=100, random_state=2)
rf.fit(X_train, y_train)

# Save the model and vectorizer
pickle.dump(rf, open('model.pkl', 'wb'))
pickle.dump(cv, open('cv.pkl', 'wb'))

print("Training complete. Model and vectorizer saved.")