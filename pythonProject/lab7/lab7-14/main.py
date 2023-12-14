def inputData():
    """Считывает данные с файла input.txt"""
    f = open('input.txt')
    string = ''.join(f.readlines())
    stack = []
    dictStaple = {'[': ']', '{': '}', '<': '>', '(': ')'}
    return string[:-1], stack, dictStaple


def recursionStaple(string: str, lenght: int, stack: list, dictStaple: dict):
    """Рекурсивная функция, которая проверяет string на верность последовательности цепочки"""
    el = string[len(string) - 1 - lenght]
    if lenght >= 0:
        if el in '[{<(':
            stack.append(dictStaple[el])
        elif el == stack[-1]:
            stack.remove(el)
        else:
            return

        if lenght == 0:
            return
        recursionStaple(string, lenght - 1, stack, dictStaple)


def outputData(lenStack: int):
    """Вывоводит в файл строку string"""
    f = open('output.txt', 'w')
    if lenStack == 0:
        print('YES', file=f)
        return
    print('NO', file=f)


def main():
    """Основная программа"""
    string, stack, dictStaple = inputData()
    if len(string) < 200:
        recursionStaple(string, len(string) - 1, stack, dictStaple)
        outputData(len(stack))
    else:
        print('Некорректные данные!')


main()
