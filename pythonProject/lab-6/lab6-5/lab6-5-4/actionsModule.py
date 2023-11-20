def actions(r, x, y):
    """ѕринимает r - радиус, x - координата х, y - координата y.
        ѕодсчитывает сколько точек с целочисленными
        координатами попадает в круг радиуса R с центром в точке (x,y)
    """
    cnt = 0
    for i in range(x-r, x+r+1):
        for j in range(y-r, y+r+1):
            if (i**2 + j**2) <= r**2:
                cnt += 1
    return cnt


print(actions(4, 0, 0))
