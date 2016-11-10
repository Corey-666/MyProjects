#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

import pytest

def func(x):
    return x + 666

def test_answer():
    assert func(0) == 666
