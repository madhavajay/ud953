# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""
This is a test that answers the Udacity Quizzes for ud953
https://www.udacity.com/course/linear-algebra-refresher-course--ud953
"""
from decimal import Decimal, getcontext
from vector import Vector
from line import Line
from plane import Plane

# set the decimal precision
getcontext().prec = 30


def test_plus_minus_scalar_multiply():
    """Quiz 1 addition, subtraction and multiplication with Vectors"""
    vector1 = Vector([8.218, -9.341])
    vector2 = Vector([-1.129, 2.111])
    answer1 = Vector([7.089, -7.23]).round_coords(3)
    assert (vector1 + vector2).round_coords(3) == answer1

    vector3 = Vector([7.119, 8.215])
    vector4 = Vector([-8.223, 0.878])
    answer2 = Vector([15.342, 7.337]).round_coords(3)
    assert (vector3 - vector4).round_coords(3) == answer2

    scalar1 = 7.41
    vector5 = Vector([1.671, -1.012, -0.318])
    answer3 = Vector([12.382, -7.499, -2.356]).round_coords(3)
    assert (vector5 * scalar1).round_coords(3) == answer3


def test_magnitude_and_normalize():
    """Quiz 2 calculating magnitude and normalization of Vectors"""
    vector1 = Vector([-0.221, 7.437])
    answer1 = Decimal('7.440')
    assert round(vector1.magnitude(), 3) == answer1

    vector2 = Vector([8.813, -1.331, -6.247])
    answer2 = Decimal('10.884')
    assert round(vector2.magnitude(), 3) == answer2

    vector3 = Vector([5.581, -2.136])
    answer3 = Vector([0.934, -0.357]).round_coords(3)
    assert vector3.normalize().round_coords(3) == answer3

    vector4 = Vector([1.996, 3.108, -4.554])
    answer4 = Vector([0.340, 0.530, -0.777]).round_coords(3)
    assert vector4.normalize().round_coords(3) == answer4


def test_dot_product_and_angle():
    """Quiz 3 calculating the dot product and angle of two Vectors"""
    vector1 = Vector([7.887, 4.138])
    vector2 = Vector([-8.802, 6.776])
    answer1 = Decimal('-41.382')
    assert round(vector1.dot_product(vector2), 3) == answer1

    vector3 = Vector([-5.955, -4.904, -1.874])
    vector4 = Vector([-4.496, -8.755, 7.103])
    answer2 = Decimal('56.397')
    assert round(vector3.dot_product(vector4), 3) == answer2

    vector5 = Vector([3.183, -7.627])
    vector6 = Vector([-2.668, 5.319])
    answer3 = 3.072
    assert round(vector5.angle_radians(vector6), 3) == answer3

    vector7 = Vector([7.35, 0.221, 5.188])
    vector8 = Vector([2.751, 8.259, 3.985])
    answer4 = 60.276
    assert round(vector7.angle_degrees(vector8), 3) == answer4


def test_parallel_or_orthogonal():
    """Quiz 4 checking for parallelism and orthogonality"""
    vector1 = Vector([-7.579, -7.88])
    vector2 = Vector([22.737, 23.64])
    assert vector1.is_parallel(vector2) is True
    assert vector1.is_orthogonal(vector2) is False

    vector3 = Vector([-2.029, 9.97, 4.172])
    vector4 = Vector([-9.231, -6.639, -7.245])
    assert vector3.is_parallel(vector4) is False
    assert vector3.is_orthogonal(vector4) is False

    vector5 = Vector([-2.328, -7.284, -1.214])
    vector6 = Vector([-1.821, 1.072, -2.94])
    assert vector5.is_parallel(vector6) is False
    assert vector5.is_orthogonal(vector6) is True

    vector7 = Vector([2.118, 4.827])
    vector8 = Vector([0, 0])
    assert vector7.is_parallel(vector8) is True
    assert vector7.is_orthogonal(vector8) is True


def test_vector_projections():
    """Quiz 5 projecting vectors"""
    vector1 = Vector([3.039, 1.879])
    vector2 = Vector([0.825, 2.036])
    answer1 = Vector([1.083, 2.672]).round_coords(3)

    projected_vector1 = vector1.project_to(vector2).round_coords(3)

    assert projected_vector1 == answer1

    vector3 = Vector([-9.88, -3.264, -8.159])
    vector4 = Vector([-2.155, -9.353, -9.473])
    answer2 = Vector([-8.350, 3.376, -1.434]).round_coords(3)

    orthogonal_vector1 = vector3.orthogonal_component(vector4).round_coords(3)
    assert orthogonal_vector1 == answer2

    vector5 = Vector([3.009, -6.172, 3.692, -2.51]).round_coords(3)
    vector6 = Vector([6.404, -9.144, 2.759, 8.718])
    answer3 = Vector([1.969, -2.811, 0.848, 2.680]).round_coords(3)
    answer4 = Vector([1.040, -3.361, 2.844, -5.190]).round_coords(3)

    projected_vector2 = vector5.project_to(vector6).round_coords(3)
    orthogonal_vector2 = vector5.orthogonal_component(vector6).round_coords(3)
    sum_vector = projected_vector2 + orthogonal_vector2

    assert projected_vector2 == answer3
    assert orthogonal_vector2 == answer4
    assert sum_vector == vector5


def test_cross_products():
    """Quiz 6 cross products"""
    vector1 = Vector([8.462, 7.893, -8.187])
    vector2 = Vector([6.984, -5.975, 4.778])
    answer1 = Vector([-11.205, -97.609, -105.685]).round_coords(3)

    cross_product = vector1.threed_cross_product(vector2).round_coords(3)
    assert cross_product == answer1

    vector3 = Vector([-8.987, -9.838, 5.031])
    vector4 = Vector([-4.268, -1.861, -8.866])
    answer2 = Decimal('142.122')

    parallelogram_area = round(vector3.threed_parallelogram_area(vector4), 3)
    assert parallelogram_area == answer2

    vector5 = Vector([1.5, 9.547, 3.691])
    vector6 = Vector([-6.007, 0.124, 5.772])
    answer3 = Decimal('42.565')

    triangle_area = round(vector5.threed_triangle_area(vector6), 3)
    assert triangle_area == answer3


def test_line_functions():
    """Quiz 7 line functions"""
    line1 = Line(Vector([4.046, 2.836]), 1.21)
    line2 = Line(Vector([10.115, 7.09]), 3.025)

    assert line1.line_relationship(line2) == 'lines are coincidental'

    line3 = Line(Vector([7.204, 3.182]), 8.68)
    line4 = Line(Vector([8.172, 4.114]), 9.883)

    assert line3.line_relationship(line4) == ("lines intersect at "
                                              "(Decimal('1.173'), "
                                              "Decimal('0.073'))")

    line5 = Line(Vector([1.182, 5.562]), 6.744)
    line6 = Line(Vector([1.773, 8.343]), 9.525)

    assert line5.line_relationship(line6) == 'lines intersect at (None, None)'


def test_planes_in_3d():
    """Quiz 8 plane functions"""

    plane1 = Plane(Vector([-0.412, 3.806, 0.728]), -3.46)
    plane2 = Plane(Vector([1.03, -9.515, -1.82]), 8.65)

    assert plane1.is_parallel(plane2) is True
    assert plane1.is_coincidence(plane2) is True
    assert plane1.plane_relationship(plane2) == ('planes are coincidental')

    plane3 = Plane(Vector([2.611, 5.528, 0.283]), 4.6)
    plane4 = Plane(Vector([7.715, 8.306, 5.342]), 3.76)

    assert plane3.is_parallel(plane4) is False
    assert plane3.plane_relationship(plane4) == ('planes are not parallel')

    plane5 = Plane(Vector([-7.926, 8.625, -7.212]), -7.952)
    plane6 = Plane(Vector([-2.642, 2.875, -2.404]), -2.443)

    assert plane5.is_parallel(plane6) is True
    assert plane5.plane_relationship(plane6) == ('planes are parallel')
