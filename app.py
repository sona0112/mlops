import streamlit as st
import pandas as pd
from sklearn.preprocessing import StandardScaler
import pickle


st.title('web deployment of medical diagnostic app')
st.subheader('is person diabetic?')
st.set_option('deprecation.showPyplotGlobalUse', False)
df=pd.read_csv('diabetes.csv')
if st.sidebar.checkbox('view data', False):
    st.write(df)
    st.pyplot()
    
if st.sidebar.checkbox('view distributions',False):
    df.hist()
    st.pyplot()

#load pickled model
model=open('rfc.pickle','rb')
clf=pickle.load(model)
model.close()


#get the frondend user input
pregs=st.number_input('Pregnancies',0,17,0), 
glucose=st.slider('Glucose',44,199,44) 
bp=st.slider('BloodPressure',20,140,20) 
skin=st.slider('SkinThickness', 7,99,7)
insulin=st.slider('Insulin',14,850,14)
bmi=st.slider('BMI',18,67,18)
dpf=st.slider('DiabetesPedigreeFunction',0.05,2.50,0.05)
age=st.slider('Age',21,85,21)


#convert user input to model input
data={ 'Pregnancies': pregs,
      'Glucose': glucose,
      'BloodPressure':bp,
      'SkinThickness':skin,
      'Insulin':insulin,
       'BMI':bmi,
      'DiabetesPedigreeFunction':dpf,
      'Age':age
    
    
}
input_data=pd.DataFrame(data)


#get the predictions and print the result
prediction=clf.predict(input_data)[0]
if prediction==1:
    st.subheader('You have Diabetes')
else:
    st.subheader("You don't have Diabetes")
