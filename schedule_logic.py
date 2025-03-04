from screening.paint import paint_this
import global_variables
import uasyncio as asyncio
import time

def paint_pic_of(current_activity):
    if current_activity == "Ворк":
        paint_this("steve", 0.1)
    elif current_activity == "Обед" or current_activity == "Завтрак":
        paint_this("esh", 0.1)
    elif current_activity == "Сон":
        paint_this("spi", 0.1)
    elif current_activity == "Подъём":
        paint_this("wakeup", 0.1)
    elif current_activity == "Книжка":
        paint_this("um", 0.1)
    else:
        paint_this("amogus", 0.1)

async def update_pic():
    schedule_list = []
    UTC_OFFSET = 3 * 3600

    with open('schedule.txt', 'r', encoding='utf-8') as file:
        schedule_list = []
        for i in file:
            i = str(i)
            i = i.split("-")

            schedule_list.append([i[0].strip(), i[1].strip()])

    while True:
        if global_variables.baige_now_doing == "SCHEDULE":
            current_time = time.localtime(time.time() + UTC_OFFSET)
            # current_time = (2025, 3, 2, 15, 38, 56, 6, 61)
            current_seconds = current_time[3] * 3600 + current_time[4] * 60 + current_time[5] #+ UTC_OFFSET

            current_activity = None
            last_time_seconds = 0

            for task in schedule_list:
                scheduled_time = task[0]
                activity = task[1]
                hours, minutes = map(int, scheduled_time.split(':'))
                scheduled_seconds = hours * 3600 + minutes * 60

                if scheduled_seconds <= current_seconds:
                    if scheduled_seconds >= last_time_seconds:
                        last_time_seconds = scheduled_seconds
                        current_activity = activity

            if current_activity == None:
                current_activity = schedule_list[-1][1]

            paint_pic_of(current_activity)

        # print("Цикл SCHEDULE логики")
        await asyncio.sleep(2)

async def schedule_logic():
    await update_pic()