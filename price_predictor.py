import streamlit as st
import pandas as pd
import numpy as np
import pickle
model=pickle.load(open("price_pipe_update.pkl","rb"))
st.title("Phone Price Predictor")
with st.form("my_form"):
    brand= st.selectbox(
    'select the brand of the phone',
    ('Apple', 'Samsung', 'OnePlus', 'Xiaomi', 'Google', 'Oppo', 'Vivo',
       'Realme', 'Motorola', 'Nokia', 'Sony', 'LG', 'Asus', 'Blackberry',
       'CAT', 'Huawei'))

st.divider() 

  

    storage=st.selectbox(
    'select ram of the phone',
    (32,64,128,256,512))


    st.divider()

    ram=st.selectbox(
    'select ram of the phone',
    ( 2,4,6,  8, 12, 16))


    st.divider()

    screen_size= st.slider('Scree size in "inches"',min_value=1.0,max_value=10.0,value=5.0,step=0.1)


    st.divider()

    battery=st.slider('battery in "mah"',min_value=1000,max_value=10000,value=5000,step=500)

    st.divider()

    first=st.number_input("enter mp of first camera",value=0)
    second=st.number_input("enter mp of second  camera",value=0)
    

    st.divider()

    user_data=np.array([[brand,storage,ram,screen_size,battery,first,second,0]])
    result=model.predict(user_data)

    submitted = st.form_submit_button("Submit")
    if submitted:
        st.title("{} inr".format(round(result[0]*80)))
