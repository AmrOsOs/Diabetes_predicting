import pickle
import streamlit as st
import pandas as pd

#Upload Data

data = pickle.load(open(r'C:\Users\meroo\Downloads\Diabetes_Prediction.sav','rb'))
st.title('Diabetes Perdiction Web App')
st.info('Easy App For Diabetes Perdicition ')
st.sidebar.header('Feature Selection')
Pregnancies = st.text_input('Pregnancies')
Glucose = st.text_input('Glucose')
BloodPressure = st.text_input('BloodPressure')
SkinThickness = st.text_input('SkinThickness')
Insulin = st.text_input('Insulin')
BMI = st.text_input('BMI')
DiabetesPedigreeFunction = st.text_input('DiabetesPedigreeFunction')
Age = st.text_input('Age')

df = pd.DataFrame({'Pregnancies' : [Pregnancies] , 'Glucose' : [Glucose] , 'BloodPressure' : [BloodPressure] , 
              'SkinThickness' : [SkinThickness] , 'Insulin' : [Insulin] , 'BMI' : [BMI] ,
               'DiabetesPedigreeFunction' : [DiabetesPedigreeFunction] , 'Age' : [Age] }, index=[0])

con = st.sidebar.button('Confirm')

if con:
   result =  data.predict(df)
   if result == 0:
      st.sidebar.write('The Patient is Clear')
      st.sidebar.image('https://img.freepik.com/free-vector/healthy-people-carrying-different-icons_53876-66139.jpg?semt=ais_hybrid&w=740&q=80',width=200)
   else:
      st.sidebar.write('Patient Has disease')
      st.sidebar.image('https://cdn.scope.digital/Images/Articles/diyabet-nedir-seker-hastaligi-belirtileri-nelerdir-6792354.jpg?tr=w-630,h-420',width=200)
      

