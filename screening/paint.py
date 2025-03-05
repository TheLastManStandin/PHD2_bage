import neopixel
import machine

from screening.pictures_10x10 import pixelarts

PIN_NUM = 4  
NUM_PIXELS = 100
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)

def to_flat(picture):
    return [pixel for row in picture for pixel in row]

def paint_this(picture, brightness = 1):
    for i, color in enumerate(to_flat(pixelarts[picture])):
        color = list(map(lambda x: round(x * brightness), color))
        np[i] = color 
    np.write()
