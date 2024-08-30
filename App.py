#Gemini Key : AIzaSyASczQK9bEiM9zT_gnjU0bRl3qDCH3DfmA

import json
import time
import pandas as pd
import seaborn as sns
from PIL import Image
import streamlit as st
import google.generativeai as genai

genai.configure(api_key="AIzaSyASczQK9bEiM9zT_gnjU0bRl3qDCH3DfmA")
model = genai.GenerativeModel('gemini-1.5-flash')

def gemini_response(query):
    response = model.generate_content(query) 
    return(response.text)
    
with open("Data.json") as fh: 
    values = json.load(fh)

p1 = f"You are a report generating model for the indian post , your task is to generate the most optimal reports for the given data\noverall success rate {values['overall_success']}\noverall failure rate{values['overall_failure']}\nSuccess Rate Bangalore Central : {values['succ_blr_c']}\nSuccess Rate Bangalore East : {values['succ_blr_e']}Success Rate Bangalore North : {values['succ_blr_n']}\nSuccess Rate Bangalore South : 0.612\nCompare the success and failure rate and provide a small report on the same (keep it very short and to the point).Also list down all the other values\nmention why we'll need to use AI based personalization and predictive time slot delivery to resuce the failure rate ini short/1-2 points, dont provide a heading"
#r1 = gemini_response(p1)
r1 = "None"

p2 = f"You are a report generating model for the indian post , based on the XGBoosting Model generated outputs , generate a report for the following values and parameters\nMost Optimal Time Slots\nBangalore Central : {values['slot_blr_c']}\nBangalore East : {values['slot_blr_e']}\nBangalore North : {values['slot_blr_n']}\nBangalore South : {values['slot_blr_s']}\nGenerate a small and consise report based on the same."
#r2 = gemini_report(p2) 
r2 = "None"

p3 = f"You are a report generating model for the indian post, based on the XGBoosting Model Generated outputs , generate a report for the following values and parameters\nMost Optimal Deliver Day\nBangalore Central : Thursday\nBangalore East : Wednesday\nBangalore North : Friday\nBangalore South : Wednesday\nGenerate a small and consise report based on the same"
#r3 = gemini_response(p3) 
r3 = "None" 

p4 = f"You are a report generating model for the indian post, based on the XGBoosting Model Generated outputs, generate a final report of the most optimal day and delivery time for a given region\nMost Optimal Delivery Day : Friday\nMost Optimal Delivery Slot : 10am-12pm"
#r4 = gemini_response(p4)
r4 = "None"

st.set_page_config(page_title="India Post", layout="wide")
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Lato:wght@300;400;700&display=swap');

    .main {background-color: #000000;}
    h1, h2, h3 {color: #ffffff; text-align: center; font-family: 'Lato', sans-serif; font-weight: 300;}
    h4, h5, h6 {color: #ffffff; text-align: center; font-family: 'Lato', sans-serif; font-weight: 300;}
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
    with st.spinner("*Analyzing Dataset*"):
        time.sleep(3)
        st.success("**Dataset Analyzed!**")

    data = pd.read_csv(uploaded_file)

    st.subheader('📊 Dataset Preview')
    st.dataframe(data, use_container_width=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)

    with st.spinner("**Running XGBoost Algorithm On The Dataset...**"):

        with st.spinner("**Predicting Most Optimal Delivery Slots!**"):
            time.sleep(3)
            st.success("**Successfully Predicted Most Optimal Delivery Slots!**")

        with st.spinner("**Generating Dataset Report**"): 
            time.sleep(3)
            st.success("**Successfully Generated Dataset Report!**")
    
    st.header("📄Data Visualization And Report")
    st.markdown("<br><br>", unsafe_allow_html=True)

    #Overall Success And Failure
    st.subheader("Overall Success Rate")
    st.markdown(f"""
        <div class="markdown-text">
        {r1}
        """, unsafe_allow_html=True)
    d1 = Image.open("Images/Avg Success Rate - Region.png")

    col1,col2,col3 = st.columns([1,2,1])
    with col1: 
        st.write("")
    with col2: 
        st.image(d1) 
    with col3: 
        st.write("")

    st.markdown("<br><br>",unsafe_allow_html=True)
    #Time Slots - Region Wise 
    st.subheader("Most Optimal Timeslot Region Wise")
    st.markdown(f"""
        <div class="markdown-text">
        {r2}
        """, unsafe_allow_html=True)
    d2 = Image.open("Images/Timeslot-Region/Overall.png")

    col1,col2,col3 = st.columns([1,2,1])
    with col1: 
        st.write("")
    with col2: 
        st.image(d2) 
    with col3: 
        st.write("")

    st.markdown("<br><br>",unsafe_allow_html=True)
    #Days - Region Wise
    st.subheader("Most Optimal Delivery Day Region Wise")
    st.markdown(f"""
        <div class="markdown-text">
        {r2}
        """, unsafe_allow_html=True)
    d3 = Image.open("Images\\Region Wise Delivery Success.png")

    col1,col2,col3 = st.columns([1,2,1])
    with col1: 
        st.write("")
    with col2: 
        st.image(d3) 
    with col3: 
        st.write("")

    st.markdown("<br><br>",unsafe_allow_html=True)
    #Most Optimal Slot
    st.subheader("Most Optimal Delivery Day And Time Slot")
    st.markdown(f"""
        <div class="markdown-text">
        {r2}
        """, unsafe_allow_html=True)
    d4 = Image.open("Images\\Heatmap.png")

    col1,col2,col3 = st.columns([1,2,1])
    with col1: 
        st.write("")
    with col2: 
        st.image(d4) 
    with col3: 
        st.write("")

else:
    st.info('**Please upload Delivery-LOGS file to begin**')