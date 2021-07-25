import streamlit as st
import pandas as pd 
def nowwhat(df):
    tasklist = ["List the column names in this selection (default)",
                "Basic Description about the data (please verify before using this information)"]
    command = st.selectbox("What would you like to do now? 🤔  \nLet me know by selecting any of the options below! ☑️", tasklist)
    if command == tasklist[0]:
        for i in df.columns:
            st.write(i)
    if command == tasklist[1]:
        st.write(df.describe())