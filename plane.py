# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a mathematical Plane Class"""

from decimal import Decimal, getcontext

from vector import Vector

getcontext().prec = 30


class Plane(object):
    """Plane class in the form Ax + By + Cz = K"""

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    """Initialise a new Plane with a normal Vector and a Constant Term"""
    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 3

        if not normal_vector:
            all_zeros = ['0'] * self.dimension
            normal_vector = Vector(all_zeros)
        self.normal_vector = normal_vector

        if not constant_term:
            constant_term = Decimal('0')
        self.constant_term = Decimal(constant_term)

        self.set_basepoint()

    def __getitem__(self, index):
        return self.normal_vector[index]

    def __setitem__(self, index, value):
        new_vals = []
        for i, val in enumerate(self.normal_vector):
            if i == index:
                val = value
            new_vals.append(val)

        self.normal_vector = Vector(tuple([Decimal(x) for x in new_vals]))

    def is_parallel(self, plane):
        """Determine if two Planes are parallel"""
        return self.normal_vector.is_parallel(plane.normal_vector)

    def plane_relationship(self, plane):
        """Return the relationship of the Planes"""
        if self.is_coincidence(plane) is True:
            return 'planes are coincidental'
        elif self.is_parallel(plane) is True:
            return 'planes are parallel'
        else:
            return 'planes are not parallel'

    def point_for_x_y(self, x_coord, y_coord):
        """
        Calculate a point with x, y, z passing in x and y
        Ax + By + Cz = k
        z = (k - (Ax + By)) / C
        """
        a1_coefficient = self.normal_vector[0]
        b1_coefficient = self.normal_vector[1]
        c1_coefficient = self.normal_vector[2]
        k1_constant = self.constant_term

        ax_val = a1_coefficient * x_coord
        by_val = b1_coefficient * y_coord

        z_coord = (k1_constant - (ax_val + by_val)) / c1_coefficient
        return Decimal(x_coord), Decimal(y_coord), Decimal(z_coord)

    def is_coincidence(self, plane):
        """
        Determine if two Planes are coincidence Planes
        If they are parallel and a Vector between a point from each plane
        Is orthogonal to the normal vector
        """

        if self.is_parallel(plane) is False:
            return False

        # get a vector as the difference between to different points on
        # both planes
        vector = (Vector(self.point_for_x_y(1, 2)) -
                  Vector(plane.point_for_x_y(2, 3)))

        # this vector should be orthogonal to the normal vector of both planes
        orthogonal1 = vector.is_orthogonal(self.normal_vector)
        orthogonal2 = vector.is_orthogonal(plane.normal_vector)

        return orthogonal1 and orthogonal2

    def set_basepoint(self):
        """Calculates the basepoint where the plane intersects x, y or z"""
        try:
            normal_vector = self.normal_vector
            constant = self.constant_term
            basepoint_coords = ['0'] * self.dimension

            initial_index = Plane.first_nonzero_index(normal_vector)
            initial_coefficient = normal_vector[initial_index]

            basepoint_coords[initial_index] = constant / initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except NoNonZeroElements as error:
            if str(error) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise error

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            """Print the coefficient as a readable string Ax + By + Cz = K"""
            coefficient = round(coefficient, num_decimal_places)
            if coefficient % 1 == 0:
                coefficient = int(coefficient)

            output = ''

            if coefficient < 0:
                output += '-'
            if coefficient > 0 and not is_initial_term:
                output += '+'

            if not is_initial_term:
                output += ' '

            if abs(coefficient) != 1:
                output += '{}'.format(abs(coefficient))

            return output

        normal_vector = self.normal_vector

        try:
            initial_index = Plane.first_nonzero_index(normal_vector)
            terms = ([
                (write_coefficient(
                    normal_vector[i],
                    is_initial_term=(i == initial_index)) + 'x_{}'.format(i+1))
                for i in range(self.dimension)
                if round(normal_vector[i], num_decimal_places) != 0
            ])
            output = ' '.join(terms)

        except NoNonZeroElements as error:
            if str(error) == self.NO_NONZERO_ELTS_FOUND_MSG:
                output = '0'
            else:
                raise error

        constant = round(self.constant_term, num_decimal_places)
        if constant % 1 == 0:
            constant = int(constant)
        output += ' = {}'.format(constant)

        return output

    @staticmethod
    def first_nonzero_index(iterable):
        """Find the first non zero value"""
        for k, item in enumerate(iterable):
            if not InaccurateDecimal(item).is_near_zero():
                return k
        raise NoNonZeroElements(Plane.NO_NONZERO_ELTS_FOUND_MSG)


class InaccurateDecimal(Decimal):
    """Utility wrapper class to detect values close to 0"""
    def is_near_zero(self, eps=1e-10):
        """Checks if value is virtually 0"""
        return abs(self) < eps


class NoNonZeroElements(Exception):
    """Custom Error for No None Zero Elements in a Plane"""
    def __init__(self, *args, **kwargs):
        Exception.__init__(self, *args, **kwargs)
