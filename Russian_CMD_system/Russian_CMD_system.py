import time

print("запуск системы")
time.sleep(1)
print("загрузка...")
time.sleep(0.5)
ram1 = "16gb"
rom1 = "128gb"
print("RAM:" + ram1)
print("ROM:" + rom1)
time.sleep(1)
print("РУССКАЯ СИСТЕМА")
print("ВЕРСИЯ 1.0")
input("ДОБРО ПОЖАЛОВАТЬ ИВАН ВЕДИТЕ ПАРОЛЬ:")
print("ДОБРО ПОЖАЛОВАТЬ ИВАН")
time.sleep(2)
while True:
    command1 = input("ВЕДИТЕ КОМАНДУ:")
    if command1 == "systeminfo":
        print("РУССКАЯ СИСТЕМА ВЕРСИИ 1.0")
        print("БЕТА ВВЕРСИЯ")
        print("ПРОИЗВОДИТЕЛЬ ИВАН ДЕГТЕВ")
    if command1 == "bankreg":
        print("НОМЕР КАРТЫ 2202 2023 3241 7249")
        print("ДО 06/27")
        print("CVC 155")
        input("ДЛЯ ПЕРЕВОДА ВВЕДИТЕ НОМЕР КАРТЫ ИЛИ НОМЕР ТЕЛЕФОНА И НАЖМИ НА ВВОД ИЛИ НА ENTER:")
        input("И.ДЁГТЕВ ЕСЛИ ВСЕ ВЕРНО ТО ВВЕДИТЕ СУММУ И НАЖМИТЕ НА ВВОД ИЛИ enter:")
        print("ОТПРАВЛЕНО")
    if command1 == "bluetoothon":
        print("ДОСТУПНО:jbl xtrim2,carbt,jbl clip3,Часы.")
        print("ПОДКЛЮЧЕНО К УСТРОЙСТВУ ЧАСЫ")
    if command1 == "bluetoothoff":
        print("BLUETOOTH ВЫКЛЮЧЕН")
    if command1 == "wi-fion":
        print("ДОСТУПНЫЕ СЕТИ wi-fi ДОМ")
        print("ПОДКЛЮЧЕНИЕ К ДОМУ")
        print("ПОДКЛЮЧЕНО")
    if command1 == "wi-fioff":
        print("wi-fi ВЫКЛЮЧЕН")
    if command1 == "telefon":
        input("ВЕДИТЕ НОМЕР И НАЖМИ НА ВВОД ИЛИ ENTER:")
        print("ВЫЗОВ")
        time.sleep(5)
        print("ГОВОРИТЕ")
        time.sleep(60)
        print("СБРОС")
    if command1 == "sms":
        input("ВЕДИТЕ НОМЕР И НАЖМИ НА ВВОД ИЛИ ENTER:")
        input("ВВЕДИ СООБЩЕНИЕ И НАЖМИ НА ВВОД ИЛИ ENTER: ")
        print("Привет")
        time.sleep(2)
        input("ВВЕДИ СООБЩЕНИЕ:")
        time.sleep(3)
        print("Скинь д/з пж")
        input("ВВЕДИ СООБЩЕНИЕ:")
        time.sleep(2)
        print("Спасибо")
        input("ВВЕДИ СООБЩЕНИЕ:")
        time.sleep(2)
        print("Пока")
    if command1 == "on-off":
        print("ПЕРЕЗАГРУЗКА...")
        time.sleep(5)
        print("ЗАПУСК СИСТЕМЫ")
        time.sleep(1)
        print("ЗАГРУЗКА...")
        time.sleep(0.5)
        print("RAM:" + ram1)
        print("ROM:" + rom1)
        time.sleep(1)
        input("ЗДРАВСТВУЙТЕ ИВАН ВЕДИТЕ ПОРОЛЬ:")
        print("ДОБРО ПОЖАЛОВАТЬ ИВАН")
    if command1 == "taxi":
        input("ДЛЯ ЗАКАЗА ТАКСИ НАЖМИТЕ НА ВВОД ВСЕ ТАКСИ СТОИТ 60₽")
        print("ПОИСК")
        time.sleep(10)
        print("МАШИНА НАЙДЕНА НОМЕР ЕН453Пru190")
        time.sleep(30)
        print("МАШИНА ПРИЕХАЛА")
        time.sleep(60)
        print("СПАСИБО ЧТО ВЫБРАЛИ НАС")
        input("ОЦЕНИТЕ НАС ОТ 1 ДО 10:")
    if command1 == "callback":
        input("ДЛЯ ЗАПРОСА ПОЗВОНИТЬ ВАМ ВЕДИТЕ ВАШ НОМЕР ТЕЛЕФОНА И НАЖМИТЕ ВВОД ИЛИ ENTER:")
        print("ОЖИДАЙТЕ 10 СЕК")
        time.sleep(10)
        input("ВАМ ЗВОНИТ +7(495)568-88-90 АОН(SYSTEM_CREATOR) ЧТОБЫ ОТВЕТИТЬ НАЖМИТЕ НА ENTER ИЛИ ВВОД СБРОСА ВЫЗОВА НЕТ!")
        print("ГОВОРИТЕ ДО 50 СЕК")
        time.sleep(50)
        print("Сброс вызова")
    if command1 == "App-store":
        print("WhatsApp-40mb number-1")
        print("IME-100mb number-2")
        print("CS2-15gb number-3")
        input("КАКОЕ ПРИЛОЖЕНИЕ:")
        print("Установка…")
        time.sleep(2)
        print("-")
        time.sleep(2)
        print("—")
        time.sleep(2)
        print("—-")
        time.sleep(2)
        print("——")
        time.sleep(2)
        print("——-")
        time.sleep(2)
        print("———")
        time.sleep(2)
        print("———-")
        time.sleep(2)
        print("————")
        time.sleep(5)
        print("————-")
        time.sleep(10)
        print("УСТАНОВКА ЗАВЕРШЕНА")
