# -*- coding: utf-8 -*-
# Author: github.com/madhavajay
"""This is a mathematical Linear System Class"""

from copy import deepcopy
from decimal import Decimal

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

    def compute_triangular_form(self):
        """Compute Triangular Form"""
        triangular = deepcopy(self)

        rows = len(triangular.planes)
        dims = triangular.dimension
        dim = 0
        for row in range(0, rows - 1):
            while dim < dims:
                coefficient = triangular.planes[row][dim]
                if coefficient == 0:
                    # we need to swap it for a row we can use to cancel
                    swap = False
                    for next_row in range(row + 1, rows - 1):
                        if triangular.planes[next_row][dim] > 0:
                            triangular.swap_rows(row, next_row)
                            swap = True
                    if swap is False:
                        dim = dim + 1
                else:
                    # we want to use the current row to clear the other others
                    for next_row in range(row + 1, rows):
                        coefficient_remove = triangular.planes[next_row][dim]
                        # negative and positive are valid, is completed already
                        if coefficient_remove != 0:
                            factor = (coefficient_remove / coefficient) * -1
                            reduction_plane = triangular.planes[row] * factor
                            triangular.planes[next_row] = (
                                triangular.planes[next_row] + reduction_plane)
                    # after doing this we need to move to the next row
                    break

        return triangular

    def clear_coefficients_up(self, row, dim):
        """Go up from the row and clear above rows with the current row"""
        for next_row in range(row)[::-1]:
            plane = self.planes[next_row]
            sub_factor = -plane[dim]
            self.add_multiple_times_row_to_row(sub_factor, row, next_row)

    def scale_coefficient_to_one(self, row, dim):
        """Scale the row to a 1 so that it can be used to clear above"""
        plane = self.planes[row]
        coefficient = plane[dim]
        sub_factor = Decimal(1) / Decimal(coefficient)
        self.planes[row] = plane * sub_factor

    def print_solution(self):
        """Print out the equation in the form of A = K1, B = K2 etc"""
        solutions = []
        term = ord('a')

        pivots = self.get_first_nonzero_indexes()
        for row, dim in enumerate(pivots):
            if dim > -1:
                plane = self.planes[row]
                solutions.append('{} = {}'.format(
                    chr(term), round(plane.constant_term, 3)))
                term = term + 1
        return ', '.join(solutions)

    def system_solutions(self):
        """
        Return the solutions of the System
        # if there is 0 = k there are no solutions
        # if there are less planes than dimensions there are infinite solutions
        # if there are more than 1 pivot variable there are infinite solutions
        # otherwise there is a single solution
        """

        rref = self.compute_rref_form()

        dims = rref.dimension
        rows = len(rref.planes)
        if rows < dims:
            return 'system has no consistent solutions'

        row = 0
        empty_rows = 0
        is_inconsistent = False
        could_be_infinite = False

        for row in range(0, rows):
            # check how many pivot variables
            plane = rref.planes[row]
            unique_values = set(plane.normal_vector.round_coords(3))
            non_zero_values = unique_values.difference([0])

            if len(non_zero_values) > 1:
                could_be_infinite = True
            row_total = 0
            for dim in range(0, dims):
                row_total = row_total + plane[dim]
            row_total = round(row_total, 3)
            constant_term = round(plane.constant_term, 3)

            # if the coefficients are 0
            if row_total == 0:
                # if the constant term is also 0
                if constant_term == 0:
                    empty_rows = empty_rows + 1
                else:
                    # the system is inconsistent
                    is_inconsistent = True
                    break
        if is_inconsistent:
            return 'system has no consistent solutions'
        elif could_be_infinite or rows - empty_rows < dims:
            return 'system has infinite solutions'
        else:
            return 'solution is: {}'.format(rref.print_solution())

    def compute_rref_form(self):
        """Compute RREF Reduced Row Echelon Form"""
        triangular = self.compute_triangular_form()
        rows = len(triangular)
        pivots = triangular.get_first_nonzero_indexes()

        for row in range(rows)[::-1]:
            dim = pivots[row]
            if dim < 0:
                continue
            coefficient = triangular.planes[row][dim]
            if coefficient != 0:
                triangular.scale_coefficient_to_one(row, dim)
                triangular.clear_coefficients_up(row, dim)

        return triangular
