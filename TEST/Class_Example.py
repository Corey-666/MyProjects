#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

'''class MyClass():
    name = 'name'
    age = 0

    def set_name(self, n):
        self.name = n

    def set_age(self, m):
        self.age = m

    def person(self):
        print('-----------------')
        print("/ Hi, I'm ", self.name)
        print("/ i'm years old ", self.age )

a = MyClass()
print(a.person())'''

class Hero:
    def __init__(self, name, level, race):
        self.name = name
        self.level = level
        self.race = race
        self.health = 100

    def show_hero(self):
        discription = (self.name + 'Level is  ' + self.level + 'race is ' + self.race + "Health " + str(self.health).title()
    #print(discription)

    def m(self):
        print("hero" + self.name + "start moving..")

myhero = Hero("Corey", 5, 'orc')




