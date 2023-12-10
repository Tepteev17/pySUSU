import os
import math


def readData():
    """Считывает данные из файла input.txt и возвращает список из этих чисел"""
    f = open('input.txt', 'r')
    numList = list(map(str, f.readline().split()))
    f.close()
    return numList


def actionData(numList: list):
    """Принимает на вход список numList в котором хранятся элементы из файла Input.txt и
    возвращает список [Число, Количество цифр, Сумма цифр, Произведение цифр]"""
    fullNum = int(numList[0])
    if fullNum >= 0:
        num = str(int(numList[0]))
    else:
        num = str(int(numList[0][1:]))
    dataOutput = [fullNum, len(num), sum(list(map(int, num))), math.prod(list(map(int, num)))]
    return dataOutput


def outputData(dataOutput: list):
    """Принимает на вход список dataOutput, который содержит Число, Количество цифр, Сумма цифр, Произведение цифр
    И записывает в файл соответствующие значения"""
    fileOutput.write('Число: %s\n' % dataOutput[0])
    fileOutput.write('Количество цифр: %d\n' % dataOutput[1])
    fileOutput.write('Cумма цифр: %d\n' % dataOutput[2])
    fileOutput.write('Произведение цифр: %d\n' % dataOutput[3])
    fileOutput.close()


"""Основная программа"""
nameList = os.listdir(r"C:\Users\Иван\PycharmProjects\pySUSU\pythonProject\lab6\lab6-5\lab6-5-2")
fileOutput = open('output.txt', 'w')
if 'input.txt' in nameList:
    numList = readData()
    if len(numList) != 0:
        dataOutput = actionData(numList)
        outputData(dataOutput)
    else:
        fileOutput.write('Файл пуст!')
else:
    print('Файл с входными данными не обнаружен!')
fileOutput.close()

# test 1 -12312321
# Число: -12312321
# Количество цифр: 8
# Cумма цифр: 15
#

# test 2 0
# Число: 0
# Количество цифр: 0
# Cумма цифр: 0

# test 3 0304543
# Число: 304543
# Количество цифр: 6
# Cумма цифр: 19


# test 4
# Число: -12312321
# Количество цифр: 8
# Cумма цифр: 15

# test 5 00000
# Число: 0
# Количество цифр: 1
# Cумма цифр: 0
