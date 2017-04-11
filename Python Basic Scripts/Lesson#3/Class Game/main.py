#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

from classes import *

name = Hero
name = input("Enter name for your hero: ")

myhero = Hero(name, 1, 100, 'sword')
myhero.show_hero()

print('\n''And now you must go to destroy everething, but something on your way stopping you!!''\n')

mymonster = Monster(name, 1, 100, [])
mymonster.show_monster()


print('You must kill this bastard! Do you wanna kill? YES or YES???''\n')
#select = ""
select  = input(str("What's your answer: "))

while select != 'yes':
    print(name)
    select = input('You born to KILL enter yes: ')
print('GOOD')
print(mymonster.name, 'Was KILLED''\n')

if mymonster.items == myhero.items:
    print('OOOh shit',mymonster.name, 'has', mymonster.items, 'too((''\n')
else:
    myhero.items = myhero.items + ", " + mymonster.items
    print('Now you have: ', myhero.items,'\n')

print("What the f..... for the monster's corpse you see the CYHDYK!!!\n"
      "To open it, guess a number from 1 to 10 with 3 attempts")

mybox = Box([], int)
mybox.open_box()
myhero.items = myhero.items + ", " + mybox.items
print('Daaaamn,', name, 'You have magic item: ', mybox.items)
print('And now you have 'myhero.items)

