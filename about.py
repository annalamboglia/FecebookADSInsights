import streamlit as st

def show_page_about():
    st.title("About")
    st.subheader("Founders")
    #[this is a text link](upload://7FxfXwDqJIZdYJ2QYADywvNRjB.png)
    #[![this is an image link](upload://7FxfXwDqJIZdYJ2QYADywvNRjB.png)]
    st.info("[Francesco Ferraro] (https://www.linkedin.com/in/francesco-ferraro-002ab7107/)")
    st.info("[Antonio Furioso] (https://www.linkedin.com/in/antoniofurioso/)")
    st.info("[Anna Lamboglia] (https://www.linkedin.com/in/annalamboglia/)")