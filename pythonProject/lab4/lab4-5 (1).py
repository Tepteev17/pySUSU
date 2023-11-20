headers = ['Фамилия', 'Имя ', 'Отчество ', 'Дата рождения ', 'Заболевание ']
dataDct = dict()
maxLenFio = 0
for i in range(5):
    headData = ['Введите Фамилию', 'Введите Имя', 'Введите отчество ', 'Введите дату рождения ', 'Введите заболевание ']
    for e in range(5):
        dataDct[headers[e] + str(i+1)] = input(headData[e] + ' ' + str(i+1) + ': ')
        maxLenFio = max(maxLenFio, len(dataDct[headers[e] + str(i+1)]))
s = f'%-{maxLenFio+4}s'
print(s % headers[0],
      s % headers[1],
      s % headers[2],
      s % headers[3],
      s % headers[4])
for i in range(5):
    print(s % dataDct[headers[0] + str(i+1)],
          s % dataDct[headers[1] + str(i+1)],
          s % dataDct[headers[2] + str(i+1)],
          s % dataDct[headers[3] + str(i+1)],
          s % dataDct[headers[4] + str(i+1)])

''' Список - упорядоченная последовательность элементов, которые могут иметь разынй тип.
    Словарь - неупорядоченные коллекции произвольных объектов, имеющие ключ и соответствуещее значение
    Кортеж  - неизменяемый список
    2.  Воcпользоваться методом append(el)
        Воcпользоваться методом insert(len(arr)//2, el)
    3.  Воcпользоваться методом pop()
        Воспользоваться методом pop(len(arr)//2-1)
    4.  in проверяет наличие элемента в последовательности
        len используется для определения длинны последовательности
        Clear очищает список 
        index, extend, count, sort, reverse...
    5.  разность, симметрическая разность, обьединение, пересечение ...
  
  '''
