# src/modelo_datos.py

class Libro:
    def __init__(self, titulo, autor, genero, ranking, fecha_publicacion):
        """
        Constructor de la clase Libro.
        :param titulo: str, título del libro
        :param autor: str, autor del libro
        :param genero: str, género del libro
        :param ranking: float, ranking del libro (de 1 a 5)
        :param fecha_publicacion: str, fecha de publicación del libro
        """
        self.titulo = titulo
        self.autor = autor
        self.genero = genero
        self.ranking = ranking
        self.fecha_publicacion = fecha_publicacion

    def mostrar_informacion(self):
        """
        Muestra la información básica del libro.
        """
        return f"{self.titulo} por {self.autor} (Género: {self.genero}, Ranking: {self.ranking})"

    def actualizar_ranking(self, nuevo_ranking):
        """
        Actualiza el ranking del libro.
        :param nuevo_ranking: float, nuevo ranking
        """
        if 0 <= nuevo_ranking <= 5:
            self.ranking = nuevo_ranking
        else:
            raise ValueError("El ranking debe estar entre 0 y 5")


class LibroRecomendado(Libro):
    def __init__(self, titulo, autor, genero, ranking, fecha_publicacion, motivo_recomendacion):
        """
        Constructor de la clase LibroRecomendado, que extiende a Libro.
        :param motivo_recomendacion: str, razón para recomendar este libro
        """
        super().__init__(titulo, autor, genero, ranking, fecha_publicacion)
        self.motivo_recomendacion = motivo_recomendacion

    def mostrar_informacion(self):
        """
        Muestra la información del libro recomendado con el motivo de recomendación.
        """
        info_libro = super().mostrar_informacion()
        return f"{info_libro} - Motivo de recomendación: {self.motivo_recomendacion}"


class Genero:
    def __init__(self, nombre):
        """
        Clase que representa un género de libro.
        :param nombre: str, nombre del género
        """
        self.nombre = nombre

    def __str__(self):
        return self.nombre


class Autor:
    def __init__(self, nombre):
        """
        Clase que representa a un autor.
        :param nombre: str, nombre del autor
        """
        self.nombre = nombre

    def __str__(self):
        return self.nombre
