from prettytable import PrettyTable 

table = PrettyTable()
table.field_names = ['Фамилия', 'Имя ', 'отчество ', 'дата рождения ', 'заболевание ']
for i in range(5):
    dataDct = {}
    headData = ['Введите Фамилию', 'Введите Имя', 'Введите отчество ', 'Введите дату рождения ', 'Введите заболевание ']
    for head in headData:
        dataDct[table.field_names[headData.index(head)]] = input(head + str(i+1))
    table.add_row(dataDct.values())

print(table)
