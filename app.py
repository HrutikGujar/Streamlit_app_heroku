# -*- coding: utf-8 -*-
"""
Created on Mon Sep 30 23:27:02 2024

@author: hp
"""

import numpy as np
import streamlit as st
import pickle
from streamlit_option_menu import option_menu

with open("SVM_dia.pkl", "rb") as file:
    diabetes_model = pickle.load(file)
with open("parkinsons.pkl", "rb") as file:
    parkinsons_model = pickle.load(file)
with open("heart.pkl", "rb") as file:
    heart_model = pickle.load(file)


with st.sidebar:
    selected =option_menu("Multiplt Disease prediction system",
                          ["Diabetes prediction",
                          "Heart Disease prediction",
                          "Parkinsons prediction"],
                          icons=['activity','heart','person'],
                          default_index= 0)
if (selected == "Diabetes prediction"):
    
    st.title("Diabetes prediction using ML")
    
    col1,col2,col3 =st.columns(3)
    
    with col1:
        Pregnancies = st.number_input('Number of Pregnancies', min_value=0, value=None)
    with col2:
        Glucose = st.number_input("Glucose Level", min_value=0.0, value=None)
    with col3:
        BloodPressure = st.number_input("Blood Pressure Value", min_value=0.0, value=None)
    with col1:
        SkinThickness = st.number_input("Skin Thickness Value", min_value=0.0, value=None)
    with col2:
        Insulin = st.number_input("Insulin Level", min_value=0.0, value=None)
    with col3:
        BMI = st.number_input("BMI Value", min_value=0.0, value=None)
    with col1:
        DiabetesPedigreeFunction = st.number_input("Diabetes Pedigree Function Value", min_value=0.0, value=None)
    with col2:
        Age = st.number_input("Age", min_value=0, value=None)
 
    
    diab_diagnosis = ''
    
    if st.button('Diabetes Test Prediction'):
        input_data = [Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]
        
        if None in input_data:
            st.error("Please fill in all fields before making a prediction.")
        else:
            diab_prediction =diabetes_model.predict([input_data])
        
        
            if (diab_prediction[0]==1):
                diab_diagnosis ="The person is diabetic"
            else:
                diab_diagnosis ="The person is not diabetic"
    st.success(diab_diagnosis)     
        
if(selected == "Heart Disease prediction"):
    
    st.title("Heart prediction using ML")
    
    col1,col2,col3 =st.columns(3)
    
    with col1:
        age =st.number_input("Age",value=None)
    with col2:
        sex =st.number_input("Sex",value=None)
    with col3:
        cp =st.number_input("Chest pain type",value=None)
    with col1:
        trestbps =st.number_input("Resting Blood Pressure",value =None)
    with col2:
        chol =st.number_input("Serum Cholestoral in mg/dl",value =None)
    with col3:
        fbs = st.number_input("Fasting Blood Sugar > 120 mg/dl",value =None)
    with col1:
        restecg = st.number_input('Resting Electrocardiographic results',value =None)
    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',value =None)
    with col3:
        exang = st.number_input('Exercise Induced Angina',value =None)
    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',value =None)
    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',value =None)
    with col3:
        ca = st.number_input('Major vessels colored by flourosopy',value =None)
    with col1:
        thal = st.number_input('thal: 0 = normal; 1 = fixed defect; 2 = reversable defect',value =None)
    
    
    heart_diagnosis =''
    
    if st.button("Heart Disease Test Prediction"):
        input_data_h =[age, sex, cp, trestbps, chol, fbs, restecg, thalach,exang, oldpeak, slope, ca, thal]
        
        if None in input_data_h:
            st.error("Please fill in all fields before making a prediction.")
        else:
            heart_prediction =heart_model.predict([input_data_h])
            
            if (heart_prediction[0]==1):
                heart_diagnosis='The person is having heart disease'
            else:
                heart_diagnosis='The person does not have any heart disease'
    st.success(heart_diagnosis)
            
   
        
if(selected == "Parkinsons prediction"):
    
    st.title("Parkinsons prediction using ML")
    
    
    #['name', 'MDVP:Fo(Hz)', 'MDVP:Fhi(Hz)', 'MDVP:Flo(Hz)', 'MDVP:Jitter(%)',
       #'MDVP:Jitter(Abs)', 'MDVP:RAP', 'MDVP:PPQ', 'Jitter:DDP',
       #'MDVP:Shimmer', 'MDVP:Shimmer(dB)', 'Shimmer:APQ3', 'Shimmer:APQ5',
       #'MDVP:APQ', 'Shimmer:DDA', 'NHR', 'HNR', 'status', 'RPDE', 'DFA',
       #'spread1', 'spread2', 'D2', 'PPE'],
       
    col1,col2,col3,col4,col5 =st.columns(5)   
    
    with col1:
        fo = st.text_input('MDVP:Fo(Hz)')
        
    with col2:
        fhi= st.text_input('MDVP:Fhi(Hz)')          
        
    with col3:
        flo = st.text_input('MDVP:Flo(Hz)')   
        
    with col4:
        Jitter_percent = st.text_input('MDVP:Jitter(%)')
  
    with col5:
        Jitter_Abs  = st.text_input('MDVP:Jitter(Abs)')

    with col1:
        RAP = st.text_input('MDVP:RAP')
     
    with col2:
        PPQ = st.text_input('MDVP:PPQ')
    
    with col3:
        DDP = st.text_input('Jitter:DDP')
 
    with col4:
        Shimmer = st.text_input('MDVP:Shimmer')
      
    with col5:
        Shimmer_dB = st.text_input('MDVP:Shimmer(dB)')
    
    with col1:
        APQ3 = st.text_input('Shimmer:APQ3')

    with col2:
        APQ5 = st.text_input('Shimmer:APQ5')
 
    with col3:
        APQ = st.text_input('MDVP:APQ')
        
    with col4:
        DDA = st.text_input('Shimmer:DDA')

    with col5:
        NHR = st.text_input('NHR')
    with col1:
        HNR = st.text_input('HNR')
        
    with col2:
        RPDE = st.text_input('RPDE')

    with col3:
        DFA = st.text_input('DFA')
        
    with col4:
        spread1 = st.text_input('spread1')
        
    with col5:
        spread2 = st.text_input('spread2')

    with col1:
        D2 = st.text_input('D2')
        
    with col2:
        PPE = st.text_input('PPE')
        
        
    perkinsons_diagnosis =''
    
    if st.button("Parkinson Test Result"):
        try:
            input_data_p = [
                float(fo), float(fhi), float(flo), float(Jitter_percent),
                float(Jitter_Abs), float(RAP), float(PPQ), float(DDP),
                float(Shimmer), float(Shimmer_dB), float(APQ3),
                float(APQ5), float(APQ), float(DDA), float(NHR),
                float(HNR), float(RPDE), float(DFA), float(spread1),
                float(spread2), float(D2), float(PPE)
            ]
            
            parkinsons_prediction = parkinsons_model.predict([input_data_p])
            
            if (parkinsons_prediction[0] == 1):
                perkinsons_diagnosis = 'The person is likely to have Parkinson\'s disease'
            else:
                perkinsons_diagnosis = 'The person is likely not to have Parkinson\'s disease'
        
        except ValueError:
            st.error("Please ensure all fields are filled with valid numbers.")
    
    st.success(perkinsons_diagnosis)
            
        
        
        

            
        
    