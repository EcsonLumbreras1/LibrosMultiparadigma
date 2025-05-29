# models/libro.py

class Libro:
    def __init__(self, id_libro: int, titulo: str, autor: str, genero: str, anio: int):
        self._id_libro = id_libro
        self._titulo = titulo
        self._autor = autor
        self._genero = genero
        self._anio = anio

    # Encapsulamiento: uso de propiedades para acceso controlado
    @property
    def id_libro(self):
        return self._id_libro

    @property
    def titulo(self):
        return self._titulo

    @property
    def autor(self):
        return self._autor

    @property
    def genero(self):
        return self._genero

    @property
    def anio(self):
        return self._anio

    def __str__(self):
        return f"'{self._titulo}' por {self._autor} ({self._anio}) - Género: {self._genero}"

    def __repr__(self):
        return f"Libro({self._id_libro}, {self._titulo}, {self._autor}, {self._genero}, {self._anio})"
