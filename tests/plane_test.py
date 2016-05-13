# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a test for the Plane Class"""
from vector import Vector
from plane import Plane


def test_add_planes():
    """Test Adding two Planes"""
    plane_1 = Plane(Vector([1, 2, 3]), 4)
    plane_2 = Plane(Vector([-1, 7, 3]), 1)
    plane_3 = plane_1 + plane_2

    answer = Plane(Vector([0, 9, 6]), 5)

    assert plane_3 == answer


def test_plane_set_basepoint():
    """Test Plane Base Point"""
    vector1 = Vector([1, 2, 3])
    constant = 2
    answer = Vector([2, 0, 0])

    plane = Plane(vector1, constant)
    basepoint = plane.basepoint

    assert basepoint == answer


def test_get_plane_coord():
    """Test getting coord value with [] syntax"""
    vector1 = Vector([1, 2, 3])
    constant = 2
    plane = Plane(vector1, constant)
    answer = 1

    x_coord = plane[0]
    assert x_coord == answer


def test_set_plane_point():
    """Test setting plane coord with [] syntax"""
    vector1 = Vector([1, 2])
    constant = 2
    plane = Plane(vector1, constant)
    answer = 3

    x_coord = plane[0]
    assert x_coord == 1
    plane[0] = 3
    assert plane[0] == answer


def test_plane_is_parallel():
    """Test if a plane is parallel"""
    plane1 = Plane(Vector([2, 3, 4]), 6)
    plane2 = Plane(Vector([2, 3, 4]), 1)

    assert plane1.is_parallel(plane2) is True
    assert plane1.is_coincidence(plane2) is False


def test_plane_is_coincidence_scale():
    """Test if a plane is a coincidece"""
    plane1 = Plane(Vector([2, 3, 4]), 1)
    plane2 = Plane(Vector([4, 6, 8]), 2)

    assert plane1.is_parallel(plane2) is True
    assert plane1.is_coincidence(plane2) is True
    assert plane1.plane_relationship(plane2) == 'planes are coincidental'
