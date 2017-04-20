#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"


# Пример простой базы данных

bob = ['Bob Smith', 42, 30000, 'software',]
sue = ['Sue Jones', 45, 40000, 'hardware']
print('Base: \n', bob, '\n', sue, '\n')

print('Get Name and Salary: ', bob[0], sue[2], '\n') #Получит имя и оклад

print('Get surname: ', bob[0].split()[-1], '\n')

sue[2]*=1.25
print('Increase the salary Sue: ', sue, '\n')

# База в виде списка
people = [bob, sue]
print('Base like list: ''\n')
for person in people:
    print(person)

print('Get 1th from "people list", and 0th from "sue list",\n' , people[1][0])