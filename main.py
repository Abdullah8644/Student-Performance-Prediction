import streamlit as st
from joblib import load
import numpy as np

# Load the trained model
with open('model.joblib', 'rb') as file:
    model = load(file)

def predict_performance(features):
    # Predict using the loaded model
    prediction = model.predict([features])
    return prediction[0]

st.title('Student Performance Predictor')

# Input features
hours = st.number_input('Hours Studied',placeholder="Write hours for study from 1 to 10",value=None)
Previous_Scores = st.number_input('Previous Scores', value=None,placeholder="Write score from 1 to 100")
Sleep_Hours	 = st.number_input('Sleep Hours	', value=None,placeholder="hours between 4 to 9")
SQPP= st.number_input('Sample Question Papers Practiced', value=None,placeholder="between 0 to 9")
y_LA= st.number_input('Do Extracurricular Activities', value=None,placeholder="0 for false 1 for True")





features = [hours, Previous_Scores, Sleep_Hours, SQPP, y_LA,]





# Button to make prediction
try:
    if st.button('Predict'):
        result = predict_performance(features)
        
        st.write(f'Predicted Performance: {result:.2f}')
except Exception as e:
    print(e)
    st.write("Please fill all values")