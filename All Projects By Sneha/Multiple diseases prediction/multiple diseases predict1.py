# -*- coding: utf-8 -*-
"""
Created on Mon Jan  1 14:24:52 2024

@author: sneha
"""

import pickle
import streamlit as st 
from streamlit_option_menu import option_menu

#loading the file from saved folder

diabetes_model = pickle.load(open("C:/Users/sneha/Desktop/All Projects By Sneha/Multiple diseases prediction/saved file/diabetes_model.sav",'rb'))
Heart_model = pickle.load(open("C:/Users/sneha/Desktop/All Projects By Sneha/Multiple diseases prediction/saved file/heartdisease_model.sav",'rb'))
Parkinson_model = pickle.load(open("C:/Users/sneha/Desktop/All Projects By Sneha/Multiple diseases prediction/saved file/Parkinson_disease_model.sav",'rb'))

#creating the sidebar model

with st.sidebar:
    
    selected = option_menu('Multiple Disease Prediction System ',
                           ['Diabetes Prediction',
                            'Heart Prediction',
                            'Parkinson Prediction'],
                           icons= ["activity","heart","person"],
                           default_index = 0)
    
#Diabetes prediction page

if(selected == 'Diabetes Prediction'):
    
    #page title
    st.title('Diabetes Prediction Using ML')
    col1,col2,col3 = st.columns(3)
    
    #getting the input data from the user
    with col1:
        Pregnancies = st.text_input('Number of Pregnancies')
    with col2:
        Glucose = st.text_input('Glucose Level')
    with col3:
        BloodPressure = st.text_input('Blood Pressure Value')
    with col1:
        SkinThickness = st.text_input('Skin Thickness Value')
    with col2:
        Insulin = st.text_input('Insulin Level')
    with col3:
        BMI = st.text_input('BMI Value')
    with col1:
        DiabetesPedigreeFunction = st.text_input('Diabetes Pedigree Function Value')
    
    with col2:
        Age = st.text_input('Age of the Person')
    
    #code for prediction
    diab_dignosis = ''
    
    #Creating button for prediction
    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict([[Pregnancies, Glucose,BloodPressure,SkinThickness,Insulin,BMI, DiabetesPedigreeFunction,Age ]])
        
        if (diab_prediction[0]==1):
            diab_dignosis = "The person is Diabetic"
        else:
            diab_dignosis = "The person is not Diabetic"
    st.success(diab_dignosis)

if (selected == 'Heart Prediction'):
    #page tile
    st.title("Heart Prediction Using Ml")
    
if (selected == 'Parkinson Prediction'):
    #page tile
    st.title("Parkinson Prediction Using Ml")
    