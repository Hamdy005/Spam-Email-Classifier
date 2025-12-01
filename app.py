import os
import pickle
import streamlit as st 
import re
import nltk
import contractions
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
nltk.download('wordnet')
nltk.download('stopwords')

## Setting Page Configuration and Header
st.set_page_config(
    page_title="Spam Email Classifier",
    page_icon="📧",
    layout="wide",
) 

st.title("📧 Spam Email Classifier")
st.write("Enter your email content below and the model will predict whether it is Spam or Ham (Not Spam).")


## Preprocessing Function
def preprocess_text(text):

    # Converting text to lowercase
    text = text.lower()

    # Removing Extra Spaces
    text = re.sub(r'\s+', ' ', text).strip()

    # Replacing Numbers with a Token
    text = re.sub(r'\d+', '<NUM>', text)

    # Normalize Elongated Words
    text = re.sub(r'(.)\1+', r'\1\1', text) 

    # Expand Contractions (e.g.: weren't => were not)
    text = contractions.fix(text)
    
    # Removing Punctuations and Non-English Charachters
    text = re.sub(r'[^a-z0-9\s]', '', text) 

    # Lemmatization  
    words = text.split()
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]

    # Returning the Cleaned Text 
    cleaned_text = ' '.join(words)
    return cleaned_text
    

## Loading the Model and Vectorizer
with open('models/logistic_regression.pkl', "rb") as file:
    model = pickle.load(file)

with open("models/vectorizer.pkl", "rb") as file:
    vectorizer = pickle.load(file)


## Prediction
email_text = st.text_area("Email Content:")

if st.button("Predict"):

    if email_text:
        processed_text = preprocess_text(email_text)
        vect_text = vectorizer.transform([processed_text])
        
        prediction = model.predict(vect_text)[0]
        prediction_proba = model.predict_proba(vect_text)[0]

        st.subheader("Prediction Result:")
        if prediction == 1:
            st.error("🚫 This email is Spam")
        else:
            st.success("✅ This email is Not Spam")

        st.subheader("Prediction Probabilities:")
        st.write(f"Ham: {prediction_proba[0]:.2f}, Spam: {prediction_proba[1]:.2f}")

    else:
        st.warning("Please enter email content to predict.")