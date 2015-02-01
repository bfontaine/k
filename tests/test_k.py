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
        self.assertIsInstance(x.a, int)

    def test_type_name(self):
        A = k.make("Foobar", "X")
        self.assertEquals(str(type(A.X)), "<class 'k.Foobar'>")

    def test_values(self):
        A = k.make("A", "xyz")
        self.assertEquals(A.x, 0)
        self.assertEquals(A.y, 1)
        self.assertEquals(A.z, 2)

    def test_values_with_start(self):
        start = 42
        A = k.make("A", "abcd", start=start)
        self.assertEquals(A.a, start)
        self.assertEquals(A.d, start+3)
