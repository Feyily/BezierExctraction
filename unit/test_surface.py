# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 20:08
# @Author  : MSH
# @FileName: test_surface.py
# @Software: PyCharm
import unittest
from surface import *
from bspline import bSpline

class TestSurface(unittest.TestCase):

    def test_plotsurface(self):
        nu = [0., 0., 0., 0., 0.333333333, 0.666666666, 1., 1., 1., 1.]
        nv = [0., 0., 0., 0., 0.5, 1., 1., 1., 1.]
        su = bSpline(3, nu)
        sv = bSpline(3, nv)
        cp = []
        with open("./points.txt", "r") as pf:
            lines = pf.readlines()
            for line in lines:
                cp.append(np.array(line.split(), dtype=np.float))
        cp = np.array(cp)
        surface = BsplineSurface(su, sv, cp)
        surface.plot_surface()
