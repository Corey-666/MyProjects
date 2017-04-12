#! /usr/bin/python3.4
# -*- coding: utf-8 -*-

import sys
s = sys.path
s.append('/home/corey/')

from pylib import pylib
import unittest

class Test(unittest.TestCase):

    def test_sys(self):
        self.assertEqual(sys.platform, pylib.platform())