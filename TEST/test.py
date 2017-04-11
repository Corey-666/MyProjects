#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"

'''
def shit():
    while True:
        s = input('enter some string >= 3 ')
        if len(s) < 3:
            continue
        else:
            s = 'exit'
            break
'''
'''
x = 666 # Глобальная переменная

def foo():
    print('x = ', x) # В теле функции печатается значение переменной Х
    x = 123 # Замена глобального х(666) на локальную переменную х(123) НО только в рамках этой функции
    print('x = ', 123)

foo(x)
print(x) # Вне тела функции х остался прежним!

'''
'''
def max(x, y):
    if x < y:
        return y
    elif x > y:
        return x
    else:
        return 'x & y PABHbl'

print(max(3,2))
'''


import sys

for i in sys.argv:
    print(i, end=' ',)
print(sys.argv)

'''
elif sys.argv == '-open':
    print('OPEN BLEAT')

print('\n\nPATH is ', sys.path,'\n')


'''


