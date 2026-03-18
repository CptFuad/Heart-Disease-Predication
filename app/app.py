import streamlit as st
import joblib
import numpy as np

model= joblib.load('../models/model.pkl')

st.title('Heart Disease Predication System')

age=st.number_input('Age')
sex=st.number_input('Sex')
cp=st.number_input('Chest Pain Type')
trestbps=st.number_input('Resting Blood Pressure')
chol=st.number_input('Cholestrol')
fbs=st.number_input('Fasting Blood Sugar')
restecg=st.number_input('Resting Electrocardiographic Results (ECG)')
thalach=st.number_input('Maximum Heart Rate Achieved')
exang=st.number_input('Exercise Induced Angina')
oldpeak=st.number_input('ST Depression induced by exercise relative to rest')
slope=st.number_input('Slope of the Peak Exercise ST Segment')
ca=st.number_input('Number of Major Vessels')
thal=st.number_input('Thalassemia')


if st.button('Predict'):
    data=np.array([[age,sex,cp,trestbps,chol, fbs, restecg, thalach,exang,oldpeak, slope, ca,thal]])
    result=model.predict(data)

    if result[0]==1:
        st.error('High Risk')
    else:
        st.success('Low Risk')