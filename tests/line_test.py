# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a test for the Line Class"""
from decimal import Decimal, getcontext
from vector import Vector
from line import Line

# set the decimal precision
getcontext().prec = 30


def test_line_set_basepoint():
    """Test Line Base Point"""
    vector1 = Vector([1, 2])
    constant = 2
    answer = Vector([2, 0])

    line = Line(vector1, constant)
    basepoint = line.basepoint

    assert basepoint == answer


def test_get_line_coord():
    """Test getting coord value with [] syntax"""
    vector1 = Vector([1, 2])
    constant = 2
    line = Line(vector1, constant)
    answer = 1

    x_coord = line[0]
    assert x_coord == answer


def test_set_line_point():
    """Test setting line coord with [] syntax"""
    vector1 = Vector([1, 2])
    constant = 2
    line = Line(vector1, constant)
    answer = 3

    x_coord = line[0]
    assert x_coord == 1
    line[0] = 3
    assert line[0] == answer


def test_direction_vector():
    """Test getting the direction Vector of a Line"""
    line1 = Line(Vector([2, 3]), 6)
    direction_vector = line1.direction_vector()
    answer = Vector([3, -2])

    assert direction_vector == answer


def test_point_for_x():
    """Test getting a point given an x Value"""
    line1 = Line(Vector([2, 3]), 6)

    x1_coord, y1_coord = line1.point_for_x(0)
    x2_coord, y2_coord = line1.point_for_x(3)
    x3_coord, y3_coord = line1.point_for_x(9)

    assert x1_coord == Decimal(0)
    assert y1_coord == Decimal(2)

    assert x2_coord == Decimal(3)
    assert y2_coord == Decimal(0)

    assert x3_coord == Decimal(9)
    assert y3_coord == Decimal(-4)


def test_line_is_parallel():
    """Test if a line is parallel"""
    line1 = Line(Vector([2, 3]), 6)
    line2 = Line(Vector([2, 3]), 1)

    assert line1.is_parallel(line2) is True


def test_line_is_coincidence():
    """Test if a line is a coincidece"""
    line1 = Line(Vector([2, 3]), 1)
    line2 = Line(Vector([2, 3]), 1)

    assert line1.is_parallel(line2) is True
    assert line1.is_coincidence(line2) is True

    line3 = Line(Vector([2, 3]), 6)
    assert line1.is_parallel(line3) is True
    assert line1.is_coincidence(line3) is False


def test_line_intersection():
    """Test if two lines intersect"""
    line1 = Line(Vector([2, 5]), 10)
    line2 = Line(Vector([1, 1]), 5)

    assert line1.is_parallel(line2) is False
    assert line1.point_of_intersection(line2) == (Decimal(5), Decimal(0))
