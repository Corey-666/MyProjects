#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

import argparse
import random
from datetime import datetime


def Timer(Guess_num):
    def decorator():
        t1 = datetime.now()
        Guess_num()
        t2 = datetime.now()
        print('Your time is: ', t2 - t1)
    return decorator


parser = argparse.ArgumentParser()
parser.add_argument('-x', '-From', nargs='?', type=int, help='Первое число диапозона')
parser.add_argument('-y', '-To ', nargs='?', type=int, help='Второе число диапозона')

args = parser.parse_args()
print('Guess from ' + str(args.x) + ' to ' + str(args.y))


@Timer
def Guess_num():

    print('Test your luck, guess the number!')

    if args.x or args.y == None:
        r = random.randint(1, 10)
    else:
        r = random.randint(args.x, args.y)
    a = int(input('enter num: '))
    count = 1

    while a != r:

        if a < r:
            print('beri bolshe')
        else:
            print('beri menshe')
        a = int(input('enter num: '))
        count += 1
    else:
        print('YGADAL!')

    if count == 1:
        print('AXEPETb!! C 1ro PA3A!')
    else:
        print(r, '\nChislo popitok: ', count)

Guess_num()