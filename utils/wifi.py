import network
import time

def connect_wifi(ssid, password):
    n = 0
    wlan = network.WLAN(network.STA_IF)  # Создаем объект для подключения к WiFi в режиме станции 😊
    wlan.active(True)  # Активируем WiFi адаптер 😊
    if not wlan.isconnected():
        print("Подключение к сети:", ssid)  # Сообщаем о попытке подключения 😊
        wlan.connect(ssid, password)  # Подключаемся к заданной сети 😊
        timeout = 100  # Максимальное время ожидания подключения в секундах 😊
        start = time.time()  # Запоминаем время начала подключения 😊
        while not wlan.isconnected() and time.time() - start < timeout:
            time.sleep(1)  # Ждем 1 секунду перед следующей проверкой 😊
            # print('try' + str(n += 1))
    if wlan.isconnected():
        print("Подключение успешно, конфигурация:", wlan.ifconfig())  # Выводим настройки сети (IP, маска, шлюз, DNS) 😊
    else:
        print("Не удалось подключиться к WiFi")  # Сообщаем о неудаче подключения 😊
    return wlan
