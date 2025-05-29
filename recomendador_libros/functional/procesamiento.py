# functional/procesamiento.py

from functools import reduce
from itertools import groupby
from operator import attrgetter
from typing import List
from models.libro import Libro

def filtrar_por_anio(libros: List[Libro], anio_min: int) -> List[Libro]:
    """Función pura que filtra libros publicados desde un año mínimo."""
    return list(filter(lambda libro: libro.anio >= anio_min, libros))

def obtener_titulos(libros: List[Libro]) -> List[str]:
    """Función pura que obtiene los títulos de una lista de libros."""
    return list(map(lambda libro: libro.titulo, libros))

def contar_por_genero(libros: List[Libro]) -> dict:
    """Cuenta cuántos libros hay por cada género usando reduce."""
    def acumulador(acum, libro):
        acum[libro.genero] = acum.get(libro.genero, 0) + 1
        return acum
    return reduce(acumulador, libros, {})

def agrupar_por_genero(libros: List[Libro]) -> dict:
    """Agrupa libros por género usando itertools.groupby.

    Nota: libros debe estar ordenada por género antes de llamar."""
    libros_ordenados = sorted(libros, key=attrgetter('genero'))
    grupos = groupby(libros_ordenados, key=attrgetter('genero'))
    return {genero: list(grp) for genero, grp in grupos}
