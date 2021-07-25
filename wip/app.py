import streamlit as st
import pandas as pd 
from simple_display import *
from multiple_sheet import *
from nowwhat import *

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
    else:
        df = pd.read_excel(file_u)
        simple_display(df)        
        nowwhat(df)

else:
    st.write("Please click on the ▶️ on the top left corner and upload the file.  \n🔴 *Only .xlsx and .xls files are supported currently*")

hide_streamlit_style = """
<style>
#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
</style>

"""
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.markdown("`Created and maintained by Indraneel Chakraborty`  \n`https://www.linkedin.com/in/indraneelchakraborty/`")
