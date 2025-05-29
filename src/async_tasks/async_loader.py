import asyncio
from loader import load_books_from_csv

async def async_load_books(path):
    print("Iniciando carga asíncrona de libros...")
    await asyncio.sleep(1)  # Simula retraso en lectura
    books = load_books_from_csv(path)
    print("Carga completada.")
    return books

async def simulate_user_requests(books):
    async def recommend(user_id):
        print(f"Usuario {user_id} está recibiendo recomendaciones...")
        await asyncio.sleep(2)  # Simula tiempo de procesamiento
        print(f"Usuario {user_id} recibió recomendaciones.")
    
    await asyncio.gather(*(recommend(i) for i in range(1, 4)))
