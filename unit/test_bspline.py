# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 16:24
# @Author  : MSH
# @FileName: test_bspline.py
# @Software: PyCharm
import unittest
from bspline import *

class TestSpline(unittest.TestCase):

    def test_findspan(self):
        node = [0., 0., 0., 0.5, 1., 1., 1.]
        sp = bSpline(2, node)
        span = sp.FindSpan(0.5)
        self.assertEqual(span, 2)

    def test_getnodes(self):
        node = [0., 0., 0., 0.5, 1., 1., 1.]
        sp = bSpline(2, node)
        span = sp.FindSpan(0.5)
        idx = sp.getNodes(span)
        self.assertEqual(idx, [0, 1, 2])
