def power(a, b):
    """Возвращает результат возведения числа a в степень b
        a - основание
        b - степень
    """
    if a == 0:
        return 0
    
    if b == 0:
        return 1

    if b < 0:
        return 1/a*power(a, b+1)
    else:
        return a*power(a, b-1)
