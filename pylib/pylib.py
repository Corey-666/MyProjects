#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

# -=Моя библиотека полезных функций!!=- #

from datetime import datetime
#----------------------------------------------------#

def py_sys_path():
    import sys
    print(sys.path,'\n')
py_sys_path()

#----------------------------------------------------#

def platform ():
    import sys
    print('Your platform is ', sys.platform)
    input()
platform()

#-----------------------------------------------------#

def fib(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a+b
    return a

#---------------------------------------------------#
<<<<<<< HEAD
=======



>>>>>>> a0d94770e7d82895b5674bf64662135203cce56f
