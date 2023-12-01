import os
import actionsModule



def coorectData(n):
    if n >= 1:
        return True


def readData():
    """Считывает данные из файла input.txt и возвращает N"""
    f = open('input.txt', 'r')
    n = int(f.readline())
    f.close()
    return n


def actionsNum(n: int):
    """Принимает параметр n - число
       Возвращает все простые числа от 1 до n"""
    actionsList = []
    for num in range(2, int(n) + 1):
        for d in range(2, num // 2 + 1):
            if num % d == 0:
                break
        else:
            actionsList.append(num)
    return str(actionsList).replace(',','')


def outputData(dataOutput: str):
    """Записывает список простых чисел в файл output.txt"""
    fileOutput.write(dataOutput[1:-1])


"""Основная программа"""
nameList = os.listdir(r"C:\Users\User\PycharmProjects\pySUSU\pythonProject\lab6\lab6-5\lab6-5-3")
fileOutput = open('output.txt', 'w')
if 'input.txt' in nameList:
    n = readData()
    if coorectData(n):
        dataOutput = actionsNum(n)
        outputData(dataOutput)
    else:
        fileOutput.write('Данные некорректны!')
else:
    print('Файл с входными данными не обнаружен!')
fileOutput.close()


# Test1: 8
# 2 3 5 7

# Test2: 40
# 2 3 5 7 11 13 17 19 23 29 31 37

# Test3: 100
# 2 3 5 7 11 13 17 19 23 29 31 37 41 43 47 53 59 61 67 71 73 79 83 89 97

# Test4: -10
# Данные некорректны!

# Test5: 1
#

# Test6: 2
# 2

# Test7:
#