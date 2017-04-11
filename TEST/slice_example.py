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



