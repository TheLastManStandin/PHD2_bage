import uasyncio as asyncio
from picsNgifs.beach_gif_5x10 import gif
import global_variables

def to_flat(picture):
    return [pixel for row in picture for pixel in row]

async def gif_logic():
    while True:
        for i in range(len(gif), 0,-1): # тк конвертер картинок у меня конвертирует в обратном порядке
            global_variables.gif_5x10_logic_picture = to_flat(gif[f"Пляж.png_{i - 1}"])
            await asyncio.sleep(0.5)