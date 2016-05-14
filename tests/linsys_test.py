# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a test for the Linear System Class"""

from vector import Vector
from line import Line
from plane import Plane
from linsys import LinearSystem


def test_linsys_basepoint():
    """Test Linear System Base Point"""

    plane_1 = Plane(Vector([1, 1, 1]), 1)
    plane_2 = Plane(Vector([0, 1, 0]), 2)
    plane_3 = Plane(Vector([1, 1, -1]), 3)
    plane_4 = Plane(Vector([1, 0, -2]), 2)

    system = LinearSystem([plane_1, plane_2, plane_3, plane_4])

    system[0] = plane_1

    vector1 = Vector([1, 2])
    constant = 2
    answer = Vector([2, 0])

    line = Line(vector1, constant)
    basepoint = line.basepoint

    assert basepoint == answer


def test_linsys_swap_row():
    """Test Linear System Swap Row"""
    plane_1 = Plane(Vector([1, 1, 1]), 1)
    plane_2 = Plane(Vector([0, 1, 0]), 2)
    plane_3 = Plane(Vector([1, 1, -1]), 3)
    plane_4 = Plane(Vector([1, 0, -2]), 2)

    lin_sys = LinearSystem([plane_1, plane_2, plane_3, plane_4])
    lin_sys.swap_rows(0, 1)
    assert lin_sys[0] == plane_2  # swapped
    assert lin_sys[1] == plane_1  # swapped
    assert lin_sys[2] == plane_3
    assert lin_sys[3] == plane_4

    lin_sys.swap_rows(1, 3)
    assert lin_sys[0] == plane_2
    assert lin_sys[1] == plane_4  # swapped
    assert lin_sys[2] == plane_3
    assert lin_sys[3] == plane_1  # swapped

    lin_sys.swap_rows(3, 1)
    assert lin_sys[0] == plane_2
    assert lin_sys[1] == plane_1  # swapped
    assert lin_sys[2] == plane_3
    assert lin_sys[3] == plane_4  # swapped


def test_linsys_multiply_row():
    """Test Linear System Multiply Coefficient and Row"""
    plane_1 = Plane(Vector([1, 1, 1]), 1)
    plane_2 = Plane(Vector([0, 1, 0]), 2)
    plane_3 = Plane(Vector([1, 1, -1]), 3)
    plane_4 = Plane(Vector([1, 0, -2]), 2)

    # same as the end of the last test
    lin_sys = LinearSystem([plane_2, plane_1, plane_3, plane_4])

    lin_sys.multiply_coefficient_and_row(1, 0)

    assert lin_sys[0] == plane_2
    assert lin_sys[1] == plane_1
    assert lin_sys[2] == plane_3
    assert lin_sys[3] == plane_4

    lin_sys.multiply_coefficient_and_row(-1, 2)
    new_plane_3 = Plane(Vector([-1, -1, 1]), -3)

    assert lin_sys[0] == plane_2
    assert lin_sys[1] == plane_1
    assert lin_sys[2] == new_plane_3
    assert lin_sys[3] == plane_4

    lin_sys.multiply_coefficient_and_row(10, 1)

    new_plane_1 = Plane(Vector([10, 10, 10]), 10)

    assert lin_sys[0] == plane_2
    assert lin_sys[1] == new_plane_1
    assert lin_sys[2] == new_plane_3
    assert lin_sys[3] == plane_4


def test_linsys_multiply_row_add():
    """Test Linear System Multiply Times Row and add to Row"""
    plane_2 = Plane(Vector([0, 1, 0]), 2)
    new_plane_1 = Plane(Vector([10, 10, 10]), 10)
    new_plane_3 = Plane(Vector([-1, -1, 1]), -3)
    plane_4 = Plane(Vector([1, 0, -2]), 2)

    # same as the end of the last test
    lin_sys = LinearSystem([plane_2, new_plane_1, new_plane_3, plane_4])

    # multiply the first row by 0 and add to the second row
    # this should have no affect
    lin_sys.add_multiple_times_row_to_row(0, 0, 1)

    assert lin_sys[0] == plane_2
    assert lin_sys[1] == new_plane_1
    assert lin_sys[2] == new_plane_3
    assert lin_sys[3] == plane_4

    # multiply the first row by 1 and add it to the second row
    lin_sys.add_multiple_times_row_to_row(1, 0, 1)

    plane_1_added = Plane(Vector([10, 11, 10]), 12)

    assert lin_sys[0] == plane_2
    assert lin_sys[1] == plane_1_added
    assert lin_sys[2] == new_plane_3
    assert lin_sys[3] == plane_4

    # multiply the second row by -1 and add to the first row
    lin_sys.add_multiple_times_row_to_row(-1, 1, 0)

    plane_2_subtracted = Plane(Vector([-10, -10, -10]), -10)

    assert lin_sys[0] == plane_2_subtracted
    assert lin_sys[1] == plane_1_added
    assert lin_sys[2] == new_plane_3
    assert lin_sys[3] == plane_4


def test_triangular_form():
    """Test for Triangular Form"""

    plane_1 = Plane(Vector([0, 1, 1]), 1)
    plane_2 = Plane(Vector([1, -1, 1]), 2)
    plane_3 = Plane(Vector([1, 2, -5]), 3)

    lin_sys = LinearSystem([plane_1, plane_2, plane_3])
    triangular = lin_sys.compute_triangular_form()

    assert triangular[0] == Plane(Vector([1, -1, 1]), 2)
    assert triangular[1] == Plane(Vector([0, 1, 1]), 1)
    assert triangular[2] == Plane(Vector([0, 0, -9]), -2)
