from picsNgifs.pictures_4x4 import pixelarts_4x4
import global_variables
import uasyncio as asyncio
import time

def to_flat(picture):
    return [pixel for row in picture for pixel in row]

def get_current_pic(current_activity):
    if current_activity == "Ворк":
        return to_flat(pixelarts_4x4["Кирка.png"])
    elif current_activity == "Обед":
        return to_flat(pixelarts_4x4["Бургер.png"])
    elif current_activity == "Завтрак":
        return to_flat(pixelarts_4x4["Завтрак.png"])
    elif current_activity == "Сон":
        return to_flat(pixelarts_4x4["Зэд.png"])
    elif current_activity == "Подъём":
        return to_flat(pixelarts_4x4["Солнце.png"])
    elif current_activity == "Книжка":
        return to_flat(pixelarts_4x4["Книга.png"])
    else:
        return to_flat(pixelarts_4x4["Штанга.png"])

async def update_pic():
    schedule_list = []

    with open('schedule.txt', 'r', encoding='utf-8') as file:
        schedule_list = []
        for i in file:
            i = str(i)
            i = i.split("-")

            schedule_list.append([i[0].strip(), i[1].strip()])

    while True:
        current_time = time.localtime(time.time() + global_variables.UTC_OFFSET)
        current_seconds = current_time[3] * 3600 + current_time[4] * 60 + current_time[5]

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

        global_variables.schedule_logic_picture = get_current_pic(current_activity)

        # print("Цикл SCHEDULE логики")
        await asyncio.sleep(15)

async def schedule_logic():
    await update_pic()