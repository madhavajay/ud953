# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a test for the Linear System Class"""

from vector import Vector
from line import Line
from plane import Plane
from linsys import LinearSystem


def test_linsys_basepoint():
    """Test Linear System Base Point"""

    plane_1 = Plane(normal_vector=Vector(['1', '1', '1']), constant_term='1')
    plane_2 = Plane(normal_vector=Vector(['0', '1', '0']), constant_term='2')
    plane_3 = Plane(normal_vector=Vector(['1', '1', '-1']), constant_term='3')
    plane_4 = Plane(normal_vector=Vector(['1', '0', '-2']), constant_term='2')

    system = LinearSystem([plane_1, plane_2, plane_3, plane_4])

    system[0] = plane_1

    vector1 = Vector([1, 2])
    constant = 2
    answer = Vector([2, 0])

    line = Line(vector1, constant)
    basepoint = line.basepoint

    assert basepoint == answer
