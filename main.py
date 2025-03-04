import neopixel
import time
import ntptime
from wifi import connect_wifi
from config import load_env
from screening.paint import paint_this, np
from schedule_logic import schedule_logic
from pomodoro_logic import pomodoro_logic
from button_check import button_press_check
import uasyncio as asyncio
import machine

screen_dot_num = 0

def next_load_dot(success):
    """
    Загрузка бейджика отображается в виде появляющихся точек
    """
    global screen_dot_num

    np[-screen_dot_num if screen_dot_num != 0 else 99] = (0, 255, 0) if success else (255, 0, 0)

    screen_dot_num += 1
    np.write()


next_load_dot(True)
# paint_this("spi")
# 17 - bri ,16 - led ,2 - pass

config = load_env()
ssid = config.get("WIFI_SSID")
password = config.get("WIFI_PASS")
wlan = connect_wifi(ssid, password)
next_load_dot(True)

ntptime.host = "ntp0.ntp-servers.net"
try:
    ntptime.settime()
    next_load_dot(True)
except Exception as e:
    print("Ошибка синхронизации времени:", e)
    next_load_dot(False)
    raise KeyboardInterrupt

UTC_OFFSET = 3 * 3600
current_time = time.localtime(time.time() + UTC_OFFSET)
print("Текущее время:", current_time)



async def main():
    asyncio.create_task(schedule_logic())
    asyncio.create_task(pomodoro_logic())
    asyncio.create_task(button_press_check())

    while True:
        await asyncio.sleep(1)

asyncio.run(main())