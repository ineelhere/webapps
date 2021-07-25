import streamlit as st
import pandas as pd 
import numpy as np

def nowwhat(df):
    tasklist = ["List the column names in this selection (default)",
                "Basic Description about the data (please verify before using this information)",
                "Explore empty cells (missing values) in your data"]
    st.markdown("**What would you like to do now? 🤔**")
    command = st.selectbox("Let me know by selecting any of the options below! ☑️", tasklist)
    if command == tasklist[0]:
        for i in df.columns:
            st.write(i)
    if command == tasklist[1]:
        st.write(df.describe())
        st.bar_chart(df.describe())
    if command == tasklist[2]:
        st.write("Count the number of empty data points in each column")
        st.dataframe(df.isnull().sum())
        st.bar_chart(data=df.isnull().sum())
