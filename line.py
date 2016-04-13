# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a mathematical Line Class"""

from decimal import Decimal, getcontext
from inaccurate_decimal import InaccurateDecimal
from nonzero import NoNonZeroElements

from vector import Vector

getcontext().prec = 30


class Line(object):
    """Line class in the form Ax + By = C"""

    NO_NONZERO_ELTS_FOUND_MSG = 'No nonzero elements found'

    """Initialise a new Line with a normal Vector and a Constant Term"""
    def __init__(self, normal_vector=None, constant_term=None):
        self.dimension = 2

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

    def direction_vector(self):
        """Return the Direction Vector of a Line where A,B becomes B,-A"""
        return Vector([self.normal_vector[1], -self.normal_vector[0]])

    def is_parallel(self, line):
        """Determine if two Lines are parallel"""
        return self.normal_vector.is_parallel(line.normal_vector)

    def point_for_x(self, x_coord):
        """
        Ax + By = C
        Get a point given a x co-ordinate where y = m x + b
        """
        b_coefficient = self.normal_vector[1]
        c_constant = self.constant_term
        m_gradient = self.gradient()
        y_coord = m_gradient * x_coord + c_constant / b_coefficient
        return Decimal(x_coord), Decimal(y_coord)

    def line_relationship(self, line):
        """Return the relationship of the Lines"""
        if self.is_coincidence(line) is True:
            return 'lines are coincidental'
        elif self.is_parallel is True:
            return 'lines are parallel'
        else:
            x_coord, y_coord = self.point_of_intersection(line)
            if x_coord is not None:
                x_coord = round(Decimal(x_coord), 3)
            if y_coord is not None:
                y_coord = round(Decimal(y_coord), 3)
            intersection = x_coord, y_coord
            return 'lines intersect at {}'.format(intersection)

    def gradient(self):
        """Get the gradient of the Line represented as m"""
        a_coefficient = self.normal_vector[0]
        b_coefficient = self.normal_vector[1]
        m_gradient = -a_coefficient / b_coefficient
        return m_gradient

    def point_of_intersection(self, line):
        """Find the point of intersection between two Lines"""
        if self.is_parallel(line) is True:
            return None, None

        a1_coefficient = self.normal_vector[0]
        b1_coefficient = self.normal_vector[1]
        c1_constant = self.constant_term

        a2_coefficient = line.normal_vector[0]
        b2_coefficient = line.normal_vector[1]
        c2_constant = line.constant_term

        determinant = (a1_coefficient * b2_coefficient) - \
                      (b1_coefficient * a2_coefficient)
        determinant_x = (c1_constant * b2_coefficient) - \
                        (b1_coefficient * c2_constant)
        determinant_y = (a1_coefficient * c2_constant) - \
                        (c1_constant * a2_coefficient)
        x_coord = determinant_x / determinant
        y_coord = determinant_y / determinant
        return Decimal(x_coord), Decimal(y_coord)

    def is_coincidence(self, line):
        """
        Determine if two Lines are coincidence Lines
        Where a new line with any point from each is also parallel
        To both lines
        """

        if self.is_parallel(line) is False:
            return False

        # get a vector as the difference between to different points on
        # both lines
        vector = Vector(self.point_for_x(1)) - Vector(line.point_for_x(2))

        # this vector should be orthogonal to the normal vector of both lines
        orthogonal1 = vector.is_orthogonal(self.normal_vector)
        orthogonal2 = vector.is_orthogonal(line.normal_vector)

        return orthogonal1 and orthogonal2

    def set_basepoint(self):
        """Calculates the basepoint where the line intersects x or y"""
        try:
            normal_vector = self.normal_vector
            constant = self.constant_term
            basepoint_coords = ['0'] * self.dimension

            initial_index = Line.first_nonzero_index(normal_vector)
            initial_coefficient = normal_vector[initial_index]

            basepoint_coords[initial_index] = constant / initial_coefficient
            self.basepoint = Vector(basepoint_coords)

        except NoNonZeroElements as error:
            if str(error) == Line.NO_NONZERO_ELTS_FOUND_MSG:
                self.basepoint = None
            else:
                raise error

    def __str__(self):

        num_decimal_places = 3

        def write_coefficient(coefficient, is_initial_term=False):
            """Print the coefficient as a readable string in Ax + By = C"""
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
            initial_index = Line.first_nonzero_index(normal_vector)
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
        raise NoNonZeroElements(Line.NO_NONZERO_ELTS_FOUND_MSG)
