import asyncio
import random
import requests
import pandas as pd
from datetime import datetime
from src.modelo_datos import Libro

generos_posibles = ["fiction", "romance", "fantasy", "science_fiction", "mystery"]
DATASET_PATH = "data/libros_dataset.csv"

def obtener_libros_desde_api(genero, limite=40):
    url = f"https://openlibrary.org/subjects/{genero}.json?limit={limite}"
    response = requests.get(url)
    libros = []
    if response.status_code == 200:
        data = response.json()
        for doc in data.get("works", []):
            titulo = doc.get("title", "Desconocido")
            autor = ", ".join([a.get("name", "Desconocido") for a in doc.get("authors", [])])
            ranking = round(random.uniform(1, 5), 1)
            fecha_publicacion = doc.get("first_publish_year", datetime.now().year)
            libros.append({
                "titulo": titulo,
                "autor": autor,
                "genero": genero,
                "ranking": ranking,
                "fecha_publicacion": fecha_publicacion
            })
    return libros

def guardar_libros_en_csv(libros):
    df = pd.DataFrame(libros)
    df.to_csv(DATASET_PATH, index=False)

def cargar_libros_desde_csv():
    try:
        df = pd.read_csv(DATASET_PATH)
        return [
            Libro(row["titulo"], row["autor"], row["genero"], row["ranking"], row["fecha_publicacion"])
            for _, row in df.iterrows()
        ]
    except FileNotFoundError:
        return []

async def actualizar_dataset_periodicamente():
    while True:
        libros_nuevos = []
        for genero in generos_posibles:
            libros_nuevos.extend(obtener_libros_desde_api(genero, limite=40))
        guardar_libros_en_csv(libros_nuevos)
        print("✅ Dataset actualizado con nuevos libros.")
        await asyncio.sleep(3600)  # Espera 1 hora
