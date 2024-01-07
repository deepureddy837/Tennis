import streamlit as st
import pandas as pd
import numpy as np
import pickle

Outlook ={
"Overcast":0,"Rain":1,"Sunny":2,}
Temperature ={
"Cool":0,"Hot":1,"Mild":2,}
Humidity ={
"High":0,"Normal":1,}
Wind ={
"Strong":0,"Weak":1,}


model=pickle.load(open('log_model.pkl','rb'))
#creating a function to accept inputs and creating a 2d array and predicting the result
def predict(outlook,temperature,humidity,wind):
    #function to accept values
    selected_outlook=Outlook[outlook]
    selected_temperature=Temperature[temperature]
    selected_humidity=Humidity[humidity]
    selected_wind=Wind[wind]
    user_input=np.array([[selected_outlook,selected_temperature,selected_humidity,selected_wind]])
    result=model.predict(user_input)[0]
    if result==1:
        return "Yes you can play tennis"
    else:
        return "No you can't play tennis"
if __name__=="__main__":
    st.header("Play Tennis or not")
    col1,col2=st.columns([2,1])
    outlook=col1.selectbox("Select Outlook:",list(Outlook.keys()))
    temperature=col1.selectbox("Select Temperatute:",list(Temperature.keys()))
    humidity=col1.selectbox("Select Humidity:",list(Humidity.keys()))
    wind=col1.selectbox("Select Wind:",list(Wind.keys()))
    result=predict(outlook,temperature,humidity,wind)
    submit_button=st.button("Predict")
    if submit_button:
        larger_text=f"<h2 style='color:white;'>{result}</h2>" 
        st.markdown(larger_text,unsafe_allow_html=True)




    



