#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"


import os
import time

source = []
source = [input('Enter path to directorys what you want TO BACKUP! Example: "~/Docs ~/Music/Metal"\n')]

target_dir_default = os.path.expanduser('~/Backup_Test') # заменяет ~ или на домашнюю директорию пользователя!
target_dir = ''
target_dir = os.path.expanduser(input('If you want, you can enter your path to directory where backup be located! (Default path "~/Backup") Otherwise push Enter\n '))

if  target_dir == '':
    target_dir = target_dir_default
else:
    print('Your path is: ', target_dir)


if os.path.exists(target_dir) != True: # возвращает True, если path указывает на существующий путь или дескриптор открытого файла.
    os.mkdir(target_dir)
print('Directory successfully created', target_dir)

target = target_dir + os.sep + time.strftime('%Y-%m-%d_%H:%M:%S') + '.zip'

'''
os.sep – содержит раз делитель пути для конкретной операционной системы, т.е. он будет '/' в 
GNU/Linux и Unix 3 , '\\' в Windows и ':' в Mac OS. 
Использование os.sep вместо этих символов напрямую делает программу переносимой,
и она сможет работать на всех этих операционных системах.
'''

zip_command = "zip -vr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup is DONE! Directory with backup: ', target)
else:
    print('Backup FUCK_UP')
