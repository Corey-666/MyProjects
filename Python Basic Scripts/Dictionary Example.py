#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

"""List of Metallica albums"""
alb = {
       "Kill Em All": 1983,
       "Ride The Lighting": 1984,
       "Master Of Puppets": 1986,
       "... And Justice For All": 1988,
       "Metallica": 1991,
       "Live in Nizhny Novgorod": 1991
       }

L = list(alb.items())
L.sort(key = lambda item: item[1])
print(L)