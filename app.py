import pandas as pd
import streamlit as st
import plotly.express as px

# Leer los datos del archivo CSV
car_data = pd.read_csv('vehicles_us.csv')

# creación de un header
st.header('Vehicles analysis')

# Crear un botón en la interfaz
hist_button = st.checkbox('Construir histograma')

# Crear un botón en la interfaz
scatter_button = st.checkbox('Construir gráfico de dispersión')

# Si se hace clic en el botón, crear y mostrar el histograma
if hist_button:
    # Escribir un mensaje en la interfaz
    st.write(
        'Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # Crear un histograma usando Plotly
    fig = px.histogram(car_data, x="odometer")

    # Mostrar el gráfico en la interfaz de Streamlit
    st.plotly_chart(fig, use_container_width=True)


# Si se hace clic en el botón, crear y mostrar el gráfico de dispersión
if scatter_button:
    # Escribir un mensaje en la interfaz
    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')

    # Crear un gráfico de dispersión usando Plotly
    fig = px.scatter(car_data, x="odometer", y="price")

    # Mostrar el gráfico en la interfaz de Streamlit
    st.plotly_chart(fig, use_container_width=True)
