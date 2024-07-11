import streamlit as st

#--- Page Setup---
about_page = st.Page(
    page="CV_Display.py",
    title="About Me",
    default=True,
)

#--- Navigation Page---
pg= st.navigation(pages=[about_page])

#--- Run Navigation ---
pg.run()