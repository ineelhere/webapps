import streamlit as st
import difflib
st.write("""
# Version control in 2 code snippets 
**For experimentation purpose only | Indraneel Chakraborty** 
    """)
l1 = st.text_area("Enter the first code snippet")
l2 = st.text_area("Enter the modified code snippet")
l1.strip().splitlines()
l2.strip().splitlines()
l3 = list(set(l1+l2))
st.markdown("## Tracing changes")
for line in difflib.unified_diff(l1, l2, fromfile='file1', tofile='file2', lineterm=''):
    st.write(line)
