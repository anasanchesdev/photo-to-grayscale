import streamlit as st
from PIL import Image  # biblioteca incluida em streamlit

st.title("Selfie to Grayscale")
st.subheader("A simple program that converts a selfie or photo to grayscale")

with st.expander("Run Camera"):  # botão/ação para iniciar a camera
    # inicia prompt da camera
    image = st.camera_input("Camera")

if image:  # após o usuário permitir o acesso à camera
    # cria objeto de imagem pillow
    image_obj = Image.open(image)

    # converte para cinza
    gray_img = image_obj.convert('L')

    # mostra a imagem em cinza
    st.image(gray_img)
