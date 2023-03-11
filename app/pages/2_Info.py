from PIL import Image
import requests
import streamlit as st

# ---- MAIN TAB SECTION ----
# emoji cheatsheet: https://www.webfx.com/tools/emoji-cheat-sheet/
st.set_page_config(
    page_title="MSDS 434: Final Project", 
    page_icon=":musical_note:", 
    layout="wide"
    )


# ---- LOAD ASSETS ----
img_nd = Image.open("images/nd_2022.jpg").resize((400, 500))

# ---- HEADER SECTION ----
with st.container():
    st.title("Additional Information")
    st.markdown('''This project was built for MSDS 434 Analytics Application Development Final Project (Part II). The final project consists of building a cloud-native 
    analytics application that is hosted on the Google Cloud Platform (GCP). The GitHub repository for this project with more technical documentation can be 
    [found here](https://github.com/DrakeData/MSDS434-Final_P2).''')
    st.subheader("Project was creatd by Nicholas Drake")
    st.image(img_nd)
    st.markdown("**Contact:** [GitHub](https://github.com/DrakeData) - [LinkedIn](https://www.linkedin.com/in/ndrakedata/) - [Email](mailto:nick@drakedata.io)")
