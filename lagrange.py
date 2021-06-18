# -*- coding: utf-8 -*-
# @Time    : 2021/6/15 22:17
# @Author  : MSH
# @FileName: lagrange.py
# @Software: PyCharm
import numpy as np

class Lagrange:
    """
    每个自由度上都定义有一个基函数
    """
    def __init__(self, d, elements):
        self.degree = d
        self.elements = elements
        self.nelement = len(self.elements) - 1
        _dofs = []
        for i in range(1, len(self.elements)):
            _dof_el = np.linspace(self.elements[i - 1], self.elements[i], self.degree + 1)
            _dofs.append(_dof_el)
        self.dofs = np.array(_dofs)
        self.ndof = self.dofs.size
        assert self.ndof == self.nelement * (self.degree + 1)

    def FindElement(self, n):
        _idx = np.searchsorted(self.elements, n) - 1
        if _idx < 0:
            _idx = 0
        return _idx

    def BasisFunctions(self, x):
        """
        计算给定n的拉格朗日基函数的值

        :param x:
        :return: 基函数的值
        """
        ret = []
        idx = self.FindElement(x)
        for i in range(self.degree + 1):
            saved1 = 1.0
            saved2 = 1.0
            for j in range(self.degree + 1):
                if i != j:
                    saved1 *= (x - self.dofs[idx][j])
                    saved2 *= (self.dofs[idx][i] - self.dofs[idx][j])
            ret.append(saved1 / saved2)
        return idx, ret
