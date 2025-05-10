import pandas as pd
import plotly.express as px
import streamlit as st

# Título de la aplicación
st.title("🚗 Análisis de Anuncios de Venta de Coches")

# Cargar los datos
file_path = "C:/Users/avict/Documents/TripleTen/car_app/vehicles_us.csv"  
car_data = pd.read_csv(file_path)

# Agregar opciones en la barra lateral
st.sidebar.header("Opciones de visualización")
build_histogram = st.sidebar.checkbox('Mostrar histograma de odómetro')
build_scatter = st.sidebar.checkbox('Mostrar gráfico de dispersión (odómetro vs. precio)')

# Mostrar resumen de datos
st.write(f"El conjunto de datos contiene **{car_data.shape[0]} filas** y **{car_data.shape[1]} columnas**.")

# Mostrar histograma si el usuario lo selecciona
if build_histogram:
    st.subheader("📊 Histograma: Distribución del Odómetro")
    hist_fig = px.histogram(car_data, x="odometer", title="Distribución de Odómetro en Vehículos")
    st.plotly_chart(hist_fig, use_container_width=True)

# Mostrar gráfico de dispersión si el usuario lo selecciona
if build_scatter:
    st.subheader("📌 Gráfico de Dispersión: Odómetro vs. Precio")
    scatter_fig = px.scatter(car_data, x="odometer", y="price", title="Relación entre Odómetro y Precio")
    st.plotly_chart(scatter_fig, use_container_width=True)

# Agregar nota final
st.write("Selecciona una opción en la barra lateral para visualizar los gráficos.")
