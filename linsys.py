# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a mathematical Linear System Class"""

from nonzero import NoNonZeroElements
from plane import Plane


class LinearSystem(object):
    """Creates a linear system of equations for solving"""

    SAME_DIM_MSG = 'All planes in the system should live in the same dimension'
    NO_SOLUTIONS_MSG = 'No solutions'
    INF_SOLUTIONS_MSG = 'Infinitely many solutions'

    def __init__(self, planes):
        try:
            dim = planes[0].dimension
            for plane in planes:
                assert plane.dimension == dim

            self.planes = planes
            self.dimension = dim

        except AssertionError:
            raise Exception(self.SAME_DIM_MSG)

    def swap_rows(self, index_1, index_2):
        """Swap two rows in the linear system to achieve triangular form"""
        row_1 = self.planes[index_1]
        self.planes[index_1] = self.planes[index_2]
        self.planes[index_2] = row_1

    def multiply_coefficient_and_row(self, coefficient, row):
        """Multiply a particular coefficient in a row"""
        plane = self.planes[row]
        plane = plane * coefficient
        self.planes[row] = plane

    def add_multiple_times_row_to_row(self, coefficient, row_to_add,
                                      row_to_be_added_to):
        """Add a multiple of one row to another to help resolve"""

        plane = self.planes[row_to_add]
        plane = plane * coefficient

        self.planes[row_to_be_added_to] += plane

    def get_first_nonzero_indexes(self):
        """Get the indices of the first nonzero term in each row"""
        num_equations = len(self)
        # num_variables = self.dimension

        indices = [-1] * num_equations

        for i, plane in enumerate(self.planes):
            try:
                indices[i] = plane.first_nonzero_index(plane.normal_vector)
            except NoNonZeroElements as err:
                if str(err) == Plane.NO_NONZERO_ELTS_FOUND_MSG:
                    continue
                else:
                    raise err
        return indices

    def __len__(self):
        return len(self.planes)

    def __getitem__(self, index):
        return self.planes[index]

    def __setitem__(self, index, plane):
        try:
            assert plane.dimension == self.dimension
            self.planes[index] = plane

        except AssertionError:
            raise Exception(self.SAME_DIM_MSG)

    def __str__(self):
        ret = 'Linear System:\n'
        str_format = 'Equation {}: {}'
        temp = [str_format.format(i + 1, p) for i, p in enumerate(self.planes)]
        ret += '\n'.join(temp)
        return ret

    def compute_rref(self):
        """Compute the Reduced Row Echelon Form"""
        pass
