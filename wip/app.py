import streamlit as st
import pandas as pd 
from simple_display import *
from multiple_sheet import *
from nowwhat import *
from trimdf import *

st.write("# Spreadsheet Buddy | ineelhere")  
st.write("Explore your data with the power of python! 😃")
st.sidebar.subheader("Upload Zone")
file_u = st.sidebar.file_uploader(label="Please upload the spreadsheet (.xls or .xlsx)")

if file_u:
    st.write("Awesome! Your file has been successfully uploaded! 🥳")
    df = pd.ExcelFile(file_u)
    if len(df.sheet_names)!=1:
        df = multiple_sheet(df)
        simple_display(df)
        nowwhat(df)
        st.markdown("**Would you like to trim this data?**")
        response = st.selectbox("Shall we proceed?", ["Click to choose","Yes","Abhi rehne dete hai" ])
        if response == "Yes":
            st.write("Awesome🔥  \nSelect ☑️ the column(s) you would like to keep ")
            trimdf(df)
        if response=="Abhi rehne dete hai":
            st.write("🥺")
    else:
        df = pd.read_excel(file_u)
        simple_display(df)        
        nowwhat(df)
        st.markdown("**Would you like to trim this data?**")
        response = st.selectbox("Shall we proceed?", ["Click to choose","Yes","Abhi rehne dete hai" ])
        if response == "Yes":
            st.write("Awesome🔥 ")
            trimdf(df)
        if response=="Abhi rehne dete hai":
            st.write("🥺")

else:
    st.write("Please click on the ▶️ on the top left corner and upload the file.  \n🔴 *Only .xlsx and .xls files are supported currently*")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("`Created by Indraneel Chakraborty `  \n`https://www.linkedin.com/in/indraneelchakraborty/`")
