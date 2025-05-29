# models/recomendador.py

from typing import List
from models.libro import Libro
from models.usuario import Usuario

class Recomendador:
    def __init__(self, libros: List[Libro]):
        self._libros = libros  # lista de libros disponibles

    @property
    def libros(self):
        return self._libros

    def recomendar_por_genero(self, usuario: Usuario) -> List[Libro]:
        """Recomienda libros que coincidan con los géneros favoritos del usuario."""
        recomendados = [libro for libro in self._libros if libro.genero in usuario.generos_favoritos]
        return recomendados

    def recomendar_por_autor(self, usuario: Usuario) -> List[Libro]:
        """Recomienda libros que coincidan con los autores favoritos del usuario."""
        recomendados = [libro for libro in self._libros if libro.autor in usuario.autores_favoritos]
        return recomendados

    def recomendar(self, usuario: Usuario, metodo: str = "genero") -> List[Libro]:
        """Método polimórfico para recomendar según el método elegido."""
        if metodo == "genero":
            return self.recomendar_por_genero(usuario)
        elif metodo == "autor":
            return self.recomendar_por_autor(usuario)
        else:
            # Si método no reconocido, devolver libros populares (los primeros 10 por ejemplo)
            return self._libros[:10]
