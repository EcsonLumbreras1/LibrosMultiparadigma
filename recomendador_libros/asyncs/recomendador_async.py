# asyncs/recomendador_async.py

import asyncio
from typing import List
from models.libro import Libro
from models.usuario import Usuario

class RecomendadorAsync:
    def __init__(self, libros: List[Libro]):
        self._libros = libros

    async def cargar_libros(self):
        """Simula la carga asíncrona de libros (ejemplo)."""
        await asyncio.sleep(1)  # simula tiempo de carga
        return self._libros

    async def recomendar_por_genero(self, usuario: Usuario) -> List[Libro]:
        libros = await self.cargar_libros()
        # Filtra libros cuyo género esté en los favoritos del usuario
        return [libro for libro in libros if libro.genero in usuario.generos_favoritos]

    async def recomendar_por_autor(self, usuario: Usuario) -> List[Libro]:
        libros = await self.cargar_libros()
        # Filtra libros cuyo autor esté en los favoritos del usuario
        return [libro for libro in libros if libro.autor in usuario.autores_favoritos]

    async def recomendar(self, usuario: Usuario, metodo: str = "genero") -> List[Libro]:
        if metodo == "genero":
            return await self.recomendar_por_genero(usuario)
        elif metodo == "autor":
            return await self.recomendar_por_autor(usuario)
        else:
            libros = await self.cargar_libros()
            return libros[:10]

# Ejemplo básico de función asincrónica que maneja concurrencia con eventos
async def demo_recomendacion_concurrente(recomendador: RecomendadorAsync, usuarios: List[Usuario]):
    tareas = []
    for usuario in usuarios:
        tarea = asyncio.create_task(recomendador.recomendar(usuario, metodo="genero"))
        tareas.append(tarea)
    resultados = await asyncio.gather(*tareas)
    return resultados
