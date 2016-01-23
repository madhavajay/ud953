# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a mathematical Vector Class"""

import math
import numbers
from decimal import Decimal, getcontext

# set the decimal precision
getcontext().prec = 30


class Vector(object):

    """Initialise a new Vector with an Array of Coordinates"""
    def __init__(self, coords):
        try:
            if not coords:
                raise ValueError
            self.coords = tuple([Decimal(x) for x in coords])
            self.dimension = len(coords)

        except ValueError:
            raise ValueError('The coordinates must be nonempty')

        except TypeError:
            raise TypeError('The coordinates must be an iterable')

    def __str__(self):
        return 'Vector: {}'.format(self.coords)

    def __eq__(self, vector):
        return self.coords == vector.coords

    def __add__(self, val):
        return self._operate('+', val)

    def __sub__(self, val):
        return self._operate('-', val)

    def __mul__(self, val):
        return self._operate('*', val)

    # pylint: disable=R0201
    def _eval_(self, x_val, operator, y_val):
        """Determine which basic operation to perform on both inputs"""
        if operator == '+':
            return x_val + y_val
        if operator == '-':
            return x_val - y_val
        elif operator == '*':
            return x_val * y_val
        else:
            raise TypeError('operator must be one of + - *')

    def _operate(self, operator, val):
        """Performs operation on Vector against scalar or Vector values"""
        if isinstance(val, (numbers.Integral, numbers.Real)):
            return self._scalar_operate(operator, Decimal(val))
        elif isinstance(val, Vector):
            return self._vector_operate(operator, val)
        else:
            raise TypeError('value must be number or Vector')

    def _scalar_operate(self, operator, val):
        return Vector([self._eval_(i, operator, val) for i in self.coords])

    def _vector_operate(self, operator, vector):
        """Performs operation on Vector against scalar or Vector values"""
        return Vector([self._eval_(x, operator, y) for x, y in zip(
            self.coords, vector.coords)])

    def round_coords(self, decimal_places):
        """Rounds the Coordinates inside the Vector to decimal_places"""
        return Vector([round(i, decimal_places) for i in self.coords])

    def magnitude(self):
        """
        Calculates the magnitude of the Vector
        a_sqrd = b_sqrd + c_sqrd
        """
        magnitude_sqrd = sum([i ** 2 for i in self.coords])
        return Decimal(math.sqrt(magnitude_sqrd))

    def normalize(self):
        """Finds the normalized Vector where the magnitude == 1"""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ZeroDivisionError('A zero vector cannot be normalized')
        else:
            return Vector([(x / magnitude) for x in self.coords])

    def sum_coordinates(self):
        """Sums the coordinates"""
        return sum(self.coords)

    def dot_product(self, vector):
        """
        Calculate the dot_product with another Vector
        Where dot_product == The sum of coordinates in Vector1 * Vector2
        """
        return (self * vector).sum_coordinates()

    def angle_radians(self, vector):
        """
        Calculate the angle between two Vectors in Radians
        Where Theta == arccos(v1 dot v2 / |v1| dot |v2|)
        """
        vector_dot_prod = self.dot_product(vector)
        if self.magnitude() == 0 or vector.magnitude() == 0:
            raise ZeroDivisionError('A zero vector has no angle')

        magnitude_dot_prod = self.magnitude() * vector.magnitude()
        cos_angle = min(1, max(vector_dot_prod / magnitude_dot_prod, -1))
        return math.acos(cos_angle)

    def angle_degrees(self, vector):
        """Calculate the angle between two Vectors in Degrees"""
        return math.degrees(self.angle_radians(vector))

    def is_parallel(self, vector):
        """
        Determine if two Vectors are parallel
        Where their absolute normalized Vectors are the same
        A vector in the opposite direction is still valid
        """
        if self.magnitude() == 0 or vector.magnitude() == 0:
            return True
        v_norm = self.normalize().round_coords(15)
        w_norm = vector.normalize().round_coords(15)
        return (v_norm == w_norm) or (v_norm == (w_norm * -1))

    def is_orthogonal(self, vector):
        """Determine if two Vectors are orthogonal (right angles)"""
        if self.magnitude() == 0 or vector.magnitude() == 0:
            return True
        return self.angle_degrees(vector) == Decimal('90')
