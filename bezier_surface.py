# -*- coding: utf-8 -*-
# @Time    : 2021/6/26 13:45
# @Author  : MSH
# @FileName: bernstein.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

class BezierSurface:
    def __init__(self, p, vertexes, cp):
        self.vertexes = np.array(vertexes)
        self.degree = p
        self.order = self.degree + 1
        self.control_point = cp
        self.subscript = [{0: 0}] * self.order

        for n in range(self.degree, 0, -1):
            _order = n + 1
            self.subscript[n] = {}
            idx = 0
            for i in range(_order):
                for j in range(_order - i):
                    self.subscript[n][i * 100 + j * 10 + n - i - j] = idx
                    idx += 1

    def barycentric_coor(self, p):
        v1 = self.vertexes[0]
        v2 = self.vertexes[1]
        v3 = self.vertexes[2]
        M = np.array([[1, 1, 1],
                      [v1[0], v2[0], v3[0]],
                      [v1[1], v2[1], v3[1]]])
        b = np.array([1, p[0], p[1]])
        bary_coor = np.linalg.solve(M, b)
        return bary_coor

    def eval(self, t):
        p = self.control_point
        bc = self.barycentric_coor(t)
        for l in range(1, self.order):
            tmp = []
            sub = self.subscript[self.degree - l + 1]
            for s in self.subscript[self.degree - l].keys():
                idx1, idx2, idx3 = sub[s + 100], sub[s + 10], sub[s + 1]
                tmp.append(bc[0] * p[idx1] + bc[1] * p[idx2] + bc[2] * p[idx3])
            p = tmp
        return np.array(p[0])

    def points_on_triangle(self, v, n):
        """
        Give n random points uniformly on a triangle.

        The vertices of the triangle are given by the shape
        (2, 3) array *v*: one vertex per row.
        """
        x = np.sort(np.random.rand(2, n), axis=0)
        return np.column_stack([x[0], x[1] - x[0], 1.0 - x[1]]) @ v

    def plot_suface(self):
        cx, cy = zip(*self.control_point)
        plt.scatter(cx, cy, s=1)
        sample = self.points_on_triangle(self.vertexes, 1000)
        # sx, sy = zip(*sample)
        # plt.scatter(sx, sy, s=0.1)
        p = []
        for s in sample:
            p.append(self.eval(s))
        # p = np.array(p)
        x, y = zip(*p)
        plt.scatter(x, y, s=0.5)
        plt.show()
