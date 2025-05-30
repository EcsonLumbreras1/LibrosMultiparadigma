# src/recomendador.py
from src.modelo_datos import LibroRecomendado
from src.funciones_funcionales import filtrar_libros_por_genero, obtener_libros_recomendados

def recomendar_libros(libros_dataset, genero_seleccionado=None, autor_seleccionado=None):
    """
    Función principal para recomendar libros basados en filtros de género y autor.
    :param libros_dataset: lista de objetos Libro
    :param genero_seleccionado: str, género seleccionado para filtrar (opcional)
    :param autor_seleccionado: str, autor seleccionado para filtrar (opcional)
    :return: lista de libros recomendados
    """
    
    # Filtrar por género
    if genero_seleccionado and genero_seleccionado != "Todos":
        libros_filtrados = filtrar_libros_por_genero(libros_dataset, genero_seleccionado)
    else:
        libros_filtrados = libros_dataset

    # Filtrar por autor si se ingresó uno
    if autor_seleccionado:
        libros_filtrados = [libro for libro in libros_filtrados if autor_seleccionado.lower() in libro.autor.lower()]
    
    # Obtener libros recomendados (ranking >= 4)
    libros_recomendados = obtener_libros_recomendados(libros_filtrados)
    
    # Crear objetos de tipo LibroRecomendado con el motivo de recomendación
    libros_recomendados_con_motivo = []
    for libro in libros_recomendados:
        motivo_recomendacion = "Altamente recomendado por su ranking"
        libro_recomendado = LibroRecomendado(libro.titulo, libro.autor, libro.genero, libro.ranking, libro.fecha_publicacion, motivo_recomendacion)
        libros_recomendados_con_motivo.append(libro_recomendado)
    
    return libros_recomendados_con_motivo