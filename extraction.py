# -*- coding: utf-8 -*-
# @Time    : 2021/6/13 23:55
# @Author  : MSH
# @FileName: try_extraction.py
# @Software: PyCharm
from surface import *
from lagrange import *
import numpy as np

class LagrangeExtraction:
    def __init__(self, nu, p, nv, q, cp):
        self.node_u = nu
        self.node_v = nv
        self.spline_u = bSpline(p, self.node_u)
        self.spline_v = bSpline(q, self.node_v)
        self.surface = BsplineSurface(self.spline_u, self.spline_v, cp)
        self.ncp = self.spline_u.LenContralPoint * self.spline_v.LenContralPoint

    def GenerateM(self, dofs_u, dofs_v):
        M = np.zeros((len(dofs_u) * len(dofs_v), self.ncp))
        dof_idx = 0
        for dof_u in dofs_u:
            for dof_v in dofs_v:
                nodesAndEvals = self.surface.getNodesAndEvals((dof_u, dof_v))
                for ne in nodesAndEvals:
                    M[dof_idx, ne[0]] = ne[1]
                dof_idx += 1
        return M

    def excraction(self):
        dofs_u = np.linspace(0, 1, 100)
        dofs_v = np.linspace(0, 1, 100)
        M = self.GenerateM(dofs_u, dofs_v)
        pT = np.matmul(M, self.surface.ControlPoints)
        return pT

    def ExtractedSurface(self):

        pass
