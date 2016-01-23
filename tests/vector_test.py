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
ZERO_VECTOR = Vector([0, 0])


def test_vector_add():
    """Test Vector Addition"""
    vector_sum = VECTOR_1 + VECTOR_2
    answer = Vector([6, -1, 9])
    assert answer == vector_sum


def test_vector_add_scalar():
    """Test adding a scalar to each coordinate of a Vector"""
    vector_sum = VECTOR_1 + 1
    answer = Vector([2, 3, 4])
    assert answer == vector_sum


def test_vector_subtract():
    """Test Vector Subtraction"""
    vector_sub = VECTOR_1 - VECTOR_2
    answer = Vector([-4, 5, -3])
    assert answer == vector_sub


def test_vector_subtract_scalar():
    """Test subtracting a scalar from each coordinate of a Vector"""
    vector_sub = VECTOR_1 - 1
    answer = Vector([0, 1, 2])
    assert answer == vector_sub


def test_vector_multiply():
    """Test Vector Multiplication"""
    vector_mul = VECTOR_1 * VECTOR_2
    answer = Vector([5, -6, 18])
    assert answer == vector_mul


def test_vector_multiply_scalar():
    """Test multiplying a scalar into each coordinate of a Vector"""
    vector_mul = VECTOR_1 * 2
    answer = Vector([2, 4, 6])
    assert answer == vector_mul


def test_vector_magnitude():
    """Test calculating the magnitude of a Vector"""
    answer = 5.0
    assert answer == VECTOR_3.magnitude()


def test_vector_normalize():
    """Test normalizing a Vector"""
    answer = Vector([0.6, 0.8])
    assert answer.magnitude() == 1.0
    assert answer == VECTOR_3.normalize()


def test_round_coords():
    """Test rounding the coordinate scalars in a Vector"""
    answer = Vector([5.582, -2.137])
    assert answer == VECTOR_4.round_coords(3)


def test_vector_normalize_zero():
    """Test ZeroDivisionError when trying to normalize a ZeroVector"""
    with pytest.raises(ZeroDivisionError) as excinfo:
        ZERO_VECTOR.normalize()
    assert str(excinfo.value) == 'A zero vector cannot be normalized'
