# src/funciones_funcionales.py
from functools import reduce

def calcular_promedio_ranking(libros):
    """
    Calcula el promedio del ranking de los libros.
    :param libros: lista de objetos Libro
    :return: float, el promedio de los rankings
    """
    if not libros:
        return 0.0
    total_ranking = reduce(lambda total, libro: total + libro.ranking, libros, 0)
    return total_ranking / len(libros)

def filtrar_libros_por_genero(libros, genero):
    """
    Filtra los libros por género.
    :param libros: lista de objetos Libro
    :param genero: str, el género a filtrar
    :return: lista de objetos Libro filtrados por género
    """
    return list(filter(lambda libro: libro.genero == genero, libros))

def ordenar_libros_por_ranking(libros, reverso=False):
    """
    Ordena los libros por ranking de mayor a menor.
    :param libros: lista de objetos Libro
    :param reverso: bool, si True ordena de mayor a menor
    :return: lista de objetos Libro ordenados
    """
    return sorted(libros, key=lambda libro: libro.ranking, reverse=reverso)

def obtener_libros_recomendados(libros):
    """
    Obtiene los libros recomendados con ranking mayor a 4.
    :param libros: lista de objetos Libro
    :return: lista de objetos Libro recomendados
    """
    return list(filter(lambda libro: libro.ranking >= 4, libros))

def obtener_libros_por_autor(libros, autor):
    """
    Filtra los libros por autor.
    :param libros: lista de objetos Libro
    :param autor: str, el autor a filtrar
    :return: lista de objetos Libro filtrados por autor
    """
    return list(filter(lambda libro: libro.autor == autor, libros))

