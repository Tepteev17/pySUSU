if __name__ == "__main__":
    import os
    import math
    nameList = os.listdir(r"C:\Users\Tepteevae\PycharmProjects\pythonProject\lab-6\lab6-5\lab6-5-2")
    fileOutput = open('output.txt', 'w')
    if 'input.txt' in nameList:
        f = open('input.txt')
        numList = list(map(str, f.readline().split()))
        if len(numList) != 0:
            fullnum = int(numList[0])
            num = str(int(numList[0][1:]))
            fileOutput.write('Чсло: %s\n' % fullnum)
            fileOutput.write('Количество цифр: %d\n' % len(num))
            fileOutput.write('Cумма цифр: %d\n' % sum(list(map(int, num))))
            # fileOutput.write('Произведение цифр: %d\n' % math.prod(list(map(int, num))))
        else:
             fileOutput.write('Файл пуст!')
    else:
        print('Файл с входными данными не обнаружен!')

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
