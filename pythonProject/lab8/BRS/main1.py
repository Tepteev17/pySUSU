from prettytable import *
import random


def brs(person: list) -> int:
    """Подсчитывает общий рейтинг за все задания у person.
    Возвращает общий рейтинг за все точки"""
    sumWeight = 0
    for i in range(1, len(person)):
        sumWeight += int(person[i][-1])

    singleWeight = 100 / sumWeight
    sum = 0
    for i in range(1, len(person)):
        sum += (int(person[i][0]) / 4) * singleWeight * int(person[i][-1])
    return sum


def readData(f, arr: list):
    """ Принимает на вход файл и список всех студентов.
        Считывает файл и заносит в arr всех студентов
    """
    for el in f:
        elems = el.split()
        fio = '%s %s %s' % (elems[0], elems[1], elems[2])
        data = [fio]
        for krm in range(3, len(elems)):
            data.append(elems[krm])
        arr.append(data)


def calcRandomScore(arr: list):
    """ Вычисляет сколько студент получил за опредленную точку.
        Значение вычисляется случайно"""
    for el in arr:
        for i in range(1, len(el)):
            el[i] = el[i].replace('0', str(random.randrange(0, 5)))


def actionPoint(point: int) -> str:
    """ Принимает на вход итоговый рейтинг point.
        Высчитывает какая оценка за дисциплину в зависимости от point."""
    if point < 59:
        return 'Неудовлетворительно'
    if point > 59 and point < 74:
        return 'Удовлетворительно'
    if point > 75 and point < 84:
        return 'Хорошо'
    return 'Отлично'


def formattedRow(person: list) -> list:
    """ Принимает на вход студента с его данными за контрольные точки.
        Формирует список(выставляет проценты за задания, общий рейтинг...)
        Возвращает список со всеми данными студента"""
    row = [person[0]]
    for i in range(1, len(person)):
        strData = ' %s       %s  ' % (str(person[i][0]), (str(int(100 * int(person[i][0]) / 4)) + '%'))
        row.append(strData)
    row.append(round(brs(person), 2))
    PA = random.randrange(0, 100)
    row.append(PA)
    rating = round(max(0.6 * brs(person) + 0.4 * PA, brs(person)), 2)
    row.append(rating)
    row.append(actionPoint(rating))
    return row


def addRows(arr: list, table):
    """Добавляет данные о студенте в таблицу"""
    table.add_row([' '] + ['Балл    Рейтинг, %']*5 + [' ']*4)
    table.add_row(['Макс.балл/вес', '4/1', '4/2', '4/3', '4/4', '4/5', ' ', ' ', ' ', ' '])
    for person in arr:
        row = formattedRow(person)
        table.add_row(row)


def main():
    """Основная программа"""
    table = PrettyTable()
    table.align = 'l'
    table.field_names = ['Фио', 'КРМ 1', 'КРМ 2', 'КРМ 3', 'КРМ 4', 'КРМ 5', 'текущий контроль всего', 'Промежуточная аттестация',
                         'Рейтинг, %', 'Оценка']
    f = open('input.txt')
    arr = []
    readData(f, arr)
    calcRandomScore(arr)
    addRows(arr, table)
    print(table)


main()