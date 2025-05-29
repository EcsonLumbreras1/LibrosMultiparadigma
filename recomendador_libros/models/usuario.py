# models/usuario.py

class Usuario:
    def __init__(self, id_usuario: int, nombre: str, generos_favoritos=None, autores_favoritos=None):
        self._id_usuario = id_usuario
        self._nombre = nombre
        self._generos_favoritos = generos_favoritos if generos_favoritos else []
        self._autores_favoritos = autores_favoritos if autores_favoritos else []

    @property
    def id_usuario(self):
        return self._id_usuario

    @property
    def nombre(self):
        return self._nombre

    @property
    def generos_favoritos(self):
        return self._generos_favoritos

    @generos_favoritos.setter
    def generos_favoritos(self, generos):
        if isinstance(generos, list):
            self._generos_favoritos = generos

    @property
    def autores_favoritos(self):
        return self._autores_favoritos

    @autores_favoritos.setter
    def autores_favoritos(self, autores):
        if isinstance(autores, list):
            self._autores_favoritos = autores

    def agregar_genero_favorito(self, genero: str):
        if genero not in self._generos_favoritos:
            self._generos_favoritos.append(genero)

    def agregar_autor_favorito(self, autor: str):
        if autor not in self._autores_favoritos:
            self._autores_favoritos.append(autor)

    def __str__(self):
        return f"Usuario: {self._nombre} | Géneros favoritos: {self._generos_favoritos} | Autores favoritos: {self._autores_favoritos}"

    def __repr__(self):
        return f"Usuario({self._id_usuario}, {self._nombre})"
