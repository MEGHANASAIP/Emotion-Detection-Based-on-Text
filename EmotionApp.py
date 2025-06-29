import streamlit as st
import joblib

# Load your trained model
model = joblib.load("model.pkl")

# Emotion label mapping
label_to_emotion = {
    0: '😠 Anger',
    1: '😊 Joy',
    2: '😨 Fear'
}

# Page config
st.set_page_config(
    page_title="Emotion Classifier",
    page_icon="💬",
    layout="centered"
)

# Custom CSS for styling
st.markdown("""
    <style>
        .main-title {
            font-size: 36px;
            font-weight: bold;
            color: #1f77b4;
        }
        .subheader {
            font-size: 20px;
            margin-bottom: 10px;
            color: #444;
        }
        .result-box {
            background-color: #f0f2f6;
            padding: 20px;
            border-radius: 10px;
            font-size: 22px;
            font-weight: bold;
            color: #333;
        }
    </style>
""", unsafe_allow_html=True)

# App title
st.markdown('<p class="main-title">💬 Emotion Detection App</p>', unsafe_allow_html=True)
st.markdown('<p class="subheader">Enter a sentence and find out the predicted emotion!</p>', unsafe_allow_html=True)

# Text input
text = st.text_area("Type your sentence here 👇", height=150, placeholder="E.g. I'm feeling very nervous about the exam...")

# Predict button
if st.button("🔍 Predict Emotion"):
    if text.strip() == "":
        st.warning("⚠️ Please enter a sentence.")
    else:
        # Predict
        prediction = model.predict([text])[0]
        emotion = label_to_emotion[prediction]

        # Display result
        st.markdown(f'<div class="result-box">Predicted Emotion: {emotion}</div>', unsafe_allow_html=True)

# Optional footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit", unsafe_allow_html=True)
