import streamlit as st
import pandas as pd 
def multiple_sheet(df):
    st.write("We noticed your file has multiple sheets.")
    sheet = st.selectbox(" Please select the sheet you would like to work on now.", df.sheet_names)
    df = pd.read_excel(file_u, sheet)
    return(df)