import streamlit as st
import pandas as pd 

st.write("# Spreadsheet Buddy | ineelhere")  
st.write("Explore your data with the power of python! 😃")
st.sidebar.subheader("Upload Zone")
file_u = st.sidebar.file_uploader(label="Please upload the spreadsheet (.xls or .xlsx)")

def multiple_sheet(df):
    st.write("I noticed your file has multiple sheets.")
    sheet = st.selectbox(" Please select the sheet you would like to work on now.", df.sheet_names)
    df = pd.read_excel(file_u, sheet)
    return(df)

def simple_display(df):
    st.write("  \n   Here is your untouched file 👇")
    st.dataframe(df)

def nowwhat(df):
    tasklist = ["List the column names in this selection (default)",
                "Basic Description about the data (please verify before using this information)"]
    command = st.selectbox("What would you like to do now? 🤔  \nLet me know by selecting any of the options below! ☑️", tasklist)
    if command == tasklist[0]:
        for i in df.columns:
            st.write(i)
    if command == tasklist[1]:
        st.write(df.describe())

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

st.markdown("`Created by Indraneel Chakraborty`  \n`https://www.linkedin.com/in/indraneelchakraborty/`")
