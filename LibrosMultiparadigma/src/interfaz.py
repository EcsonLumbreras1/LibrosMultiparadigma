import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from modelo_datos import LibroRecomendado
from funciones_funcionales import filtrar_libros_por_genero, obtener_libros_recomendados, calcular_promedio_ranking
from actualizacion_datos import cargar_libros_desde_csv

def mostrar_recomendaciones(libros_dataset):
    st.title("Recomendador de Libros")

    genero_seleccionado = st.selectbox("Selecciona un género", ["Todos", "fiction", "romance", "fantasy", "science_fiction", "mystery"])
    autor_seleccionado = st.text_input("Autor (opcional)")

    libros_filtrados = libros_dataset
    if genero_seleccionado != "Todos":
        libros_filtrados = filtrar_libros_por_genero(libros_filtrados, genero_seleccionado)
    if autor_seleccionado:
        libros_filtrados = [l for l in libros_filtrados if autor_seleccionado.lower() in l.autor.lower()]

    libros_recomendados = obtener_libros_recomendados(libros_filtrados)
    st.subheader(f"Libros recomendados ({len(libros_recomendados)})")

    if libros_recomendados:
        for libro in libros_recomendados:
            st.write(f"**{libro.titulo}** por {libro.autor} ({libro.genero}) - ⭐ {libro.ranking}")
    else:
        st.write("No hay libros recomendados con los filtros actuales.")

    if libros_filtrados:
        promedio = calcular_promedio_ranking(libros_filtrados)
        st.write(f"📊 Promedio de ranking: {promedio:.2f}")

def main():
    libros_dataset = cargar_libros_desde_csv()
    mostrar_recomendaciones(libros_dataset)

if __name__ == "__main__":
    main()
