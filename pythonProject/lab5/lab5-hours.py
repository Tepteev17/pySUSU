'''TRIANGLE.PY
    Нахождение время прибытия.
    (с) Тептеев А.Е (группа КЭ-141)
    16-окт-19
'''

def InpData():
    ''' Запрос у пользователявремя отправления поезда: Hotp – часы и Motp – минуты. Известно время в
    пути: Hp – часы и Mp – минуты.'''
    Hotp = int(input())
    Motp = int(input())
    Hp = int(input())
    Mp = int(input())
    return Hotp, Motp, Hp, Mp

def formatTime(time):
    """преобразует время в формат **:**"""
    time = str(time)
    if len(time) == 1:
        format = '0' + time
        return format
    else:
        return time

def calcExist(Hotp,Motp,Hp,Mp):
    endTimeH = round((Hotp + Hp) % 24, 2)
    if (Motp + Mp) / 60 >= 1:
        endTimeH += round((Motp + Mp) / 60)
    endTimeM = round((Motp + Mp) % 60, 2)
    days = Hp // 24

    return formatTime(endTimeH), formatTime(endTimeM), days

def OutData(endTimeH, endTimeM,days):
    '''Вывод времени прибытия поезда на конечную станцию в виде «HH час : MM мин».
определить также количество полных суток в пути до конечной станции. '''
    print(endTimeH + ' hours' + ' : ' + endTimeM + ' minutes')
    print(str(days) + ' days')

"""Основная программа"""
Hotp, Motp, Hp, Mp = InpData()
endTimeH, endTimeM, days = calcExist(Hotp, Motp, Hp, Mp)
OutData(endTimeH, endTimeM, days)
