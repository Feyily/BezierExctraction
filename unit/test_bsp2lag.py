# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 20:58
# @Author  : MSH
# @FileName: test_bsp2lag.py
# @Software: PyCharm
import unittest
from bspline2lagrange import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class TestbSplineToLagrange(unittest.TestCase):

    def test_convertsurface(self):
        nodes = np.linspace(0, 1, 30)
        surface = LagrangeSurface(3, nodes, 3, nodes)

        nu = [0., 0., 0., 0., 0.333333333, 0.666666666, 1., 1., 1., 1.]
        nv = [0., 0., 0., 0., 0.5, 1., 1., 1., 1.]
        cp = []
        with open("./points.txt", "r") as pf:
            lines = pf.readlines()
            for line in lines:
                cp.append(np.array(line.split(), dtype=np.float))
        cp = np.array(cp)
        ext = LagrangeExtraction(nu, 3, nv, 3, cp)

        sp = ConvertSurface(surface, ext)
        fig = plt.figure(figsize=(12, 8))
        ax = fig.gca(fc='whitesmoke', projection='3d')
        for s in sp:
            ax.scatter(s[0], s[1], s[2])
        plt.show()
