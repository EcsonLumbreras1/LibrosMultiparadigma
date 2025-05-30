# main.py
import asyncio
from src.actualizacion_datos import actualizar_dataset_periodicamente

# Ejecuta la actualización del dataset cada hora
async def iniciar_actualizacion():
    await actualizar_dataset_periodicamente()

if __name__ == "__main__":
    asyncio.run(iniciar_actualizacion())
