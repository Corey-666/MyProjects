import os

'''
rec = {}

rec['name'] = input('Enter your name ') # Присваивание выполняется по ключам!
#if rec['name'] == '':
#print('Name not entered!')
#rec['name'] = input('Enter your name ')
rec['job'] = str(input('Enter your job '))
rec['age'] = str(input('Enter your age '))

print(rec['name'],
      rec['job'],
      rec['age'])
print(rec)

with open('/home/corey/test_data.txt', 'w') as f:
      f.write(str(rec))
'''

# Примеры написанны в виде функций для локализации переменных!!!

def dict_1():
    D = {'key-1':'corey', 'key-2':666, 'key-3':{'sub-key-1':'jopa', 'sub-key-2':13}}
    print('\tExample of dictionary: ',D)

    print('key-3 in D:', 'key-3' in D, '\n' # проверка на вложенность
          'len D:', len(D), '\n'
          'method keys, D.keys()', list(D.keys()), '\n') # list(D.keys()) потому что список удобнее сортировать!

    # Изменение словаря
    D['key-4'] = ['kill', 'python', 123.321]
    print('Added key-4:', D)
    del D['key-2']
    print('Delete key-2:', D)
    D['key-1'] = ['Mr. Corey Kill']
    print('New value for key-1:', D, '\n')

    # Методы D.values, D.items
    print('Method D.values: ', list(D.values()), '\n'
          'Method D.items: ', list(D.items()), '\n') # D.items возвращает КОРТЕЖИ пар key:value
    # Метод get
    print('Method get, D.get(key-4):', D.get('key-4'), '\n'
          'If key not found, D.get(key-13):', D.get('key-13'), '\n')

    # Метод update
    D2 = {'up-key-1':['Shit'], 100:100**3}
    D.update(D2) # Объединяет словари перезаписывая значения с одиноаовыми ключами
    print('Method update, D.update(D2): ', D, '\n')

    # Метод pop
    DD = {'aa':'11', 'bb':22, 'cc':'33'}
    print('some dict DD:', DD)
    DD.pop('aa')
    print("DD.pop('aa'):", DD)
    DD.pop('cc')
    print("DD.pop('cc'):", DD, '\n')

    # обхот методом for
    print('Итерация словаря циклом for', '\n')
    print(D)
    for key in D: # Полная форма выглядит как for key in D.keys()
        print(key, '\t', D[key])


# Примеры создания словарей
d1 = {} # Динамическое присваивание по ключам
d1['name'] = 'corey'
d1['age'] = 666
print(d1)

d2 = dict(name='corey', age='666') #Форма именованных аргументов
print(d2)

d3 = dict([('name', 'corey'), ('age', 666)]) #Кортежи ключ:значение
print(d3)

#dict_1()





