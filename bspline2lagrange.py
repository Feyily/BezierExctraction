# -*- coding: utf-8 -*-
# @Time    : 2021/6/17 18:24
# @Author  : MSH
# @FileName: bspline2lagrange.py
# @Software: PyCharm
from extraction import *

def ConvertSurface(lsurface: LagrangeSurface, ext: LagrangeExtraction):
    """
    将B样条曲面转换成拉格朗日曲面

    :param lsurface: 拉格朗日曲面对象
    :param ext: 拉格朗日提取对象
    :return:
    """
    us = lsurface.u_lagrange.dofs.flatten()
    vs = lsurface.v_lagrange.dofs.flatten()
    # 拉个朗日曲面控制顶点
    pl = ext.excraction(us, vs)

    node = np.linspace(0, 1, 30)
    _sample = []
    for x in node:
        for y in node:
            _sample.append([x, y])
    _sample = np.array(_sample)

    L = lsurface.BasisMatrix(_sample)
    new_p = np.matmul(L, pl)
    return new_p
