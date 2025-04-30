import streamlit as st
import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

# Load trained model and vectorizer
@st.cache_resource
def load_model():
    model = joblib.load("svm_model.pkl")
    vectorizer = joblib.load("tfidf_vectorizer.pkl")
    return model, vectorizer

# Streamlit UI
st.title("📩 SMS Spam Detection")
st.write("Enter a message below to check whether it's **Spam** or **Ham**.")

user_input = st.text_area("Type your message here...")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter a message to classify.")
    else:
        model, vectorizer = load_model()
        input_tfidf = vectorizer.transform([user_input])
        prediction = model.predict(input_tfidf)[0]
        label = "🚫 Spam" if prediction == 1 else "✅ Ham"
        st.success(f"The message is: **{label}**")
