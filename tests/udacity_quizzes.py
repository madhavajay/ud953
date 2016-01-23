# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""
This is a test that answers the Udacity Quizzes for ud953
https://www.udacity.com/course/linear-algebra-refresher-course--ud953
"""
from vector import Vector


def test_plus_minus_scalar_multiply():
    """Quiz 1 addition, subtraction and multiplication with Vectors"""
    vector1 = Vector([8.218, -9.341])
    vector2 = Vector([-1.129, 2.111])
    answer1 = Vector([7.089, -7.23])
    assert answer1 == (vector1 + vector2).round_coords(3)

    vector3 = Vector([8.218, -9.341])
    vector4 = Vector([-1.129, 2.111])
    answer2 = Vector([7.089, -7.23])
    assert answer2 == (vector3 - vector4).round_coords(3)

    scalar1 = 7.41
    vector5 = Vector([1.671, -1.012, -0.318])
    answer3 = Vector([12.382, -7.499, -2.356])
    assert answer3 == (vector5 * scalar1).round_coords(3)


def test_magnitude_and_normalize():
    """Quiz 2 calculating magnitude and normalization of Vectors"""
    vector1 = Vector([-0.221, 7.437])
    answer1 = 7.440
    assert answer1 == round(vector1.magnitude(), 3)

    vector2 = Vector([8.813, -1.331, -6.247])
    answer2 = 10.884
    assert answer2 == round(vector2.magnitude(), 3)

    vector3 = Vector([5.581, -2.136])
    answer3 = Vector([0.934, -0.357])
    assert answer3 == vector3.normalize().round_coords(3)

    vector4 = Vector([1.996, 3.108, -4.554])
    answer4 = Vector([0.340, 0.530, -0.777])
    assert answer4 == vector4.normalize().round_coords(3)
