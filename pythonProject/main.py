"""hashing"""
# task 1
books = ["Война и мир","Война и мир", "Преступление и наказание", "Гарри Поттер и философский камень",
         "Мастер и Маргарита", "1984", "Анна Каренина", "Убить пересмешника"]
hashTable = [''] * len(books)


def hashFunctionMediumSquare(lastNameBook):
    """Помещает в хеш таблицу 7 книг методом средних квадратов (по
    названию книги)"""
    summ = 0
    for el in lastNameBook:
        weight = lastNameBook.index(el) + 1
        code = ord(el)
        summ += code * weight

    hashValue = int(str(summ ** 2)[len(str(summ ** 2)) // 2 - 1:len(str(summ ** 2)) // 2 + 2]) % len(books)
    return hashValue


for el in books:
        hashTable.insert(hashFunctionMediumSquare(el), el)

print(hashTable)






# task 2
books2 = ['Stephen King', 'J.K. Rowling', 'Haruki Murakami', 'Agatha Christie', 'Gabriel Garcia Marquez',
          'Toni Morrison', 'Neil Gaiman']
hashTable2 = [''] * len(books2)
def hashFunctionRolls(lastNameBook):
    """Помещает в хеш таблицу 7 книг методом свертки (по фамилии автора)"""
    summ = 0
    for i in range(0, len(lastNameBook)-1, 2):
        sumCodes = ord(lastNameBook[i]) + ord(lastNameBook[i+1])
        summ += sumCodes

    hashValue = summ % len(books2)
    return hashValue


for el in books2:
        hashTable2[hashFunctionRolls(el)] = el

print(hashTable2)

# task 3

books3 = [
    ('The Shining', '1977'),
    ('Harry Potter and the Sorcerer\'s Stone', '1997'),
    ('Norwegian Wood', '1987'),
    ('Murder on the Orient Express', '1934'),
    ('One Hundred Years of Solitude', '1967'),
    ('Beloved', '1987'),
    ('American Gods', '2001'),
    ('To Kill a Mockingbird', '1960'),
    ('The Catcher in the Rye', '1951'),
    ('1984', '1949')
]
hashTable3 = [''] * len(books3)

def hashFunctionRolls(el):
    """Помещает в хеш таблицу 10 книг методом свертки (по дате печати)"""
    summ = 0
    date = el[1]
    for i in range(0, len(date)-1, 2):
        sumCodes = int(el[1][i:i+2][::-1])
        summ += sumCodes

    hashValue = summ % len(books3)
    return hashValue


for el in books3:
    hashTable3[hashFunctionRolls(el)] = el

print(hashTable3[hashFunctionRolls(('The Shining', '1977'))])
