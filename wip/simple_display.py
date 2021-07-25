import streamlit as st
import pandas as pd 
def simple_display(df):
    st.write("  \n   Here is your untouched file 👇")
    st.dataframe(df)
