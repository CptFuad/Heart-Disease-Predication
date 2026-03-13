import streamlit as st
import joblib
import numpy as np

model= joblib.load('models/model.pkl')

st.title('Heart Disease Predication System')

age=st.number_input('Age')
chol=st.number_input('Cholestrol')
bp=st.number_input('Blood Pressure')

if st.button('Predict'):
    data=np.array([[age, chol, bp]])
    result=model.predict(data)

    if result[0]==1:
        st.error('High Risk')
    else:
        st.success('Low Risk')