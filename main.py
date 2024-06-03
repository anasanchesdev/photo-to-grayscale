import streamlit as st
from PIL import Image
# biblioteca incluida em streamlit

image = st.camera_input("Camera")
print(image)

image_obj = Image.open(image)
gray_img = image_obj.convert("L")
