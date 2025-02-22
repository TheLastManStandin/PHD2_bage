import neopixel
import time
from wifi import connect_wifi
from config import load_env
from paint import paint_this

paint_this("burger")

config = load_env()

ssid = config.get("WIFI_SSID")
password = config.get("WIFI_PASS")
wlan = connect_wifi(ssid, password)
