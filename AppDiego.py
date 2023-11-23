import datetime
import time
import pandas as pd
import streamlit as st
from PIL import Image

@st.cache
def run_fun(n: int) -> list:
    return range

st.title('Título: Analítica de Datos')

st.header('Este es un header')
st.subheader('Este es un subheader')

st.text('Texto: Hola Streamlit!')
st.markdown('#Este es un markdown h1 \n ##Este es un h2 \n ###Este es un h3')
st.header('Colores de texto y mensajes de error')
st.info('Información!')
st.warning('Warning')
st.error('Error')
st.exception('NameError("no está definido")')
st.header('Obtener información de ayuda de Python')
st.help(range)
st.header('Widgets:')
st.subheader('Checkbox')

if st.checkbox('Show/Hide'):
    st.text('Mostrar u ocultar Widget')
    st.subheader('Radio buttons')
    
status = st.radio('Cuál es tu estatus?', ('Activo','Inactivo'))

if status == 'Activo':
    st.success('Estás activo')
else:
    st.warning('Inactivo')
    st.subheader('Selectbox')

occupation = st.selectbox('Tu ocupación', 
                          ['Programador', 'Científico de datos', 'BI', 'Ingeniero de datos'])
st.write('Opción seleccionada:', occupation)
st.subheader('MultiSelect')

location = st.multiselect('Dónde trabajas?',
                         ('México', 'Nueva York', 'Guadalajara', 'Monterrey', 'Nepal', 'Buenos Aires', 'Caracas'))

st.write('Selección:', len(location), 'locaciones')
st.subheader('Slider')

level = st.slider('Cuál es tu nivel?', 1, 5)
st.write('Nivel:', level)
st.subheader('Buttons')

if st.button('Acerca'):
    st.text('Streamlit es genial')
else:
    st.text('')
st.header('Cómo recibir una entrada y procesarla en Streamlit?')
st.subheader('Recibiendo texto de entrada')
# Recibiendo texto de entrada
firstname = st.text_input('Ingresa tu nombre:')
if st.button('Aceptar'):
    result = firstname.title()
    st.success(result)
st.subheader('Área de texto')
message = st.text_area('Escribe tu mensaje:')
if st.button('Aceptar1'):
    result = message.title()
    st.success(result)
st.subheader('Entrada de fecha')
# Entrada de fecha
today = st.date_input('Hoy es:', datetime.datetime.now())
st.text(f'{today}')
st.subheader('Entrada de tiempo')
# Time
the_time = st.time_input('La hora es:', datetime.time())
st.text(f'{the_time}')
st.text('Trabajando con imágenes, audio y video')
# Imágenes
st.subheader('Archivo de imagen')
img = Image.open('LogoHorizontal.png')
st.image(img, width=300, caption='Simple imagen')

st.header('Otras opciones que permite la función write')
# Writing text/super function
st.subheader('Texto con write')
st.write('Texto con write')
st.write(range(10))
st.header('Mostrando código puro y JSON')
st.subheader('Código puro')
st.code('import numpy as np')
with st.echo():
    # This will also be shown
    df = pd.DataFrame()
st.subheader('Desplegando JSON')
st.text('Mostrando JSON')
st.json({'Nombre':'John', 'Apellido':'Smith', 'Genero':'Masculino'})
st.header('Mostrar barra de progreso, spinner y balloons')
st.subheader('Barra de progreso')
my_bar = st.progress(0)
for p in range(10):
    my_bar.progress(p + 1)