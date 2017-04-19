#! /usr/bin/python3.5
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"

'''
Примеры срезов в списке
my_list[x:y:z] где:
x - позиция с которой начинается вырезка (включает указанный элемент)
y - позиция где заканчивается срез (НЕ включает указанный элемент)
z - шаг
'''
my_list = ['apple', 'banana', 'kiwi', 'orange', 'plum']
print(my_list[::]) # All list

print(my_list[::2]) # шаг в 1 элемент

print(my_list[:-1]) # БЕЗ последнего элемента

print(my_list[::-1]) # с конца

print(my_list[1:4:1]) # срез с 1го по 3й (включительно) элементы

################

my_str = 'abcdifghijklmnop'
print('My string: ', my_str)
print('Каждый 2й элемент с 1го по 9й:', my_str[1:10:2],'\n',
      'Каждый 2й элемент от начала до конца:', my_str[::2], '\n' # Если какой-то параметр НЕ указан, по умолчанию 0!
      'С последнего элемента:', my_str[::-1], '\n' # [0:0:-1]
      'В обратном порядке:', my_str[5:2:-1], '\n' # C 5го по 2й в обратном порядке
      )
for element in my_str:
    print(element, end='-*-')
print('\n')
#    print(element, end='-*-') # Элементы строки через 1 заменяются -*-

# Объект среза !!!
sl = 'shit'
print(sl[1:3])
print(sl[slice(1, 3)])
print(sl[::-1])
print(sl[slice(None, None, -1)], '\n')

######################
'''
name = input('Enter yor name: ')
print('{0} You are stupid {1}'.format(name, 'bitch'))
'''
# replace method!
sss = 'v;wdv;vjqwvwc;ckwjjckk'
print(sss.replace('w', '-*-'), '\n') # По сути replace выполняет глобальный поиск с заменой!!!

############################

#join method
string = 'CoreyKill'
print(string)
ls = list(string)
ls = ls + ['666']
print(ls)
print( ''.join(ls)) # Метод join собирает список обратно в строку!

##############################

