#!/usr/bin/python3

# Выполнение 100 000 операций имитационного
#Моделирования, для реализации займет много времени
#Вывод сообщений о каждых 10 000 операций
#Обратная связь демонстирует пользователю, что
#программа не зависла.
import datetime, random

#Возвращение списка объектов дат
# дней рождения
def getBirthdays(numberOfBirthdays):
    birthdays = []
    for i in range(numberOfBirthdays):
        #Год в имитации роли не играет
        # ,лишь бы в объектах дней рождения он был одинаков
        startOfYear = datetime.date(2025, 1, 1)
        #Получаем случайный день года
        randomNumberOfDays = datetime.timedelta(random.randint(0,364))
        birthday = startOfYear + randomNumberOfDays
        birthdays.append(birthday)
    return birthdays
#для возвращения объектов даты для рождения, в кот. встречаются несколько раз
#в списке дней рождения
def getMatch(birthdays):
    if len(birthdays) == len(set(birthdays)):
        return None #Нет одинаковых дней рождения
    for a, birthdayA in enumerate(birthdays):
        for b, birthdayB in enumerate(birthdays[a+1 :]):
            if birthdayA == birthdayB:
                return birthdayA #Возвращаем найденые соответствия
#MAIN
MONTHS = ("Jan","Feb","Mar","Apr","May","Jun","Jul",
          "Aug",'Sep',"Oct","Nov","Dec")
while True:
    response = int(input("Сколько дней рождения будем создавать?(Макс 100):"))
    if response > 0 and response <= 100:
        numBDays = response
        break
print()
birthdays = getBirthdays(numBDays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ",end='')
    monthName = MONTHS[birthday.month - 1]
    dateText = f"{monthName, birthday.day}"
    print(dateText)
print()
print()
#делаем проверку на совпадения
math = getMatch(birthdays)
#Отображаем результаты
print("Результаты симуляции:",end='')
if math != None:
    monthName = MONTHS[math.month - 1]
    dateText =  f"{monthName, math.day}"
    print(f"Люди имеющие такую дату: {dateText}")
else:
    print("Не удалось найти людей с такой датой")
print()
#Делаем 100 000 операций имитации
print("Начинается проверка 100 000 вариаций")
input("Нажмите Enter, чтобы начать...")
simMatch = 0 #Числом операций моделировани с совпадающими датами
for i in range(100000):
    if i % 10000 == 0:
        print(i, 'Симуляция идет...')
    birthdays = getBirthdays(numBDays)
    if getMatch(birthdays) != None:
        simMatch += 1
print("Симуляция успешно закончена!")
print(f"Дней рождений: {numBDays}")
print(f"Кол-во совпадений: {simMatch}")

