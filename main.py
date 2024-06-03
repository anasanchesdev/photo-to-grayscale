import streamlit as st
from PIL import Image  # biblioteca incluida em streamlit


def process_image(image):
    image_obj = Image.open(image)  # cria objeto de imagem pillow
    gray_img = image_obj.convert('L')  # converte para cinza
    st.image(gray_img)  # mostra a imagem em cinza


st.title("Selfie to Grayscale")
st.subheader("A simple program that converts a selfie or photo to grayscale")
uploaded_image = st.file_uploader("Upload Image")

with st.expander("Run Camera"):  # botão/ação para iniciar a camera
    # inicia prompt da camera
    camera_image = st.camera_input("Camera")

if camera_image:  # após o usuário permitir o acesso à camera
    process_image(camera_image)

elif uploaded_image:  # após o usuário fazer upload de alguma foto
    process_image(uploaded_image)
