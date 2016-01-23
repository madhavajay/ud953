# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a test for the Vector Class"""
import pytest
from vector import Vector


# Fixtures
VECTOR_1 = Vector([1, 2, 3])
VECTOR_2 = Vector([5, -3, 6])
VECTOR_3 = Vector([3, 4])
VECTOR_4 = Vector([5.5819, -2.1369])
VECTOR_5 = Vector([5.5819, -2.1369])
ZERO_VECTOR = Vector([0, 0])


def test_vector_add():
    """Test Vector Addition"""
    vector_sum = VECTOR_1 + VECTOR_2
    answer = Vector([6, -1, 9])
    assert vector_sum == answer


def test_vector_add_scalar():
    """Test adding a scalar to each coordinate of a Vector"""
    vector_sum = VECTOR_1 + 1
    answer = Vector([2, 3, 4])
    assert vector_sum == answer


def test_vector_subtract():
    """Test Vector Subtraction"""
    vector_sub = VECTOR_1 - VECTOR_2
    answer = Vector([-4, 5, -3])
    assert vector_sub == answer


def test_vector_subtract_scalar():
    """Test subtracting a scalar from each coordinate of a Vector"""
    vector_sub = VECTOR_1 - 1
    answer = Vector([0, 1, 2])
    assert vector_sub == answer


def test_vector_multiply():
    """Test Vector Multiplication"""
    vector_mul = VECTOR_1 * VECTOR_2
    answer = Vector([5, -6, 18])
    assert vector_mul == answer


def test_vector_multiply_scalar():
    """Test multiplying a scalar into each coordinate of a Vector"""
    vector_mul = VECTOR_1 * 2
    answer = Vector([2, 4, 6])
    assert vector_mul == answer


def test_vector_magnitude():
    """Test calculating the magnitude of a Vector"""
    answer = 5.0
    assert VECTOR_3.magnitude() == answer


def test_vector_normalize():
    """Test normalizing a Vector"""
    answer = Vector([0.6, 0.8])
    assert answer.magnitude() == 1.0
    assert VECTOR_3.normalize() == answer


def test_round_coords():
    """Test rounding the coordinate scalars in a Vector"""
    answer = Vector([5.582, -2.137])
    assert VECTOR_4.round_coords(3) == answer


def test_vector_normalize_zero():
    """Test ZeroDivisionError when trying to normalize a ZeroVector"""
    with pytest.raises(ZeroDivisionError) as excinfo:
        ZERO_VECTOR.normalize()
    assert str(excinfo.value) == 'A zero vector cannot be normalized'


def test_sum_coordinates():
    """Test the sum of a Vectors coordinates"""
    answer = 6
    assert VECTOR_1.sum_coordinates() == answer


def test_dot_product():
    """Test calculating the dot_product of two Vectors"""
    answer = 17
    assert VECTOR_1.dot_product(VECTOR_2) == answer


def test_angle_radians():
    """Test calculating the angle in radians between two Vectors"""
    answer = 0.997
    assert round(VECTOR_1.angle_radians(VECTOR_2), 3) == answer


def test_angle_degrees():
    """Test calculating the angle in degrees between two Vectors"""
    answer = 57.109
    assert round(VECTOR_1.angle_degrees(VECTOR_2), 3) == answer
