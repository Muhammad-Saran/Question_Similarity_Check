import numpy as np
import pickle
from nltk_utils import preprocess
from sklearn.feature_extraction.text import CountVectorizer

# Load the trained model and vectorizer
rf = pickle.load(open('model.pkl', 'rb'))
cv = pickle.load(open('cv.pkl', 'rb'))

bot_name = "Mueen"

def get_similarity(question1, question2):
    # Preprocess both questions
    processed_q1 = preprocess(question1)
    processed_q2 = preprocess(question2)
    
    # Vectorize both questions
    X_q1 = cv.transform([processed_q1]).toarray()
    X_q2 = cv.transform([processed_q2]).toarray()
    
    # Combine features
    X_combined = np.hstack((X_q1, X_q2))
    
    # Predict similarity
    prediction = rf.predict(X_combined)[0]
    
    # Return response based on prediction
    if prediction == 1:
        return f"{bot_name}: These questions are similar.\nQ1: '{question1}'\nQ2: '{question2}'"
    else:
        return f"{bot_name}: These questions are different.\nQ1: '{question1}'\nQ2: '{question2}'"

# Optional: Keep the command-line version for testing
if __name__ == "__main__":
    print("Let's chat! Type two questions to see if they are similar or different (type 'quit' to exit).")
    while True:
        question1 = input("You (Question 1): ")
        if question1.lower() == "quit":
            break
        
        question2 = input("You (Question 2): ")
        if question2.lower() == "quit":
            break
        
        print(get_similarity(question1, question2))
        print()
    print(f"{bot_name}: Goodbye!")