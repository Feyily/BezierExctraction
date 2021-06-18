# -*- coding: utf-8 -*-
# @Time    : 2021/6/14 10:16
# @Author  : MSH
# @FileName: surface.py
# @Software: PyCharm
from bspline import *
from lagrange import *
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


class LagrangeSurface:
    def __init__(self, p, ele1, q, ele2, cp=None):
        self.p = p
        self.q = q
        self.u_lagrange = Lagrange(p, ele1)
        self.v_lagrange = Lagrange(q, ele2)
        self.ndof = self.u_lagrange.ndof * self.v_lagrange.ndof
        self.ControlPoints = cp

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
        for i, p in enumerate(samples):
            bfs = self.BasisFunctions(p)
            for bf in bfs:
                ret[i, bf[0]] = bf[1]
        return ret
