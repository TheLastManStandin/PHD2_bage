from screening.paint import np
from screening.pictures_4x4 import pixelarts_4x4
import neopixel
import machine
import time
import uasyncio as asyncio
import global_variables
import random

def to_flat(picture):
    return [pixel for row in picture for pixel in row]

def update_display(progress, color): 
    NUM_PIXELS = 16
    num_pixels = int(progress * NUM_PIXELS)
    pic = [(0, 0, 0) for _ in range(NUM_PIXELS)]
    
    for i in range( NUM_PIXELS):
        if i < num_pixels:
            pic[i] = color
            if i > 0:
                pic[i - 1] = tuple(map(lambda x: round(x * 0.2), color))
            if i > 1:
                pic[i - 2] = (0, 0, 0)

    global_variables.pomodoro_logic_picture = pic[::-1]

async def pomodoro_timer(work_duration, break_duration):
    work_duration = work_duration * 60
    break_duration = break_duration * 60
    plug_pic = to_flat(pixelarts_4x4["Помидор.png"])
    """
    Реализует цикл Помодоро:
    - Рабочая сессия (по умолчанию 35 минут) с зелёным прогресс-баром.
    - Перерыв (по умолчанию 10 минут) с синим прогресс-баром.
    """
    while True:
        if global_variables.pomodoro == True:
            print("Начинается рабочая сессия") 
            start_time = time.time()
            while global_variables.pomodoro == True:
                elapsed = time.time() - start_time
                if elapsed >= work_duration:
                    break
                progress = elapsed / work_duration
                update_display(progress, (0, 255, 0)) 
                await asyncio.sleep(1)
        
            print("Начинается перерыв") 
            start_time = time.time()
            while global_variables.pomodoro == True:
                elapsed = time.time() - start_time
                if elapsed >= break_duration:
                    break
                progress = elapsed / break_duration
                update_display(progress, (0, 0, 255)) 
                await asyncio.sleep(1)
        else:
            global_variables.pomodoro_logic_picture = plug_pic
            await asyncio.sleep(1)

    # print("Цикл POMODORO логики")

async def pomodoro_logic(work_duration=35, break_duration=10):
    await pomodoro_timer(work_duration, break_duration)

