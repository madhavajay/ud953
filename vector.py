# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a mathematical Vector Class"""

import math
import numbers


class Vector(object):

    """Initialise a new Vector with an Array of Coordinates"""
    def __init__(self, coords):
        try:
            if not coords:
                raise ValueError
            self.coords = tuple(coords)
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
        if isinstance(val, numbers.Integral):
            return self._scalar_operate(operator, val)
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
        return math.sqrt(magnitude_sqrd)

    def normalize(self):
        """Finds the normalized Vector where the magnitude == 1"""
        magnitude = self.magnitude()
        if magnitude == 0:
            raise ZeroDivisionError('A zero vector cannot be normalized')
        else:
            return Vector([(x / magnitude) for x in self.coords])