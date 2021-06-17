# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 23:56
# @Author  : MSH
# @FileName: bspline.py
# @Software: PyCharm
import numpy as np

class bSpline:
    def __init__(self, p, node, cp=None):
        self.p = p  # u方向次数
        self.NodeVector = node   # 结点向量
        self.ContralPoints = cp  # 控制顶点
        self.LenContralPoint = len(self.NodeVector) - p - 1
        if cp is not None:
            assert self.LenContralPoint == len(cp)

    def BasisFunctions(self, t, span):
        left = [0]
        right = [0]
        base = [1.0]
        for i in range(1, self.p + 1):
            left.append(t - self.NodeVector[span + 1 - i])
            right.append(self.NodeVector[span + i] - t)
            saved = 0.0
            for j in range(i):
                tmp = base[j] / (right[j + 1] + left[i - j])
                base[j] = saved + right[j + 1] * tmp
                saved = left[i - j] * tmp
            base.append(saved)
        return base

    def FindSpan(self, t):
        span = np.searchsorted(self.NodeVector, t) - 1
        if span < self.p:
            span = self.p
        return span

    def getNodes(self, span):
        """
        Given a parameter ``u``, return a list of the indices of B-spline
        basis functions whose supports contain ``u``.
        """
        nodes = []
        for i in range(span - self.p, span + 1):
            nodes += [i % self.LenContralPoint, ]
        return nodes
