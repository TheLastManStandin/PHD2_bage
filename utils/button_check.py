import global_variables
import machine
import uasyncio as asyncio
import time

async def button_press_check():
    while True:
        LED_pin = machine.Pin(16, machine.Pin.IN, machine.Pin.PULL_UP)

        if LED_pin.value() == 0:
            if global_variables.pomodoro == False:
                global_variables.pomodoro = True
                print("Переключение на режим помодоро")
                time.sleep(2)
            elif global_variables.pomodoro == True:
                global_variables.pomodoro = False
                print("Переключение на режим расписания")
                time.sleep(2)

        await asyncio.sleep(0.2)