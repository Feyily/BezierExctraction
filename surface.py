# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 10:16
# @Author  : MSH
# @FileName: surface.py
# @Software: PyCharm
from bspline import *
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class BsplineSurface:
    def __init__(self, su, sv, cp=None):
        self.spline_u: bSpline = su
        self.spline_v: bSpline = sv
        self.ControlPoints = cp

    def getNodesAndEvals(self, xi):
        u = xi[0]
        v = xi[1]
        span_u = self.spline_u.FindSpan(u)
        nodesu = self.spline_u.getNodes(span_u)
        span_v = self.spline_v.FindSpan(v)
        nodesv = self.spline_v.getNodes(span_v)

        dersu = self.spline_u.BasisFunctions(u, span_u)
        dersv = self.spline_v.BasisFunctions(v, span_v)

        retval = []
        for i in range(len(nodesu)):
            for j in range(len(nodesv)):
                retval.append([nodesu[i] + nodesv[j] * self.spline_u.LenContralPoint,
                               dersu[i] * dersv[j]])
        return retval

    def plot_surface(self):
        samples_u = np.linspace(0, 1, 20)
        samples_v = np.linspace(0, 1, 20)
        samples = []
        for u in samples_u:
            for v in samples_v:
                nodesAndEvals = self.getNodesAndEvals((u, v))
                _p = np.zeros(3)
                for ne in nodesAndEvals:
                    _p += self.ControlPoints[ne[0]] * ne[1]
                samples.append(_p)

        fig = plt.figure(figsize=(12, 8))
        ax = fig.gca(fc='whitesmoke', projection='3d')
        for s in samples:
            ax.scatter(s[0], s[1], s[2])
        plt.show()
