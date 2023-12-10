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
    # gap = len(arr) // 4
    # while gap != 0:
    #     for i in range(len(arr) - gap):
    #         print(arr[i])
    #         if arr[i] > arr[i + gap]:
    #             arr[i], arr[i + gap] = arr[i + gap], arr[i]
    #     gap = gap // 2
    # return arr
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