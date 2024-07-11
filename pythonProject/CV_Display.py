import streamlit as st
import os

fileDir = os.path.dirname(os.path.realpath('__file__'))
image_str = os.path.join(fileDir, 'pythonProject/CV/Photo.png')
col1, col2 = st.columns(2,gap='small', vertical_alignment="center")
with col1:
    st.image(image_str, width=230)
with col2:
    st.title("Shankar Manne", anchor=False)
    st.write(
        "Senior Embedded Software Engineer with 19 Yrs of exp in developing both "
        "Low level and High Level applications."
    )