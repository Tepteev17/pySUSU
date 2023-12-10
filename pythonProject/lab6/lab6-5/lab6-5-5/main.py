import random
""" main.py
    Генерирация случайной прямоугольной матрицы A
    размера NхM (N и M считываются из файла input.txt). Вывод матрицы A в
    файл. Разделение элементов каждой строки на наибольший элемент этой строки.
    Генерирация случайной прямоугольной матрицы B размера MхK (K –
    случайное число из диапазона 5..15). Вывод матрицы B в файл.
    Счет и вывод в файл произведения матриц A и B.
    (с) Тептеев А.Е (группа КЭ-141)
    24-ноя-23 """


def InpData():
    """ Считывание из файла параметров матриц N и M, а также генерация случайного параметра K"""
    f = open('input.txt', 'r')
    N, M = map(int, f.readline().split())
    K = random.randrange(5,16)
    return N, M, K


def OutData(A: list, B: list, MultiplicatedMatrix: list, K: int):
    """ Запись в файл матрицы A, матрицы B, и произведения матриц A и B. """
    f = open('output.txt', 'w')
    f.write(f'K = {K}\n')
    f.write('Матрица A:\n')
    for i in range(len(A)):
        for j in range(len(A[i])):
            f.write(str(A[i][j]) + ' ')
        f.write('\n')
    f.write('Матрица B:\n')
    for i in range(len(B)):
        for j in range(len(B[i])):
            f.write(str(B[i][j]) + ' ')
        f.write('\n')
    f.write('Матрица A*B:\n')
    for i in range(len(MultiplicatedMatrix)):
        for j in range(len(MultiplicatedMatrix[i])):
            f.write(str(MultiplicatedMatrix[i][j]) + ' ')
        f.write('\n')
    f.close()
    pass


def FirstMatrixGeneration(N: int, M: int):
    """ Генерация случайной матрицы A размером N на M"""
    A = []
    for Iterations in range(N):
        Counter = 0
        A.append([])
        Max = 0
        if len(A[Iterations]) == 0:
            while Counter < M:
                Temporary = random.randrange(0,50)
                Max = max(Max,Temporary)
                A[Iterations].append(Temporary)
                Counter += 1
    return A


def SecondMatrixGeneration(M: int, K: int):
    """ Генерация случайной матрицы B размером M на K"""
    B = []
    for Iterations in range(M):
        Counter = 0
        B.append([])
        Max = 0
        if len(B[Iterations]) == 0:
            while Counter < K:
                Temporary = random.randrange(0,50)
                Max = max(Max, Temporary)
                B[Iterations].append(Temporary)
                Counter += 1
    return B


def MatrixMultiplication(A: list, B: list, N: int, M: int, K: int):
    """ Деление элемента каждой строки матрицы A на наибольший элемент этой строки,
    Нахождение произведения матриц A и B."""
    DividedA = []
    for Iterations in range(N):
        Max = max(A[Iterations])
        DividedA.append([0] * M)
        for Elements in range(M):
            DividedA[Iterations][Elements] = A[Iterations][Elements] // Max

    MultiplicatedMatrix = []
    for Iterations in range(N):
        MultiplicatedMatrix.append([0] * K)
    for i in range(N):
        for j in range(K):
            for k in range(M):
                MultiplicatedMatrix[i][j] += DividedA[i][k] * B[k][j]
    return MultiplicatedMatrix



""" Основная программа."""
N, M, K = InpData()
A = FirstMatrixGeneration(N, M)
B = SecondMatrixGeneration(M, K)
MultiplicatedMatrix = MatrixMultiplication(A, B, N, M, K)
OutData(A, B, MultiplicatedMatrix, K)



