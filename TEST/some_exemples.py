#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"


#print(help(int))

my_list = ['corey', 666, ['inner list'], '123']

for item in my_list:
    print(item, end=' ') # end=' ' выводит список в 1 строку. Закончить вывод пробелом

# Добавление элемента в список
my_list.append('NEW_element') # append метод класса list. Добавляет 1 элемент в конец списка
print(my_list, '\n')

print(my_list[2][0])
my_list[2].append('123')
print(my_list[2], '\n')

# Пример кортежа
zoo = ('qqq', 'ddd', 'ggg')
print(zoo)
new_zoo = ('xxx', 'yyy', zoo)
print(new_zoo[2][0:], '\n')

empty = () # Пустой кортеж
singleton = (666,) # Кортеж из одного элемента 666

# Пример словаря
# в словаре, пара ключь-значение НЕ упорядочены. Для порядка словарь нужно сортировать!
#print(help(dict))

my_dict = {'key1' : 'value1', 'key2' : 'value2', 'corey' : 'THE KING'}
print(my_dict, '\n',
      my_dict['key1'], '\n') # Обращение к элементу словаря

my_dict['new_key'] = 'new_value' # Добавить элемент
del my_dict['key1'] # Удалить элемент
print(my_dict, '\n')


# Пример сортировки словаря
for key, value in my_dict.items():
    print('Ключь {0} со значением {1}'.format(value, key))






