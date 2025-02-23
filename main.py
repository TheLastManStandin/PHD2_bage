import neopixel
import time
import ntptime
from wifi import connect_wifi
from config import load_env
from paint import paint_this

paint_this("amogus")

config = load_env()

ssid = config.get("WIFI_SSID")
password = config.get("WIFI_PASS")
wlan = connect_wifi(ssid, password)

try:
    ntptime.settime()
except Exception as e:
    print("Ошибка синхронизации времени:", e)  

current_time = time.localtime()
print("Текущее время:", current_time)