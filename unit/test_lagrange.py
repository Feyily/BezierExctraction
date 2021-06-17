# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 23:01
# @Author  : MSH
# @FileName: test_lagrange.py
# @Software: PyCharm
import unittest
from lagrange import *

class TestLagrange(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.IgnoreEps = 1e-15
        cls.elements = [0, 1, 2, 3]

    def test_init(self):
        lagrange = Lagrange(2, self.elements)
        except_dofs = np.array([[0, 0.5, 1], [1, 1.5, 2], [2, 2.5, 3]])
        self.assertTrue((lagrange.dofs == except_dofs).all())

    def test_findspan(self):
        lagrange = Lagrange(2, self.elements)
        ele = lagrange.FindElement(1.1)
        self.assertEqual(ele, 1)

    def test_basisfunctions(self):
        node = [0, 1, 2, 3]
        lagrange = Lagrange(3, node)
        _, bs = lagrange.BasisFunctions(1.2)
        pass

    def test_surfacebasisfunctions(self):
        surface = LagrangeSurface(2, self.elements, 2, self.elements)
        bf = surface.BasisFunctions([2.2, 1.1])
        bsum = 0
        for b in bf:
            bsum += b[1]
        # 浮点数的验证不能用assertEqual
        self.assertLess(abs(bsum - 1.0), self.IgnoreEps)
