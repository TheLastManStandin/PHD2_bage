import machine
import neopixel
import time

# Настройка пинов и количества светодиодов (10x10 = 100) 😊
PIN_NUM = 4  # Пин подключения NeoPixel 😊
NUM_PIXELS = 100  # Общее количество пикселей 😊
np = neopixel.NeoPixel(machine.Pin(PIN_NUM), NUM_PIXELS)

# Определяем основные цвета 😊
BLACK = (0, 0, 0)        # Чёрный цвет 😊
ORANGE = (255, 165, 0)     # Оранжевый цвет (базовый цвет тигра) 😊
WHITE = (255, 255, 255)    # Белый цвет (для глаз) 😊

# Определяем пиксельный арт тигра в виде матрицы 10x10 😊
# Каждая строка – это список из 10 элементов (цветов) 😊
tiger = [
    [(30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139),
     (30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139)],

    [(30, 105, 139), (30, 105, 139), (107, 75, 23), (107, 75, 23), (127, 100, 60),
     (107, 75, 23), (107, 75, 23), (127, 100, 60), (30, 105, 139), (30, 105, 139)],

    [(30, 105, 139), (107, 75, 23), (127, 100, 60), (107, 75, 23), (107, 75, 23),
     (107, 75, 23), (107, 75, 23), (107, 75, 23), (107, 75, 23), (30, 105, 139)],

    [(30, 105, 139), (127, 100, 60), (107, 75, 23), (107, 75, 23), (127, 100, 60),
     (107, 75, 23), (127, 100, 60), (107, 75, 23), (127, 100, 60), (30, 105, 139)],

    [(30, 105, 139), (18, 103, 18), (18, 103, 18), (107, 75, 23), (107, 75, 23),
     (107, 75, 23), (107, 75, 23), (18, 103, 18), (18, 103, 18), (30, 105, 139)],

    [(30, 105, 139), (39, 26, 4), (153, 0, 0), (18, 103, 18), (18, 103, 18),
     (18, 103, 18), (18, 103, 18), (153, 0, 0), (39, 26, 4), (30, 105, 139)],

    [(30, 105, 139), (39, 26, 4), (39, 26, 4), (153, 0, 0), (153, 0, 0),
     (153, 0, 0), (153, 0, 0), (39, 26, 4), (39, 26, 4), (30, 105, 139)],

    [(30, 105, 139), (107, 75, 23), (39, 26, 4), (39, 26, 4), (39, 26, 4),
     (39, 26, 4), (39, 26, 4), (39, 26, 4), (107, 75, 23), (30, 105, 139)],

    [(30, 105, 139), (30, 105, 139), (107, 75, 23), (107, 75, 23), (107, 75, 23),
     (107, 75, 23), (107, 75, 23), (107, 75, 23), (30, 105, 139), (30, 105, 139)],

    [(30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139),
     (30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139), (30, 105, 139)]
]

# Преобразуем матрицу (список списков) в плоский список из 100 элементов 😊
tiger_flat = [pixel for row in tiger for pixel in row]

# Выводим изображение тигра на матрицу NeoPixel 😊
for i, color in enumerate(tiger_flat):
    np[i] = color  # Присваиваем цвет каждому пикселю по порядку 😊
np.write()  # Отправляем данные на светодиоды 😊

# Задержка, чтобы можно было наблюдать изображение 😊
time.sleep(10)
