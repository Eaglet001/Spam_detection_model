# pip install -U stramlit
# pip install -U plotly

# you can run your app by typing : streamlit run app.py
  
import streamlit as st
import pandas as pd

# import model
import joblib
model = joblib.load('model.pkl')

# create title
st.title('Email Spam Detection ')
st.set_page_config(page_title="Email Spam Detection", page_icon="📧", layout="centered")
# create text input for user message
message = st.text_input('Enter your message here')

# create a button to submit the message
Submit = st.button('Predict')

if Submit:
    prediction = model.predict([str(message)])
    if prediction[0] == 1:
        st.error('🚫This message is spam')
    else:
        st.success('✅This message is not spam')

st.balloons()