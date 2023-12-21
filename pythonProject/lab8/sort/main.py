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
    arrSorted = sorted(arrGenerate)
    arrRevSorted = sorted(arrGenerate, reverse=True)

    return arrSorted, arrRevSorted, arrGenerate


def exchangeSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """Принимает случайно сгенерированный список arrGenerate и сущность таблицы
    Выполняет сортировку методом перестановки(пузырька) и
    записывает данные о времени выполнения в таблицу"""
    isSorted = True
    arrGenerateCopy = copy.copy(arrGenerate)
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy, arrRevSorted]:
        start_time = time.time()
        sortedArr = exchangeSort(arr)
        if check(sortedArr, arrSorted):
            end_time = time.time()
            timeComp = end_time - start_time
            timeCompArr.append(timeComp)
        else:
            isSorted = False
    if isSorted:
        addNewRow(table, ['Сортировка пузырьком', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def shellSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """Принимает случайно сгенерированный список  и сущность таблицы
        Выполняет сортировку методом Шелла и
        записывает данные о времени выполнения в таблицу"""
    isSorted = True
    arrGenerateCopy = copy.copy(arrGenerate)
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy, arrRevSorted]:
        start_time = time.time()
        sortedArr = shellSort(arr)
        if check(sortedArr, arrSorted):
            end_time = time.time()
            timeComp = end_time - start_time
            timeCompArr.append(timeComp)
        else:
            isSorted = False
    if isSorted:
        addNewRow(table, ['Сортировка Shella', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def quickSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """Принимает случайно сгенерированный список  и сущность таблицы
        Выполняет сортировку методом Быстрой сортировки и
        записывает данные о времени выполнения в таблицу"""
    isSorted = True
    arrGenerateCopy = copy.copy(arrGenerate)
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy, arrRevSorted]:
        start_time = time.time()
        sortedArr = quickSort(arr)
        if check(sortedArr, arrSorted):
            end_time = time.time()
            timeComp = end_time - start_time
            timeCompArr.append(timeComp)
        else:
            isSorted = False

    if isSorted:
        addNewRow(table, ['Быстрая сортировка', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


#  //////////////////////
def builtSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """Принимает случайно сгенерированный список и сущность таблицы
        Выполняет сортировку методом встроенной сортировки и
        записывает данные о времени выполнения в таблицу"""
    isSorted = True
    arrGenerateCopy = copy.copy(arrGenerate)
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy, arrRevSorted]:
        start_time = time.time()
        sortedArr = builtSort(arr)
        if check(sortedArr, arrSorted):
            end_time = time.time()
            timeComp = end_time - start_time
            timeCompArr.append(timeComp)
        else:
            isSorted = False

    if isSorted:
        addNewRow(table, ['Встроенная сортировка', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def selectionSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """ Принимает случайно сгенерированный список  и сущность таблицы
        Выполняет сортировку методом выбора и
        записывает данные о времени выполнения в таблицу"""
    isSorted = True
    arrGenerateCopy = copy.copy(arrGenerate)
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy, arrRevSorted]:
        start_time = time.time()
        sortedArr = selectionSort(arr)
        if check(sortedArr, arrSorted):
            end_time = time.time()
            timeComp = end_time - start_time
            timeCompArr.append(timeComp)
        else:
            isSorted = False

    if isSorted:
        addNewRow(table, ['Сортировка выбором', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def sortSimpleInsertsProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """ Принимает случайно сгенерированный список и сущность таблицы
        Выполняет сортировку методом простых вставок и
        записывает данные о времени выполнения в таблицу"""
    isSorted = True
    arrGenerateCopy = copy.copy(arrGenerate)
    timeCompArr = []
    for arr in [arrSorted, arrGenerateCopy, arrRevSorted]:
        start_time = time.time()
        sortedArr = sortSimpleInserts(arr)
        if check(sortedArr, arrSorted):
            end_time = time.time()
            timeComp = end_time - start_time
            timeCompArr.append(timeComp)
        else:
            isSorted = False

    if isSorted:
        addNewRow(table, ['Сортировка простыми вставками', timeCompArr[0], timeCompArr[1], timeCompArr[2]])


def mergeSortProcedure(arrSorted: list, arrRevSorted: list, arrGenerate: list, table):
    """ Принимает случайно сгенерированный список arrGenerateCopy2 и сущность таблицы
        Выполняет сортировку методом слияния и
        записывает данные о времени выполнения в таблицу"""
    arrGenerateCopy = copy.copy(arrGenerate)
    timeCompArr = []
    isSorted = True
    for arr in [arrSorted, arrGenerateCopy, arrRevSorted]:
        start_time = time.time()
        sortedArr = mergeSort(arr)
        if check(sortedArr, arrSorted):
            end_time = time.time()
            timeComp = end_time - start_time
            timeCompArr.append(timeComp)
        else:
            isSorted = False
    if isSorted:
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

arrSorted, arrRevSorted, arrGenerate = generateLists(n)

exchangeSortProcedure(arrSorted, arrRevSorted, arrGenerate, table)
shellSortProcedure(arrSorted, arrRevSorted, arrGenerate, table)
quickSortProcedure(arrSorted, arrRevSorted, arrGenerate, table)
builtSortProcedure(arrSorted, arrRevSorted, arrGenerate, table)
selectionSortProcedure(arrSorted, arrRevSorted, arrGenerate, table)
mergeSortProcedure(arrSorted, arrRevSorted, arrGenerate, table)
sortSimpleInsertsProcedure(arrSorted, arrRevSorted, arrGenerate, table)
outData(table, f)
