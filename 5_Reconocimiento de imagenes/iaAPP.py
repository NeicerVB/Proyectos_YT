import numpy as np
import matplotlib.pyplot as plt
import streamlit as st
from PIL import Image
import tensorflow as tf

def main():
    st.title("Clasificador de imagenes")
    st.write("Carga una imagen y obtendrás una predicción de la IA")
    
    file = st.file_uploader("Carga una imagen")
    
    if file:
        image = Image.open(file)
        st.image(image, use_column_width=True)
        
        resized_image = image.resize((32,32))
        img_array = np.array(resized_image) / 255
        img_array = img_array.reshape((1,32,32,3))
        
        model = tf.keras.models.load_model("./cifar10_model.h5")
        
        predictions = model.predict(img_array)
        
        cifar10_classes = ['airplane', 'automobile', 'bird', 'cat', 'dog', 'deer', 'frog', 'horse', 'ship', 'truck']
        
        fig, axes = plt.subplots()
        y_pos = np.arange(len(cifar10_classes))
        axes.set_yticks(y_pos)
        axes.set_yticklabels(cifar10_classes)
        axes.barh(y_pos, predictions[0], align='center')
        axes.set_xlabel('Probabilidad')
        axes.set_title('Predicciones')
        st.pyplot(fig)
    else: 
        st.text("Por favor, carga una imagen")
        