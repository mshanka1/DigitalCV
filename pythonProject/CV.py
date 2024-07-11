import os
import streamlit as st
import streamlit.components.v1 as components
from PIL import Image
# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Shankar Manne"
PAGE_ICON = ":wave:"
NAME = "Shankar Manne"
DESCRIPTION = """
Senior Embedded Software Engineer with 19 Yrs in 
High and Low Level application design and development.
"""
EMAIL = "mshanka1@gmail.com"
#cv_dir_path = os.path.dirname(os.path.realpath(__file__))
cv_html_filepath = "./CVHTML/cv.html"
profile_pic = "./CV/Photo.jpg"
#if os.path.isfile(cv_html_filepath):
print("file is there")
#arr = os.listdir(cv_doc_filepath)
#cv_doc_filepath += arr[0]
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
#profile_pic = Image.open(profile_pic)
# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.write("📫", EMAIL)
    st.write('\n')
    st.subheader("About my Experience & Qulifications")
    #with open(cv_html_filepath, 'r') as f:
        #html_data = f.read()
    #st.components.v1.html(html_data, scrolling=True, height=500)
    #b = open(cv_html_filepath, 'r')
    #st.html(b.read())
    #b.close()
#else:
    #import mammoth
    #cv_doc_filepath = os.path.join(cv_dir_path, 'CV\\')
    #arr = os.listdir(cv_doc_filepath)
    #cv_doc_filepath+=arr[0]
    #print(cv_doc_filepath)
    #f = open(cv_doc_filepath, 'rb')
    #b = open(cv_html_filepath, 'wb')
    #document = mammoth.convert_to_html(f)
    #b.write(document.value.encode('utf8'))
    #f.close()
    #b.close()
