def inCorrectData(a: int, b=1):
    """ Проверяет корекктность введеных значений a и b
    """
    if a <= 0 or b <= 0:
        print('Данные некоректны!')
        return


def printRectangle(a: int, b: int, file=False):
    """"Принимает параметры а - ширина, b- длинна, file - название файла
        печатает в файл с именем file
        прямоугольник из символов * со сторонами a и b
    """
    inCorrectData(a, b)
    f = open(file, 'w')
    for i in range(1, a+1):
        if i == 1 or i == a:
            f.write(b*'* ' + '\n')
        else:
            f.write('*' + '  '*(b-2) + ' *' + '\n')
    f.close()


def PrintSquare(a: int, file=False):
    """"Принимает параметры а - ширина и высота, file - название файла
        печатает в файл с именем file
        прямоугольник из символов * со стороной а
    """
    inCorrectData(a)
    f = open(file, 'w')
    for i in range(1, a+1):
        f.seek(0, 2)
        if i == 1 or i == a:
            f.write(a*'*  ' + '\n')
        else:
            f.write('* ' + '   '*(a-2) + ' *' + '\n')
    f.close()
