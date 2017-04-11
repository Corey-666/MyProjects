#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

#Function example
# сравнение символов в строках и возврат общих символов
def func(s1, s2):
    r = []
    for x in s1:
        if x in s2:
            r.append(x)
    return (r)

print(func('jopa', 'jopisha'))

def func2(z = 666):
    s = ['sdcsd', 123, {'d':13}, 666]
    for x in s:
        if z in s:
            return (z)
    print(z)

#print(func2())
