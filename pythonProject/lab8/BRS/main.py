from prettytable import PrettyTable
import random

table = PrettyTable()
table.field_names = ['Фио', '1', '2', '3', '4', '5', 'текущий контроль всего', 'Промежуточная аттестация', 'Рейтинг, %', 'Оценка']

f = open('input.txt')
arr = []

def brs(person):
    sumWeight = 0
    for i in range(1, len(person)):
        sumWeight += int(person[i][-1])

    singleWeight = 100/sumWeight
    sum = 0
    for i in range(1, len(person)):
        sum += (int(person[i][0])/4)*singleWeight*int(person[i][-1])
    return sum

for el in f:
    arr.append(el.split())

for el in arr:
    for i in range(1, len(el)):
        el[i] = el[i].replace('0', str(random.randrange(0, 5)))
def actionPoint(point):
    if point < 59:
        return 'Неудовлетворительно'
    if point > 59 and point < 74:
        return 'Удовлетворительно'
    if point > 75 and point < 84:
        return 'Хорошо'
    return 'Отлично'

def formattedRow(person):
    print(person)
    row = [person[0]]
    for i in range(1, len(person)):
        row.append(str(person[i][0]) + " | " + (str(int(100*int(person[i][0])/4)))+'%')
    row.append(round(brs(person), 2))
    PA = random.randrange(0, 100)
    row.append(PA)
    rating = round(max(0.6*brs(person) + 0.4*PA, brs(person)), 2)
    row.append(rating)
    row.append(actionPoint(rating))
    print(row)
    return row


for person in arr:
    row = formattedRow(person)
    table.add_row(row)

print(table)
