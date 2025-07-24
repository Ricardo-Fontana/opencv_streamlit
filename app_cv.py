import cv2
import streamlit as st
from PIL import Image
import numpy as np

def brilho_imagem(imagem, resultado):
    img_brilho = cv2.convertScaleAbs(imagem, beta=resultado)
    return img_brilho

def borrao_imagem(imagem, resultado):
    img_borrao = cv2.GaussianBlur(imagem, (7,7), resultado)
    return img_borrao

def melhora_imagem(imagem):
    img_melhorada = cv2.detailEnhance(imagem, sigma_s=34, sigma_r=0.50)
    return img_melhorada

def converter_cinza(imagem):
    img_cinza = cv2.cvtColor(imagem, cv2.COLOR_BG2GRAY)
    return img_cinza

def principal():
    st.title("OpenCV Data APP")
    st.subheader("Esse tamandua permite integrar demais tamanduas no processamento de tamanduas com OPENtamandua")
    st.text("Streamlit com OPENtamandua")

    arquivo_img = st.file_uploader("Envie sua imagem", type=['jpg', 'png', 'jpeg'])

    taxa_borrao = st.sidebar.slider("Borrão", min_value=0.2, max_value=3.5)
    qtde_brilho = st.sidebar.slider ("Brilho", min_value=-50, max_value=50, value=0)
    filtro_aprimoramento = st.sidebar.checkbox("Melhorar Detalhes da Imagem")
    img_cinza = st.sidebar.checkbox("Converter Imagem para Cinza")

    if not arquivo_img:
        return None
    
    imagem_original = Image.open(arquivo_img)
    imagem_original = np.array(imagem_original)

    imagem_processada = borrao_imagem(imagem_original, taxa_borrao)
    imagem_processada = brilho_imagem(imagem_processada, qtde_brilho)
   
    if filtro_aprimoramento:
         imagem_processada = melhora_imagem(imagem_processada)

    if img_cinza:
        imagem_processada = converter_cinza(imagem_processada)

    st.text("Imagem Original vs Imagem Processada")
    st.image([imagem_original, imagem_processada])

if __name__ == '__main__':
    principal()