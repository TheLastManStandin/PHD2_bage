from screening.paint import np
import neopixel
import machine
import time
import uasyncio as asyncio
import global_variables

def update_display(progress, color):
    PIN_NUM = 4  
    NUM_PIXELS = 100
    np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)
    """
    Обновляет дисплей: заполняет часть светодиодов в соответствии с progress (от 0.0 до 1.0)
    выбранным цветом, а остальные выключает.
    """
    num_pixels = int(progress * NUM_PIXELS)
    for i in range(NUM_PIXELS):
        if i < num_pixels:
            np[-i if i > 0 else 99] = color
            if i > 0:
                np[-(i -1) if i > 1 else 99] = list(map(lambda x: round(x * 0.3), color))
            if i > 1:
                np[-(i -2) if i > 2 else 99] = list(map(lambda x: round(x * 0.1), color))
            if i > 2:
                np[-(i -3)] = (0, 0, 0)
        else:
            np[-i] = (0, 0, 0)
    np.write()

async def pomodoro_timer(work_duration, break_duration):
    work_duration = work_duration * 60
    break_duration = break_duration * 60
    """
    Реализует цикл Помодоро:
    - Рабочая сессия (по умолчанию 35 минут) с зелёным прогресс-баром.
    - Перерыв (по умолчанию 10 минут) с синим прогресс-баром.
    """
    while True:
        if global_variables.baige_now_doing == "POMODORO":
            print("Начинается рабочая сессия") 
            start_time = time.time()
            while global_variables.baige_now_doing == "POMODORO":
                elapsed = time.time() - start_time
                if elapsed >= work_duration:
                    break
                progress = elapsed / work_duration
                update_display(progress, (0, 255, 0)) 
                await asyncio.sleep(1)
            # update_display(1.0, (0, 255, 0))
        else:
            await asyncio.sleep(1)

        if global_variables.baige_now_doing == "POMODORO":
            print("Начинается перерыв") 
            start_time = time.time()
            while global_variables.baige_now_doing == "POMODORO":
                elapsed = time.time() - start_time
                if elapsed >= break_duration:
                    break
                progress = elapsed / break_duration
                update_display(progress, (0, 0, 255)) 
                await asyncio.sleep(1)
            # update_display(1.0, (0, 0, 255))
        else:
            await asyncio.sleep(1)

    # print("Цикл POMODORO логики")

async def pomodoro_logic(work_duration=35, break_duration=10):
    await pomodoro_timer(work_duration, break_duration)

