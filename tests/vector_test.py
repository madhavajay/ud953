# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a test for the Vector Class"""
from decimal import Decimal, getcontext
import pytest
from vector import Vector

# set the decimal precision
getcontext().prec = 30


# Fixtures
VECTOR_1 = Vector([1, 2, 3])
VECTOR_2 = Vector([5, -3, 6])
VECTOR_3 = Vector([3, 4])
VECTOR_4 = Vector([5.5819, -2.1369])
VECTOR_5 = Vector([2, 2])
VECTOR_6 = Vector([-2, -2])
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
    answer = Vector([0.6, 0.8]).round_coords(1)
    assert answer.magnitude() == Decimal('1.0')
    assert VECTOR_3.normalize() == answer


def test_invert_vector():
    """Test inverting a Vector"""
    vector1 = Vector([5, 5])
    answer = Vector([-5, -5])

    invert_vector = vector1.invert_vector()
    assert invert_vector == answer


def test_round_coords():
    """Test rounding the coordinate scalars in a Vector"""
    answer = Vector([5.582, -2.137]).round_coords(3)
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


def test_is_parallel():
    """Test if two Vectors are parallel"""
    answer1 = False
    assert VECTOR_1.is_parallel(VECTOR_2) == answer1

    answer2 = True
    assert VECTOR_5.is_parallel(VECTOR_6) == answer2


def test_projection():
    """Test the resultant Vector from projecting one vector onto another"""
    vector1 = Vector([2, 1])
    vector2 = Vector([0.825, 2.036])
    answer = Vector([0.630, 1.555]).round_coords(3)

    projected_vector = vector1.project_to(vector2).round_coords(3)
    assert projected_vector == answer


def test_orthogonal_component():
    """Test the orthogonal component Vector of the Vector Projection"""
    vector1 = Vector([2, 1])
    vector2 = Vector([0.825, 2.036])
    answer = Vector([1.370, -0.555]).round_coords(3)

    orthogonal_vector = vector1.orthogonal_component(vector2).round_coords(3)
    assert orthogonal_vector == answer


def test_component_vectors():
    """Test the component Vectors of a Vector given the Baseline Vector"""
    vector1 = Vector([2, 1]).round_coords(3)
    vector2 = Vector([0.825, 2.036])
    answer = Vector([2, 1]).round_coords(3)

    projected_vector = vector1.project_to(vector2)
    orthogonal_vector = vector1.orthogonal_component(vector2)
    sum_components = projected_vector + orthogonal_vector

    assert sum_components == answer


def test_cross_product_error():
    """Test TypeError when trying to use non 3d Vectors with cross_product"""
    with pytest.raises(TypeError) as excinfo:
        VECTOR_1.threed_cross_product(VECTOR_3)
    assert str(excinfo.value) == 'Both vectors must be 3 dimensional'


def test_cross_product():
    """Test 3d dimensional cross product of two Vectors"""
    vector1 = Vector([5, 3, -2])
    vector2 = Vector([-1, 0, 3])
    answer = Vector([9, -13, 3])

    cross_product = vector1.threed_cross_product(vector2)
    assert cross_product == answer
    assert cross_product.is_orthogonal(vector1) is True
    assert cross_product.is_orthogonal(vector2) is True


def test_parallelogram_area():
    """Test calculate the area of parallelogram of two 3d Vectors"""
    vector1 = Vector([5, 3, -2])
    vector2 = Vector([-1, 0, 3])
    answer = Decimal('16.093')

    area = round(vector1.threed_parallelogram_area(vector2), 3)
    assert area == answer


def test_triangle_area():
    """Test calculate the area of triangle of two 3d Vectors"""
    vector1 = Vector([5, 3, -2])
    vector2 = Vector([-1, 0, 3])
    answer = Decimal('8.047')

    area = round(vector1.threed_triangle_area(vector2), 3)
    assert area == answer


def test_iterable():
    """Test that Vector coordinates are iterable"""
    vector1 = Vector([1, 2, 3])
    array = [1, 2, 3]

    for i, coord in enumerate(vector1):
        assert coord == array[i]


def test_index_get():
    """Test that Vector can be accessed with [] indexing"""
    vector1 = Vector([1, 2, 3])
    answer = 3

    assert vector1[2] == answer


def test_index_set():
    """Test that Vector can be set with [] indexing"""
    vector1 = Vector([1, 2, 2])
    answer = 3

    assert vector1[2] == 2
    vector1[2] = 3
    assert vector1[2] == answer
