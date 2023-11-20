"""TRIANGLE.PY
    Нахождение время прибытия.
    (с) Тептеев А.Е (группа КЭ-141)
    16-окт-19
"""


def InpData():
    """Запрос у пользователя время отправления поезда: Hotp – часы и Motp – минуты. Время в
    пути: Hp – часы и Mp – минуты."""
    Hotp = int(input())
    Motp = int(input())
    Hp = int(input())
    Mp = int(input())
    return Hotp, Motp, Hp, Mp


def coorectTimeFormat(Hotp, Motp, Hp, Mp):
    if Hotp >= 23 or Motp >= 59 or Mp >= 59 or Hp < 0:
        return False
    return True


def formatTime(time):
    """Преобразует время в формат **:**"""
    time = str(time)
    if len(time) == 1:
        format = '0' + time
        return format
    else:
        return time


def calcExist(Hotp, Motp, Hp, Mp):
    endTimeH = round((Hotp + Hp) % 24, 2)
    if (Motp + Mp) / 60 >= 1:
        endTimeH += round((Motp + Mp) / 60)
    endTimeM = round((Motp + Mp) % 60, 2)
    days = Hp // 24

    return formatTime(endTimeH), formatTime(endTimeM), days


def OutData(endTimeH, endTimeM, days):
    '''Вывод времени прибытия поезда на конечную станцию в виде «HH час : MM мин».
        определить также количество полных суток в пути до конечной станции. '''
    print(endTimeH + ' hours' + ' : ' + endTimeM + ' minutes')
    print(str(days) + ' days')


"""Основная программа"""
Hotp, Motp, Hp, Mp = InpData()
if coorectTimeFormat(Hotp, Motp, Hp, Mp):
    endTimeH, endTimeM, days = calcExist(Hotp, Motp, Hp, Mp)
    OutData(endTimeH, endTimeM, days)
else:
    print('Данные введены некорректно!')


# Test 1: 12 34 56 12
# 20 hours : 46 minutes
# 2 days


# Test 2: 00 00 00 00
# 00 hours : 00 minutes
# 0 days


# Test 3: 1 1 1 1
# 02 hours : 02 minutes
#  0 days


# Test 4: 25 12 123 12
# Данные введены некорректно!


# Test 5: -12 123 123 3
# Данные введены некорректно!

# Test 6: 12 123 -123 3
# Данные введены некорректно!

# Test 7: 12 30 019 12
# 07 hours : 42 minutes
# 0 days
