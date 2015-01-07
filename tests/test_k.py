# -*- coding: UTF-8 -*-

import platform

if platform.python_version() < '2.7':
    import unittest2 as unittest
else:
    import unittest

import k

class TestK(unittest.TestCase):

    def test_type(self):
        x = k.make("x", "a")
        self.assertIsInstance(x.a, x)


    def test_type_name(self):
        A = k.make("Foobar", "X")
        self.assertEquals(str(type(A.X)), "<class 'k.Foobar'>")
