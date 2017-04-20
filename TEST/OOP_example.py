#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"


'''
Предположим,
у нас есть класс с именем MyClass и экземпляр этого класса с именем myobject. При вызове
 метода этого объекта, например, “ myobject.method(arg1, arg2) ”, Python автоматически
  превращает это в “ MyClass.method(myobject, arg1, arg2) ” – в этом и состоит смысл self.
'''

class MyClass():# Если нет суперкласса, скобки можно не ставить
    name = input('Enter name: ')
    job = input('Enter job: ')
    age = input('Enter age: ')


    def change(self, newname, newjob, newage):
        self.name = newname
        self.job = newjob
        self.age = newage


obj1 = MyClass()
obj2 = MyClass()

print('{0},{1},{2}'.format(obj1.age, obj1.name, obj1.job))

print(
    obj2.change(newname='vasia', newjob='dvornik', newage=666)
)