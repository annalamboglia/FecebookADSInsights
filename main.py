import streamlit as st
from predict_page import show_predict_page
from about import show_page_about

menu=["Predict", "About"]
page = st.sidebar.selectbox("Menu", menu)

if page == "Predict":
    show_predict_page()

else:
    show_page_about()