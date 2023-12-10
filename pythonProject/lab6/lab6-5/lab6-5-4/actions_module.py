def PointsCounter(R: int):
    """ Нахождение количества точек с целочисленными
    координатами, попадающих в круг радиуса R с центром в точке (x,y)"""
    Counter = 0
    SquareR = R ** 2
    for Number in range(R + 1):
        Counter += int((SquareR - Number ** 2) ** 0.5)
    return Counter * 4 + 1