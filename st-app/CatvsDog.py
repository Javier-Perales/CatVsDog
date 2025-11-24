import streamlit as st
from tensorflow import keras
# from keras.models import load_model  
from PIL import Image, ImageOps  
import numpy as np

# Configuración de la página
st.set_page_config(page_title="Reconocimiento Perros vs Gatos", page_icon="🐾")

st.title("🐶 Detector de Mascotas 🐱")
st.write("Usa la cámara para saber si es un perro o un gato.")

# CARGAMOS EL MODELO Y ETIQUETAS
# Usamos cache para que no se cargue cada vez que detecta un movimiento
@st.cache_resource
def carga_modelo():
    # Cargamos el modelo
    modelo = keras.models.load_model("st-app/keras_model.h5", compile=False)
    # Carga las etiquetas de las clases
    clases = open("st-app/labels.txt", "r").readlines()
    return modelo, clases




# WIDGET DE CÁMARA
imagen_camara = st.camera_input("Haz una foto")
