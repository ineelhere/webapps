import streamlit as st
import difflib
st.write("""
# Version control in 2 code snippets 
**For experimentation purpose only | Indraneel Chakraborty** 
    """)
l1 = st.text_area("Enter the first list of data. One data per line")
l2 = st.text_area("Enter the second list of data. One data per line")
l1.strip().splitlines()
l2.strip().splitlines()
l3 = list(set(l1+l2))
st.markdown("## Tracing changes")
for line in difflib.unified_diff(l1, l2):
    st.write(line)
