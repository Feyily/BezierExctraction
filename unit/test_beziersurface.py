# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 14:12
# @Author  : MSH
# @FileName: test_bernstein.py
# @Software: PyCharm
import unittest
from bezier_surface import *


class TestBernstein(unittest.TestCase):

    def test_eval(self):
        p = np.array([[2.1554, 1.2465], [4.1446, 2.4845],
                      [0.1564, 3.1468], [2.1543, 2.4874],
                      [1.1548, 2.1564], [3.1515, 3.5485],
                      [4.1515, 2.1543], [3.0155, 0.5678],
                      [1.1531, 4.1053], [0.4512, 2.2645]])
        bs = BezierSurface(3, [[-1, -1], [1, -1], [0, 1]], p)
        s = bs.eval((0, 1))
        pass

    def test_plotsurface(self):
        p = np.array([[3, 5], [4, 4], [4, 3], [5, 2], [1, 4],
                      [2, 3], [4, 1], [0, 2], [2, 1], [0, 0]])
        bs = BezierSurface(3, [[-1, -1], [1, -1], [0, 1]], p)
        bs.plot_suface()
