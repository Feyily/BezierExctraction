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


class LagrangeSurface:
    def __init__(self, p, ele1, q, ele2):
        self.p = p
        self.q = q
        self.u_lagrange = Lagrange(p, ele1)
        self.v_lagrange = Lagrange(q, ele2)
        self.ndof = self.u_lagrange.ndof * self.v_lagrange.ndof

    def BasisFunctions(self, p):
        u, v = p[0], p[1]
        ret = []
        u_idx, u_bf = self.u_lagrange.BasisFunctions(u)
        v_idx, v_bf = self.v_lagrange.BasisFunctions(v)
        cnt = 0
        for i in range(len(u_bf)):
            for j in range(len(v_bf)):
                el_offset = ((v_idx * self.u_lagrange.nelement) + u_idx)
                ret.append([el_offset * (self.p + 1) * (self.q + 1) + cnt,
                            u_bf[i] * v_bf[j]])
                cnt += 1
        return ret

    def BasisMatrix(self, samples: np.ndarray):
        shape = (len(samples), self.ndof)
        ret = np.zeros(shape)
        for p in samples:
            bf = self.BasisFunctions(p)
        pass
