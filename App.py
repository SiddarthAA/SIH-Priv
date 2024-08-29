#Gemini Key : AIzaSyASczQK9bEiM9zT_gnjU0bRl3qDCH3DfmA

import streamlit as st
import pandas as pd
import time
from PIL import Image
import seaborn as sns

st.set_page_config(page_title="India Post", layout="wide")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');

    .main {background-color: #000000;}
    h1, h2 {color: #ffffff; text-align: center; font-family: 'Lato', sans-serif; font-weight: 300;}
    .markdown-text {font-family: 'Lato', sans-serif; font-weight: 300; color: #ffffff;}
    .st-bar-chart, .st-line-chart, .st-heatmap {background-color: #ffffff; padding: 10px; border-radius: 10px; margin-bottom: 20px;}
    .st-dataframe {background-color: #ffffff; border-radius: 10px; padding: 10px; margin-bottom: 20px;}
    .chart-container {padding: 10px;}
            
    .stFileUploader {font-family: 'Lato', sans-serif; color: #ffffff; background-color: #333333; border: 1px solid #ffffff; border-radius: 5px; padding: 10px;}
    .stTextInput, .stSelectbox, .stMultiselect, .stNumberInput, .stCheckbox, .stRadio, .stSlider, .stTextArea {font-family: 'Lato', sans-serif;}

    </style>
    """, unsafe_allow_html=True)

st.title('📦 India Post : AI-Driven Personalized Delivery Experience')

banner_image = Image.open("Banner.png") 
banner_image = banner_image.resize((1920, 400))
st.image(banner_image, use_column_width=True)  

st.markdown("""
    <div class="markdown-text">
    This dashboard visualizes delivery data across different regions, time slots, and days of the week. 
    Explore the insights using the interactive charts below.
    </div>
    """, unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

uploaded_file = st.file_uploader("Upload Your Delivery Log To Begin! 🧾", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)

    st.subheader('📊 Dataset Preview')
    st.dataframe(data, use_container_width=True)



    with st.spinner("## **Running eXtreme Boosing**"): 
        time.sleep(3)
        st.markdown("###### **Hello**")
    
else:
    st.info('**Please upload a CSV file to begin**')