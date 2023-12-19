import streamlit as st
import pandas as pd
import numpy as np
import pickle

def convert_to_words(num):  
    if num == 0:  
        return "zero"  
    ones = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]  
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]  
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]  
    words = ""  
    if num>= 1000:  
        words += ones[num // 1000] + " thousand "  
num %= 1000  
    if num>= 100:  
        words += ones[num // 100] + " hundred "  
num %= 100  
    if num>= 10 and num<= 19:  
        words += teens[num - 10] + " "  
num = 0  
elifnum>= 20:  
        words += tens[num // 10] + " "  
num %= 10  
    if num>= 1 and num<= 9:  
        words += ones[num] + " "  
    return words.strip()


model=pickle.load(open("price_pipe_update.pkl","rb"))
st.title("Phone Price Predictor")
with st.form("my_form"):
    brand= st.selectbox(
    'select the brand of the phone',
    ('Samsung','Apple', 'OnePlus', 'Xiaomi', 'Google', 'Oppo', 'Vivo',
       'Realme', 'Motorola', 'Nokia', 'Sony', 'LG', 'Asus', 'Blackberry',
       'CAT', 'Huawei'))


  

    storage=st.selectbox(
    'select storage of the phone',
    (32,64,128,256,512))


    

    ram=st.selectbox(
    'select ram of the phone',
    ( 2,4,6,  8, 12, 16))


    

    screen_size= st.slider('Scree size in "inches"',min_value=1.0,max_value=10.0,value=5.0,step=0.1)


    

    battery=st.slider('battery in "mah"',min_value=1000,max_value=10000,value=5000,step=100)

    

    first=st.number_input("enter mp of back camera",value=0)
   # second=st.number_input("enter mp of front  camera",value=0)
    

    

    user_data=np.array([[brand,storage,ram,screen_size,battery,first,0,0]])
    result=model.predict(user_data)

    submitted = st.form_submit_button("Predict")
if submitted:
        st.title("Estimated price : {} inr".format(round(result[0]*72)))
        x=round(result[0]*72)
        st.title(convert_to_words(x))
    
    
