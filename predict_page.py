import streamlit as st 
import streamlit.components.v1 as stc
import pickle
import numpy as np
from PIL import Image 


""" def load_model():
    with open('', rb) as file:
        data=pickle.load(file)
    return data


data=load_model()

model_loaded=data['model']
le_country=data['']
le_education=data[]
 """

@st.cache
def load_image(image_file):
	img = Image.open(image_file)
	return img 

def show_predict_page():
    st.title("Software Facebook ADS Insights")
    image_file = st.file_uploader("Upload Image",type=['png','jpeg','jpg'])
    if image_file is not None:
        #To See Details
		#st.write(type(image_file))
		#st.write(dir(image_file))
        file_details = {"Filename":image_file.name,"FileType":image_file.type,"FileSize":image_file.size}
        #st.write(file_details)
        img = load_image(image_file)
        #st.image(img)

        ok=st.button("Calculate Insights")
        if ok:
            st.subheader(f"Results:")
