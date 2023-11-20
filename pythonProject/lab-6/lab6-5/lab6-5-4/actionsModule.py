def actions(r,x,y):
    """��������� r - ������, x - ���������� �,y - ���������� y
        ������� ������� ����� � ��������������
        ������������ �������� � ���� ������� R � ������� � ����� (x,y)
    """
    cnt = 0
    for i in range(x-r, x+r+1):
        for j in range(y-r, y+r+1):
            if (i**2 + j**2) <= r**2:
                cnt += 1
    return cnt


print(actions(4, 0, 0))
