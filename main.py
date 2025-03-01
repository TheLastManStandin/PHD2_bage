import neopixel
import time
import ntptime
from wifi import connect_wifi
from config import load_env
from screening.paint import paint_this
from utils.decode_unicode_escape import decode_unicode_escape
import os
import uasyncio as asyncio

paint_this("dot")
current_pic = "dot"

config = load_env()
ssid = config.get("WIFI_SSID")
password = config.get("WIFI_PASS")
wlan = connect_wifi(ssid, password)

ntptime.host = "ntp0.ntp-servers.net"
try:
    ntptime.settime()
except Exception as e:
    print("Ошибка синхронизации времени:", e)

UTC_OFFSET = 3 * 3600
current_time = time.localtime(time.time() + UTC_OFFSET)
print("Текущее время:", current_time)

def get_schedule_list(file):
    shcedule_list = []

    for line in file:
        decoded = decode_unicode_escape(line.strip())
        parts = decoded.split('\u2013')  # Используем юникод-символ напрямую
        if len(parts) >= 2:
            time_part = parts[0].strip()
            event_part = parts[1].strip()
            shcedule_list.append([time_part, event_part])

    return shcedule_list

async def update_pic(schedule_list):
    while True:
        current_time = time.localtime(time.time() + UTC_OFFSET)
        current_seconds = current_time[3] * 3600 + current_time[4] * 60 + current_time[5] + UTC_OFFSET

        current_activity = None
        last_time_seconds = 0

        for task in schedule_list:
            scheduled_time = task[0]
            activity = task[1]
            hours, minutes = map(int, scheduled_time.split(':'))
            scheduled_seconds = hours * 3600 + minutes * 60

            # Если запланированное время меньше или равно текущему, обновляем текущее занятие
            if scheduled_seconds <= current_seconds:
                if scheduled_seconds >= last_time_seconds:
                    last_time_seconds = scheduled_seconds
                    current_activity = activity

        if current_activity == None:
            current_activity = schedule_list[-1][1]
        
        retu

        await asyncio.sleep(5)

async def main():
    with open('schedule.txt', 'r', encoding='utf-8') as file:
        schedule_list = get_schedule_list(file)

    asyncio.create_task(update_pic(schedule_list))

    while True:
        await asyncio.sleep(1)

asyncio.run(main())