def actionsNum(n):
    """Принимает параметр n - число
        Выводит все простые числа от 2 до n
    """
    actionsList = []
    for num in range(2, int(n) + 1):
        for d in range(2, num//2 + 1):
            if num % d == 0:
                break
        else:
            actionsList.append(num)
    return str(actionsList)


