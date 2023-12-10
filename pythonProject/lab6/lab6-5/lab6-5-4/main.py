import time
from datetime import datetime
from actions_module import *
""" main.py
    Нахождение количества точек с целочисленными
    координатами, попадающих в круг радиуса R с центром в точке (x,y).
    Вывод сегодняшней даты, времени начала работы программы и времени выполнения в секундах.
    Входные данные считываются из файла input.txt.
    Выходные данные записываются в файл output.txt.
    (с) Тептеев А.Е (группа КЭ-141)
    24-ноя-23 """


def InpData():
    """ Считывание из файла input.txt данных о круге радиуса R с центром в точке (x,y)."""
    f = open('input.txt', 'r')
    R = int(f.readline())
    x, y = map(int, f.readline().split())
    f.close()
    return R, x, y


def OutData(Counter: int, Time: float):
    """ Запись в файл сегодняшней даты, времени начала работы программы и времени выполнения в секундах"""
    f = open('output.txt', 'w')
    CurrentTime = datetime.now()
    if len(str(CurrentTime.day)) == 1:
        if len(str(CurrentTime.month)) == 1:
            f.write('0' + str(CurrentTime.day) + '.0' + str(CurrentTime.month) + '.' + str(CurrentTime.year) +
                    ' ' + str(CurrentTime.hour) + ':' + str(CurrentTime.minute) + '\n')
        else:
            f.write('0' + str(CurrentTime.day) + '.' + str(CurrentTime.month) + '.' + str(CurrentTime.year) +
                    ' ' + str(CurrentTime.hour) + ':' + str(CurrentTime.minute) + '\n')
    else:
        if len(str(CurrentTime.month)) == 1:
            f.write(str(CurrentTime.day) + '.0' + str(CurrentTime.month) + '.' + str(CurrentTime.year) +
                    ' ' + str(CurrentTime.hour) + ':' + str(CurrentTime.minute) + '\n')
        else:
            f.write(str(CurrentTime.day) + '.' + str(CurrentTime.month) + '.' + str(CurrentTime.year) +
                    ' ' + str(CurrentTime.hour) + ':' + str(CurrentTime.minute) + '\n')
    f.write(str(int(Counter)) + '\n')
    f.write(str(Time))
    f.close()
    pass



""" Основная программа. Тут же подсчет времени работы."""
StartTime = time.time()
R, x, y = InpData()
Counter = PointsCounter(R)
EndTime = time.time()
Time = EndTime - StartTime
OutData(Counter, Time)

