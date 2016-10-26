#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

#---Модуль классы---#

class Hero():

    def __init__(self, name, level, health, items):
        self.name = name
        self.level = level
        self.health = health
        self.items = items

    def show_hero(self):
        pers = ("Your name is " + self.name,
                "Your level is " + str(self.level),
                "Your health is " + str(self.health),
                "You have " + str(self.items))
        print(pers)

#------------------------------------------------------------------

class Monster():

    def __init__(self, name, level, health, items):
        import random
        self.name = 'Monster' + '-' + str(level)
        self.level = level
        self.health = health
        self.items = random.choice(['sword', 'shield', 'boots'])

    def show_monster(self):
        M = ('Your enemy is ' + self.name,# + '-' + str(self.level),
             'His level ' + str(self.level),
             'His health ' + str(self.health),
             'He has ' + self.items)
        print(M)

#------------------------------------------------------------------

class Box():
    def __init__(self, items, level):
        import random
        self.items = random.choice(['ring + 100 Python skills', 'amulet + 100 Linux skills', 'glasses + 100 Testing skills'])
        self.level = random.randint(1, 10)

    def open_box(self):

        r = self.level
        a = int(input('Enter key: '))

        while a != r:
            if a < r:
                print('beri bolshe')
            else:
                print('beri menshe')

            a = int(input('Enter key: '))
        else:
            print('Locker open!!!')

        print('Password is: ', r)


