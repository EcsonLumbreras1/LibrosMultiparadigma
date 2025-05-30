
# LibrosMultiparadigma 📚

## Descripción

**LibrosMultiparadigma** es una aplicación desarrollada en Python que integra tres paradigmas de programación: Orientación a Objetos, Programación Funcional y Programación Reactiva/Concurrente. La aplicación permite analizar datos y recomendar libros a partir de un dataset dinámico de más de 200 libros, el cual se actualiza automáticamente cada hora desde la API pública de OpenLibrary.

## Requisitos

- Python 3.9 o superior
- `pandas`
- `requests`
- `streamlit`

Instala las dependencias con:

```bash
pip install -r requirements.txt
```

## Instrucciones de Ejecución

### Ejecutar el recomendador interactivo:

```bash
streamlit run src/interface.py
```

### Ejecutar la actualización periódica de libros (cada hora):

```bash
python main.py
```

## Justificación Técnica

### Paradigma Orientado a Objetos
- Se implementaron clases como `Libro`, `LibroRecomendado`, `Genero` y `Autor`.
- Se usó herencia y polimorfismo (`LibroRecomendado` hereda de `Libro` y sobreescribe métodos).
- Se aplicaron principios SOLID como SRP, OCP y LSP para un diseño modular y extensible.

### Paradigma Funcional
- Se usaron funciones puras para operaciones como filtrado, ordenamiento y cálculo de promedios.
- Se utilizaron funciones de orden superior: `map`, `filter`, `reduce`.
- Se creó un módulo funcional separado para encapsular este comportamiento.

### Paradigma Reactivo/Concurrente
- Se implementó una función asíncrona con `asyncio` que actualiza el dataset automáticamente cada hora.
- El enfoque concurrente permite mantener datos actualizados sin afectar la interacción del usuario.

## Videos

- 🎥 [Video técnico explicativo](https://drive.google.com/...)
- 🎥 [Video de demostración de la aplicación](https://drive.google.com/...)

## Equipo

- **Nombre del miembro 1** – Recolector de datos, lógica de negocio funcional.
- **Nombre del miembro 2** – Estructura OOP y diseño de clases.
- **Nombre del miembro 3** – Interfaz con Streamlit y lógica reactiva.

## Enlace al Repositorio

[https://github.com/usuario/librosmultiparadigma](https://github.com/usuario/librosmultiparadigma)


## Nota sobre funciones no utilizadas directamente

Se desarrollaron varias funciones y clases adicionales que no están conectadas actualmente a la interfaz interactiva, pero que fueron creadas para demostrar dominio en los paradigmas requeridos. Estas funciones siguen principios de modularidad y están listas para futuras integraciones. Su inclusión permite cumplir con los principios SOLID y la separación de responsabilidades entre lógica de negocio y presentación.
