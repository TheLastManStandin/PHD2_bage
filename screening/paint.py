import neopixel
import machine
import global_variables
import uasyncio as asyncio

# from screening.pictures_10x10 import pixelarts

PIN_NUM = 4  
NUM_PIXELS = 100
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)

def fill_pixel(x, y, iterator, brightness):
    try:
        pixel_color = next(iterator)
        pixel_color = list(map(lambda x: round(x * brightness), pixel_color))
        np[x * 10 + y] = pixel_color
    except:
        pass

async def update_display(first_module=[],second_module=[],third_module=[],forth_module=[],brightness=1):
    center = 10 // 2

    first_module_iterator = iter(first_module)
    second_module_iterator = iter(second_module)
    third_module_iterator = iter(third_module)

    if global_variables.modules == 4:
        forth_module_iterator = iter(forth_module)

    for x in range(10):
        for y in range(10):
            if x < 4 and y < 4:
                fill_pixel(x, y, first_module_iterator, brightness)
            if x > 4 and y < 4:
                fill_pixel(x, y, second_module_iterator, brightness)
            if y >= 5 and global_variables.modules == 3:
                fill_pixel(x, y, third_module_iterator, brightness)
    
    np.write()

async def display_logic():
    if global_variables.modules == 4:
        for x in range(10):
            for y in range(10):
                if (4 <= x and x <= 5) or (4 <= y and y <= 5):
                    np[x * 10 + y] = (10, 10, 10)

        while True:
            await update_display(
                first_module=global_variables.schedule_logic_picture,
                second_module=global_variables.pomodoro_logic_picture,
                brightness=0.2
                )
            await asyncio.sleep(1)
    elif global_variables.modules == 3:
        for x in range(10):
            for y in range(10):
                if y < 5:
                    np[x * 10 + y] = (10, 10, 10)

        while True:
            await update_display(
                first_module=global_variables.schedule_logic_picture,
                second_module=global_variables.pomodoro_logic_picture,
                third_module=global_variables.gif_5x10_logic_picture,
                brightness=0.1
                )
            await asyncio.sleep(0.5)