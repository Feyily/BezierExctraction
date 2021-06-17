# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 16:40
# @Author  : MSH
# @FileName: text_extraction.py
# @Software: PyCharm
import unittest
from extraction import *

class TestLagrangeExtraction(unittest.TestCase):

    def test_extraction(self):
        nu = [0., 0., 0., 0., 0.333333333, 0.666666666, 1., 1., 1., 1.]
        nv = [0., 0., 0., 0., 0.5, 1., 1., 1., 1.]
        cp = []
        with open("./points.txt", "r") as pf:
            lines = pf.readlines()
            for line in lines:
                cp.append(np.array(line.split(), dtype=np.float))
        cp = np.array(cp)
        ext = LagrangeExtraction(nu, 3, nv, 3, cp)
        ext.excraction()
        pass
