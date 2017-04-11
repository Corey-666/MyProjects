#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"


import os
import time

source = []
source = [input('Enter directory for backup: ')]

target_dir = '/home/corey/Temp/Backup_Test'

target = target_dir + os.sep + time.strftime('%Y-%m-%d_%H:%M:%S') + '.zip'

zip_command = "zip -qr {0} {1}".format(target, ' '.join(source))

if os.system(zip_command) == 0:
    print('Backup is DONE', target)
else:
    print('Backup FUCK_UP')
