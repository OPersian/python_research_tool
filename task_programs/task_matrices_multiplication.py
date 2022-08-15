"""
Task on 2D matrices' multiplication, w/ and w/o user-defined objects.

Matrices' sizes to check (elements): 512, 1024, 2048.
"""
import time
from typing import Optional
from numbers import Number


from task_programs.constants import (
    FILLER_INT,
    MAX_NUMBER,
)

# Matrix sizes
SMALL = 512
MEDIUM = 1024
LARGE = 2048
# SMALL = 200
# MEDIUM = 400
# LARGE = 1024

MEASUREMENTS_NUMBER = 100


# TODO MatricesMultiplicationTaskConfig
# TODO MatricesMultiplicationTask


class Matrix:
    """
    Matrix functionality.
    """

    def __init__(
        self,
        dims: tuple,
        fill: Optional[Number] = FILLER_INT,
    ):
        """
        Create a matrix.

        Arguments:
            dims (tuple): dimensions - number of rows and columns.
            fill (int | float | None): filler element to fill a matrix with.
        """
        self.rows_no = dims[0]
        self.cols_no = dims[1]
        self.A = [[fill] * self.cols_no for _ in range(self.rows_no)]

    def __repr__(self):
        m = len(self.A)  # first dim
        mtx_str = ''

        for i in range(m):
            mtx_str += (', '.join(map(lambda x: '{0:8.3f}'.format(x), self.A[i])) + '\n')

        return mtx_str

    def multiply(self, other):
        """
        Multiplication of matrices.

        Multiply the elements in the same row of the first matrix
        to the elements in the same col of the second matrix.

        Return:
            results (tuple): product matrix (`Matrix`) and
                execution time of multiplication in seconds (float).
        """
        min_duration = MAX_NUMBER
        matrix = None

        for _ in range(MEASUREMENTS_NUMBER):
            start = time.time()  # before matrix init

            matrix = Matrix(dims=(self.rows_no, self.cols_no), fill=None)  # None, not 0 (None is smaller than int)

            for i in range(self.rows_no):
                for j in range(self.cols_no):
                    acc = 0
                    for k in range(self.rows_no):
                        acc += self.A[i][k] * other.A[k][j]
                    matrix.A[i][j] = acc

            end = time.time()
            cur_duration = end - start
            if cur_duration < min_duration:
                min_duration = cur_duration

        return matrix, min_duration


def create_matrices(matrix_size, is_oop=True, fill=FILLER_INT):
    """
    Initialize and return 2 matrices.
    """
    if is_oop:
        x = Matrix(dims=(matrix_size, matrix_size), fill=fill)
        y = Matrix(dims=(matrix_size, matrix_size), fill=fill)
    else:
        x = [[fill] * matrix_size for _ in range(matrix_size)]
        y = [[fill] * matrix_size for _ in range(matrix_size)]

    return x, y


def multiply_func(matrix_size, fill=FILLER_INT):
    """
    Matrix multiplication (functional approach).

    Return:
        results (tuple): product matrix (list) and
            execution time of multiplication in seconds (float).
    """
    x, y = create_matrices(matrix_size, fill=fill, is_oop=False)
    min_duration = MAX_NUMBER
    result = None

    start = time.time()  # before result matrix init
    for _ in range(MEASUREMENTS_NUMBER):

        # result = [[0] * matrix_size for _ in range(matrix_size)]

        # for i in range(len(x)):
        #     for j in range(len(y[0])):
        #         for k in range(len(y)):  # rows
        #             result[i][j] += x[i][k] * y[k][j]

        result = [[sum(a * b for a, b in zip(x_row, y_col)) for y_col in zip(*y)] for x_row in x]

        end = time.time()
        cur_duration = end - start

        if cur_duration < min_duration:
            min_duration = cur_duration

    return result, min_duration


def multiply_oop(matrix_size, fill=FILLER_INT):
    """
    Matrix multiplication (OOP approach).
    """
    x, y = create_matrices(matrix_size, fill=fill)
    return x.multiply(y)
