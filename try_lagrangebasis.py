# -*- coding: utf-8 -*-
# @Time    : 2021/6/16 9:55
# @Author  : MSH
# @FileName: try_lagrangebasis.py
# @Software: PyCharm
from dolfin import *
import numpy as np

mesh = UnitIntervalMesh(3)
# mesh = UnitSquareMesh(3, 3)
V = FunctionSpace(mesh, 'CG', 2)
el = V.element()

# Where to evaluate
x = np.array([0.1])

# Find the cell with point
x_point = Point(*x)
cell_id = mesh.bounding_box_tree().compute_first_entity_collision(x_point)
cell = Cell(mesh, cell_id)
coordinate_dofs = el.tabulate_dof_coordinates(cell)

for i in range(el.space_dimension()):
    v = el.evaluate_basis(i, x, coordinate_dofs, cell.orientation())
    print(i, v)
