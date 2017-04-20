#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"

T = (1, 2, 3, 4)
print(len(T))

print(T + (5, 6)) # Конкатенация
print(T) # Кортеж НЕ изменяемый!

print(T.index(4),'\n', # Значение 4 находится в позиции 3
      T.count(4)) # значение 4 присутствует в одном экземпляре

