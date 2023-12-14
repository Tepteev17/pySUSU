def inputData():
    """Считывает данные с файла input.txt"""
    f = open('input.txt')
    string = ''.join(f.readlines())
    arr = []
    return string, arr


def reverseRecursive(string: str, lenght: int, arr: list):
    """Рекурсивная функция, которая берет элемент по индексу строки и добавляет его в arr"""
    if lenght >= 0:
        arr.append(string[lenght])
        reverseRecursive(string, lenght - 1, arr)


def outputData(string: str):
    """Вывоводит в файл строку string"""
    f = open('output.txt', 'w')
    print(string, file=f)


def main():
    """Основная программа"""
    string, arr = inputData()
    reverseRecursive(string, len(string) - 1, arr)
    revString = ''.join(arr)
    outputData(revString)


main()
