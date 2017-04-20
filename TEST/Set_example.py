#! /usr/bin/python
# -*- coding: utf-8 -*-
__author__ = "cOREY_kILL"
__license__ = "GPL"

# Пример множества

engineers = {'corey', 'james', 'kirk', 'jack'}
managers = {'corey', 'bob'}

print(type(engineers)) # класс "set" - множество

# Пример операций над множествами
print('Does Corey the engineer?', 'corey' in engineers) # Кто одновременно является инженером и менеджером?

print('How is the engineer and manages at the same time?', engineers & managers)

print('All of ingineers and managers', engineers | managers) #  Все сотрудники из обеих категорий

print('Engineers NOT managers:', engineers - managers) # Инженеры, не являющиеся менеджерами

print('Managers NOT engineers:', managers - engineers) # Менеджеры, не являющиеся инженерами

print('Are all managers engineers?', engineers > managers) # Все менеджеры являются инженерами?

print('Are these employees engineers?', {'kirk', 'jack'} < engineers) # Оба сотрудника - инженеры? (подмножество)

print('Employees belonging to the same category', managers ^ engineers) # Сотрудники принадлежащие к одной категории

print('Intersection', (managers | engineers) - (managers ^ engineers)) # Пересечение