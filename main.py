import neopixel
import time
import ntptime
from wifi import connect_wifi
from config import load_env
from screening.paint import paint_this, np
from utils.decode_unicode_escape import decode_unicode_escape
import os
import uasyncio as asyncio

screen_dot_num = 0

def next_load_dot(success):
    global screen_dot_num

    np[screen_dot_num] = (0, 255, 0) if success else (255, 0, 0)

    screen_dot_num += 1
    np.write()

next_load_dot(True)
# paint_this("dot")
# current_pic = "dot"

config = load_env()
ssid = config.get("WIFI_SSID")
password = config.get("WIFI_PASS")
wlan = connect_wifi(ssid, password)

ntptime.host = "ntp0.ntp-servers.net"
try:
    ntptime.settime()
    next_load_dot(True)
except Exception as e:
    print("Ошибка синхронизации времени:", e)
    next_load_dot(False)

UTC_OFFSET = 3 * 3600
current_time = time.localtime(time.time() + UTC_OFFSET)
print("Текущее время:", current_time)

async def update_pic(schedule_list):
    while True:
        current_time = time.localtime(time.time() + UTC_OFFSET)
        # current_time = (2025, 3, 2, 15, 38, 56, 6, 61)
        current_seconds = current_time[3] * 3600 + current_time[4] * 60 + current_time[5] #+ UTC_OFFSET

        current_activity = None
        last_time_seconds = 0

        print(current_seconds)

        for task in schedule_list:
            scheduled_time = task[0]
            activity = task[1]
            print(activity, end="\t")
            hours, minutes = map(int, scheduled_time.split(':'))
            scheduled_seconds = hours * 3600 + minutes * 60

            if scheduled_seconds <= current_seconds:
                if scheduled_seconds >= last_time_seconds:
                    last_time_seconds = scheduled_seconds
                    current_activity = activity

            print(current_activity, scheduled_seconds)

        if current_activity == None:
            current_activity = schedule_list[-1][1]

        if current_activity == "Ворк":
            paint_this("steve")
            current_pic = "steve"
        elif current_activity == "Обед" or current_activity == "Завтрак":
            paint_this("burger")
            current_pic = "burger"
        else:
            paint_this("amogus")
            current_pic = "amogus"

        await asyncio.sleep(30)

async def main():
    with open('schedule.txt', 'r', encoding='utf-8') as file:
        schedule_list = []
        for i in file:
            i = str(i)
            i = i.split("-")

            schedule_list.append([i[0].strip(), i[1].strip()])

    asyncio.create_task(update_pic(schedule_list))

    while True:
        await asyncio.sleep(1)

asyncio.run(main())