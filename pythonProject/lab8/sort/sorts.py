import random


def check(unsortedArr, sortedArr) -> bool:
    """Принимает неотсортированный список unsortedArr и отсортированный список sortedArr.
    Проверяет отсортирвоался ли список"""
    if unsortedArr != sortedArr:
        return True
    return False


def exchangeSort(arr: list) -> list:
    """Принимает неотсортированный список arr.
        Возвращает остортированный список методом перестановки"""

    for run in range(len(arr)-1):
        for i in range(len(arr)-1):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
    return arr


def shellSort(arr: list) -> list:
    """Принимает неотсортированный список arr.
        Возвращает остортированный список методом Шелла"""
    a = [9, 5, 3, 2, 1]
    n = len(arr)
    for k in range(5):
        gap = a[k]
        for i in range(gap, n):
            temp = arr[i]
            j = i - gap
            while j >= 0 and temp < arr[j]:
                arr[j + gap] = arr[j]
                j -= gap
            arr[j + gap] = temp
    return arr

def quickSort(arr: list) -> list:
    """Принимает неотсортированный список arr.
        Возвращает остортированный список методом Быстрой сортировки"""
    if len(arr) <= 1:
        return arr
    else:
        q = random.choice(arr)
        left = [elem for elem in arr if elem < q]
        center = [q] * arr.count(q)
        right = [elem for elem in arr if elem > q]
        return quickSort(left) + center + quickSort(right)


def sortSimpleInserts(arr: list) -> list:
    """Принимает неотсортированный список arr.
        Возвращает остортированный список методом простых вставок"""
    for i in range(0, len(arr)):
        currValue = arr[i]
        position = i

        while position > 0 and currValue < arr[position - 1]:
            arr[position], arr[position - 1] = arr[position - 1], arr[position]
            position -= 1

    return arr

def builtSort(arr: list) -> list:
    """Сортирует последовательность arr встроенным методом sorted"""
    return sorted(arr)


def selectionSort(arr: list) -> list:
    """Принимает неотсортированный список arr.
        Возвращает остортированный список остортированный с помощью мпетода сортировка выобра"""
    for i in range(len(arr)):
        minValue = i

        for j in range(i, len(arr)):
            if arr[minValue] < arr[j]:
                minValue = j
    arr[minValue], arr[i] = arr[i], arr[minValue]

    return arr

def splitСonsistency(arr: list) -> list:
    """Разбивает массив на 2 части и возвращает отсортированную часть"""
    if len(arr) == 1:
        return arr
    middle = len(arr) // 2
    leftList = arr[:middle]
    rightlist = arr[middle:]

    leftList = splitСonsistency(leftList)
    rightlist = splitСonsistency(rightlist)

    return list(mergeConsistency(leftList, rightlist))

def mergeConsistency(leftList: list, rightlist: list) -> list:
    """Сортирует две части разделенного массива и склеивает их в одну"""
    subsequence = []

    while len(leftList) != 0 and len(rightlist) != 0:
        if leftList[0] > rightlist[0]:
            subsequence.append(rightlist[0])
            rightlist.remove(rightlist[0])
        else:
            subsequence.append(leftList[0])
            leftList.remove(leftList[0])

    if len(leftList) == 0 and len(rightlist) != 0:
        subsequence += rightlist
    else:
        subsequence += leftList

    return subsequence


def mergeSort(arr: list) -> list:
    """Выполняет сортировку последовательности методом слияния"""
    return splitСonsistency(arr)
