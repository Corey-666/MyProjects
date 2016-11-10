#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import subprocess
from subprocess import Popen, PIPE
from datetime import datetime

df = Popen(["df -ah"], executable='/bin/bash', shell=True, stdout= open('/home/corey/disk_usage.log', 'a'))

with open('/home/corey/disk_usage.log', 'a') as f:
    f.write('\n' + str(datetime.now()) + '\n' + '~'*100 + '\n')
    f.close()
    


'''
# вывод на экран
stdout=subprocess.PIPE

out = df.stdout.readlines()

for line in out:
    out = (line.strip())
    out.split()
    print(out)
'''


'''
def ping1(ipaddress="192.168.1.14"):
    p = subprocess.Popen("/bin/ping -c 2 %s" % ipaddress, shell=True,
                        stdout=subprocess.PIPE)
    out = p.stdout.read() #в переменной out находится вывод команды ping. Ниже идет обработка вывода команды ping.
    print (out)
    result = out.split()
    print (result)

if __name__ == '__main__':
    ping1()

'''
