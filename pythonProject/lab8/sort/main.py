from sorts import *
import time
import copy
from sys import setrecursionlimit
from prettytable import *
import random


def generateLists(n: int):
    """ Создание трех последовательностей размера N:
        Случайно сгенерированной
        Отсортированной
        Отсортированной в обратном порядке."""
    arrGenerate = []
    for i in range(n):
        arrGenerate.append(random.randrange(-100000, 100000))
    arrGenerateCopy1 = copy.copy(arrGenerate)
    arrGenerateCopy2 = copy.copy(arrGenerate)
    arrSorted = sorted(arrGenerate)
    arrRevSorted = sorted(arrGenerate, reverse=True)

    return arrSorted, arrRevSorted, arrGenerate, arrGenerateCopy1, arrGenerateCopy2


def exchangeSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """Принимает случайно сгенерированный список arrGenerate и сущность таблицы
    Выполняет сортировку методом перестановки(пузырька) и
    записывает данные о времени выполнения в таблицу"""

    timeCompArr = []
    for arr in [arrSorted, arrGenerate, arrRevSorted]:
        start_time = time.time()
        sortedArr = exchangeSort(arr)
        check(arr, sortedArr)
        end_time = time.time()
        timeComp = end_time - start_time
        timeCompArr.append(timeComp)
    addNewRow(table, ['Сортировка пузырьком', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def shellSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerateCopy1: list, table):
    """Принимает случайно сгенерированный список arrGenerateCopy1 и сущность таблицы
        Выполняет сортировку методом Шелла и
        записывает данные о времени выполнения в таблицу"""

    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy1, arrRevSorted]:
        start_time = time.time()
        sortedArr = shellSort(arr)
        check(arr, sortedArr)
        end_time = time.time()
        timeComp = end_time - start_time
        timeCompArr.append(timeComp)
    addNewRow(table, ['Сортировка Shella', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def quickSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerateCopy2: list, table):
    """Принимает случайно сгенерированный список arrGenerateCopy2 и сущность таблицы
        Выполняет сортировку методом Быстрой сортировки и
        записывает данные о времени выполнения в таблицу"""
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy2, arrRevSorted]:
        start_time = time.time()
        sortedArr = quickSort(arr)
        check(arr, sortedArr)
        end_time = time.time()
        timeComp = end_time - start_time
        timeCompArr.append(timeComp)

    addNewRow(table, ['Быстрая сортировка', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def builtSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerateCopy2: list, table):
    """Принимает случайно сгенерированный список arrGenerateCopy2 и сущность таблицы
        Выполняет сортировку методом встроенной сортировки и
        записывает данные о времени выполнения в таблицу"""
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy2, arrRevSorted]:
        start_time = time.time()
        sortedArr = builtSort(arr)
        check(arr, sortedArr)
        end_time = time.time()
        timeComp = end_time - start_time
        timeCompArr.append(timeComp)

    addNewRow(table, ['Встроенная сортировка', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def selectionSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerateCopy2: list, table):
    """ Принимает случайно сгенерированный список arrGenerateCopy2 и сущность таблицы
        Выполняет сортировку методом выбора и
        записывает данные о времени выполнения в таблицу"""
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy2, arrRevSorted]:
        start_time = time.time()
        sortedArr = selectionSort(arr)
        check(arr, sortedArr)
        end_time = time.time()
        timeComp = end_time - start_time
        timeCompArr.append(timeComp)

    addNewRow(table, ['Сортировка выбором', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def mergeSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerateCopy2: list, table):
    """ Принимает случайно сгенерированный список arrGenerateCopy2 и сущность таблицы
        Выполняет сортировку методом слияния и
        записывает данные о времени выполнения в таблицу"""
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy2, arrRevSorted]:
        start_time = time.time()
        sortedArr = mergeSort(arr)
        check(arr, sortedArr)
        end_time = time.time()
        timeComp = end_time - start_time
        timeCompArr.append(timeComp)

    addNewRow(table, ['Сортировка Слиянием', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def addNewRow(table: list, row: list):
    """Принимает сущность таблицы и список, который нужно добавить в строку
    Добавляет строку в таблицу"""
    table.add_rows([row])


def outData(table, f):
    """Принимает сущность таблицы и файл.
    Выводит таблицы в файл"""
    print(table, file=f, sep='\n')


# Основная программа
setrecursionlimit(10000)
table = PrettyTable()
table.field_names = ["Метод", "отсортированная", "случайная", "отсортированная в обратном порядке"]
n = int(input('Введите число N: '))
f = open('output.txt', 'w')

arrSorted, arrRevSorted, arrGenerate, arrGenerateCopy1, arrGenerateCopy2 = generateLists(n)

exchangeSortProcedure(arrSorted, arrRevSorted, arrGenerate, table)
shellSortProcedure(arrSorted, arrRevSorted, arrGenerateCopy1, table)
quickSortProcedure(arrSorted, arrRevSorted, arrGenerateCopy2, table)
builtSortProcedure(arrSorted, arrRevSorted, arrGenerateCopy2, table)
selectionSortProcedure(arrSorted, arrRevSorted, arrGenerateCopy2, table)





mergeSortProcedure(arrSorted, arrRevSorted, arrGenerateCopy2, table)
outData(table, f)
