import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

selected = st.sidebar.selectbox('Selecione a página', ['Classificador','DashBoard'])


if(selected == 'Classificador'):
    st.title('Clasificador')
else:
    st.title('DashBoard')

    for i in range(3):
        st.subheader('Avaliações por categoria de produto')
        st.image(Image.open(f'images/{i+1}.png'))
        st.markdown('')
    st.subheader('Avaliação do modelo')
    st.write("A avaliação do modelo para a opção Almoço calculada através do método r2 score foi de 0.726032691037806")
    st.write("A avaliação do modelo para a opção Janta calculada através do método r2 score foi de 0.7264856877990088")