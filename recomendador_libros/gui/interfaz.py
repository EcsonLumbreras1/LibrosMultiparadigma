import streamlit as st
import csv
import asyncio
from models.libro import Libro
from models.usuario import Usuario
from models.recomendador import Recomendador
from functional import procesamiento
from asyncs.recomendador_async import RecomendadorAsync  

# Función para cargar los libros desde el archivo CSV
def cargar_datos(libros_csv_path: str):
    libros = []
    with open(libros_csv_path, newline='', encoding='utf-8') as csvfile:
        lector = csv.DictReader(csvfile)
        for fila in lector:
            libro = Libro(
                id_libro=int(fila['id']),
                titulo=fila['titulo'],
                autor=fila['autor'],
                genero=fila['genero'],
                anio=int(fila['anio'])
            )
            libros.append(libro)
    return libros

def main():
    st.title("Recomendador de Libros Multiparadigma")

    libros = cargar_datos('data/libros.csv')
    recomendador = Recomendador(libros)

    # **Sección 1: Funciones Funcionales**
    st.header("Análisis Funcional de Libros")

    # Filtro por año
    anio_min = st.number_input("Filtrar libros publicados desde el año:", min_value=0, max_value=2100, value=2000)
    if st.button("Aplicar filtro por año"):
        libros_filtrados = procesamiento.filtrar_por_anio(libros, anio_min)
        st.write(f"Libros publicados desde {anio_min}:")
        for libro in libros_filtrados:
            st.write(libro)

    # Contar libros por género
    if st.button("Contar libros por género"):
        conteo = procesamiento.contar_por_genero(libros)
        st.write("Conteo de libros por género:")
        st.json(conteo)

    # Obtener títulos
    if st.button("Mostrar títulos de libros"):
        titulos = procesamiento.obtener_titulos(libros)
        st.write(titulos)

    # Agrupar libros por género
    if st.button("Agrupar libros por género"):
        grupos = procesamiento.agrupar_por_genero(libros)
        for genero, grupo in grupos.items():
            st.write(f"{genero}: {[libro.titulo for libro in grupo]}")
    
    st.markdown("---")

    # **Sección 2: Funciones Asíncronas (Reactivas)**
    st.header("Recomendación Asíncrona de Libros")

    # Simulamos un usuario con preferencias
    usuario = Usuario(1, "Usuario1", ["Fantasía", "Misterio"], ["Autor 1"])

    # Función para ejecutar recomendaciones asíncronas
    async def recomendar_async():
        recomendador = RecomendadorAsync(libros)
        recomendaciones = await recomendador.recomendar(usuario, metodo="genero")
        return recomendaciones

    if st.button("Obtener recomendaciones (Asíncrono)"):
        recomendaciones = asyncio.run(recomendar_async())  # Ejecuta la función asincrónica
        st.write("Recomendaciones de libros:")
        for libro in recomendaciones:
            st.write(f"- {libro.titulo} por {libro.autor}")

    st.markdown("---")

    # **Sección 3: Funciones Orientadas a Objetos (OOP)**
    st.header("Recomendación de Libros (OOP)")
    
    nombre_usuario = st.text_input("Ingresa tu nombre:")
    generos_input = st.text_input("Géneros favoritos (separados por coma):")
    autores_input = st.text_input("Autores favoritos (separados por coma):")
    metodo = st.selectbox("Método de recomendación:", ["genero", "autor"])
    
    # Creación del objeto recomendador
    recomendador_oop = Recomendador(libros)

    # Obtener preferencias del usuario
    if st.button("Recomendar libros (OOP)"):
        generos_fav = [g.strip() for g in generos_input.split(",") if g.strip()]
        autores_fav = [a.strip() for a in autores_input.split(",") if a.strip()]

        usuario = Usuario(
            id_usuario=1,
            nombre=nombre_usuario,
            generos_favoritos=generos_fav,
            autores_favoritos=autores_fav
        )

        recomendaciones_oop = recomendador_oop.recomendar(usuario, metodo=metodo)

        st.subheader(f"Recomendaciones para {usuario.nombre}:")
        if recomendaciones_oop:
            for libro in recomendaciones_oop:
                st.write(f"- {libro}")
        else:
            st.write("No se encontraron recomendaciones con los filtros dados.")

if __name__ == "__main__":
    main()
