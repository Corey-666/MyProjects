#! /usr/bin/python3.5
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

'''
import sys

for i in sys.argv:
    print(i, end=' ',)
print(sys.argv)

'''

'''
elif sys.argv == '-open':
    print('OPEN BLEAT')

print('\n\nPATH is ', sys.path,'\n')

'''

'''
print(2<4<6)

print('{0:o}, {1:x}, {2:b}'.format(100,100,100)) # o - восьмиричный литерал
                                                 # x - шестнадцетиричный
                                                 # b - двоичный


print(int('01010101', 2)) # Преобразование изображения числа в число по основанию

a = 666
print(a.bit_length())

print(0.1 + 0.1 + 0.1 - 0.3)
'''



# Экранированные и НЕ форматированные строки
'''
s = set('sdlvmrogij3490tugebjqp"})"/') # Множество
print('a' in s,'\n', s, '\n')

print('Ж\t0\nП \x00\tA') # экранированные последовательности

print('C:\Windows\Shit') # Правильно писать с \\ (двумя слэшами) или r перед строкой!!!

path = 'c:\shit\fuck\ass' # НЕ правильно
print(path)
path_right = r'c:\shit\fuck\ass'
print(path_right)
'''

print(r'JOPA'[:-1])

minus = (len('jopa')-1) # !!! Технически отрицательное смещение складывается с длинной строки!!!
print('jopa'[minus])    # len('jopa')-1 = 4+(-1) = 3
print('jopa'[-1])
















