import streamlit as st
import pandas as pd 
import base64

def trimdf(df):
	choices = []
	for i in df.columns:
		agree = st.checkbox(i)
		if agree:
			choices.append(i)

	st.dataframe(df[choices])

	csv = df.to_csv(index=False)
	b64 = base64.b64encode(csv.encode()).decode()  # some strings <-> bytes conversions necessary here
	href = f'<a href="data:file/csv;base64,{b64}">Download the above as a CSV File</a> (right-click and save as &lt;some_name&gt;.csv)'
	st.markdown(href, unsafe_allow_html=True)
