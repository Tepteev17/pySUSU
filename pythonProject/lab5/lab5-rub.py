'''TRIANGLE.PY
    Нахождение время прибытия.
    (с) Тептеев А.Е (группа КЭ-141)
    16-окт-19
'''

def inpData():
    ''' Получает на вход кол-во копеек'''
    pen =  int(input('Введите кол-во копеек: '))
    return pen
def confToNum(pen):
    """Сичтает количество рублей и копеек и возвращает cntRUB и pen соответственно"""
    qntRUB = pen // 100
    qntPen = pen % 100
    return qntRUB, qntPen

def compGenus(qntRUB, qntPen):
    genusRUB = ''
    genusPen = ''
    if str(qntRUB)[-1] in '234':
        genusRUB = 'РУБЛЯ'
        pass
    elif str(qntRUB)[-2:] in ('11', '12', '13', '14','15', '16', '17', '18','19','20'):
        genusRUB = 'РУБЛЕЙ'
        pass
    elif str(qntRUB)[-1] in "1":
        genusRUB = 'РУБЛЬ'
        pass
    else:
        genusRUB = 'РУБЛЕЙ'



    if str(qntPen)[-1] in '234':
        genusPen = 'КОПЕЙКИ'
        pass
    elif str(qntPen)[-2:] in ('11', '12', '13', '14','15', '16', '17', '18','19','20'):
        genusPen = 'КОПЕЕК'
        pass
    elif str(qntPen)[-1] in '1':
        genusPen = 'КОПЕЙКА'
        pass
    else:
        genusPen = 'КОПЕЕК'
    return genusRUB, genusPen

def outData(qntRUB, qntPen,genusRUB, genusPen):
    '''Вывод Количества рублей и копеек в соответствии с падежом'''
    print(str(qntRUB) + " " + genusRUB)
    print(str(qntPen) + " " + genusPen)

"""Основная программа"""
pen = inpData()
qntRUB, qntPen = confToNum(pen)
genusRUB, genusPen = compGenus(qntRUB, qntPen)
outData(qntRUB, qntPen,genusRUB, genusPen)
