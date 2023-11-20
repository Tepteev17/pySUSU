if __name__ == "__main__":
    import os
    import moduleActionsNum
    nameList = os.listdir(r"C:\Users\Tepteevae\PycharmProjects\pythonProject\lab-6\lab6-5\lab6-5-3")
    fileOutput = open('output.txt', 'w')
    if 'input.txt' in nameList:
        f = open('input.txt')
        numList = list(map(str, f.readline().split()))
        if len(numList) > 0:
            n = int(numList[0])
            if moduleActionsNum.coorectData(n):
                arr = str(moduleActionsNum.actionsNum(n)[1:-1])
                fileOutput.write(arr)
            else:
                fileOutput.write('Данные некорректны!')
        elif len(numList) == 0:
            fileOutput.write('Файл пуст!')
    else:
        print('Файл с входными данными не обнаружен!')
