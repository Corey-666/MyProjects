#! /usr/bin/python2.7
# -*- coding: utf-8 -*-

import random
from datetime import datetime

import unittest


def Timer(Guess_num):
    def decorator():
        t1 = datetime.now()
        Guess_num()
        t2 = datetime.now()
        print('Your time is: ', t2 - t1)
    return decorator

@Timer
def Guess_num():

    print('Test your luck, guess the number!')

    r = random.randint(1, 10)
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
        print('AXYETb!! C 1ro PA3A!')
    else:
        print(r, '\nChislo popitok: ', count)

if __name__ == '__main__':
        Guess_num()

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

class Test_Guess_num(unittest.TestCase):


    def test_random(self, r):
        r = random.randint(1, 10)
        self.assertTrue(r in range(1,10))

    def test_count(self):







if __name__ == '__main__':
    unittest.main()