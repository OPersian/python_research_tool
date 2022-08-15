"""
Task on 2D matrices' multiplication, w/ and w/o user-defined objects.

Matrices' sizes to check (elements): 512, 1024, 2048.
"""
import sys
import time
from typing import Optional
from numbers import Number

# Matrix sizes
SMALL = 512
MEDIUM = 1024
LARGE = 2048
# SMALL = 200
# MEDIUM = 400
# LARGE = 1024

# Filler numbers to populate matrices with.
FILLER_INT = 10
FILLER_FLOAT = 10.0

MAX_NUMBER = sys.maxsize
MEASUREMENTS_NUMBER = 100


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


def task_02_runner(fill, matrix_size=None):
    if matrix_size:
        res_func_3 = multiply_func(matrix_size, fill=fill)
        res_oop_3 = multiply_oop(matrix_size, fill=fill)
    else:
        res_func_3 = multiply_func(LARGE, fill=fill)
        res_oop_3 = multiply_oop(LARGE, fill=fill)

    if not matrix_size:
        res_func_1 = multiply_func(SMALL, fill=fill)
        res_oop_1 = multiply_oop(SMALL, fill=fill)
        res_func_2 = multiply_func(MEDIUM, fill=fill)
        res_oop_2 = multiply_oop(MEDIUM, fill=fill)

    # Commented out for the sake of clean output
    # print("Ensure multiplication went right (equal results): ")
    # print("{} x {} func: ".format(LARGE, LARGE))
    # for r in res_func_3[0]:
    #     print(r)
    # print("{} x {} oop: ".format(LARGE, LARGE))
    # print(res_oop_3[0])

    if not matrix_size:
        print("{} x {} matrices".format(SMALL, SMALL))
        print("Func took {} sec".format(res_func_1[1]))
        print("OOP took {} sec".format(res_oop_1[1]))
        print("OOP to func: {}\n".format(res_oop_1[1] / res_func_1[1]))

        print("{} x {} matrices".format(MEDIUM, MEDIUM))
        print("Func took {} sec".format(res_func_2[1]))
        print("OOP took {} sec".format(res_oop_2[1]))
        try:
            print("Func {} to {}: {}".format(MEDIUM, SMALL, res_func_2[1] / res_func_1[1]))
            print("OOP {} to {}: {}".format(MEDIUM, SMALL, res_oop_2[1] / res_oop_1[1]))
            print("OOP to func: {}\n".format(res_oop_2[1] / res_func_2[1]))
        except ZeroDivisionError:
            pass

        print("{} x {} matrices".format(LARGE, LARGE))
        print("Func took {} sec".format(res_func_3[1]))
        print("OOP took {} sec".format(res_oop_3[1]))

    else:
        print("{} x {} matrices".format(matrix_size, matrix_size))
        print("Func took {} sec".format(res_func_3[1]))
        print("OOP took {} sec".format(res_oop_3[1]))

    try:
        if not matrix_size:
            print("Func {} to {}: {}".format(LARGE, SMALL, res_func_3[1] / res_func_1[1]))
            print("OOP {} to {}: {}".format(LARGE, SMALL, res_oop_3[1] / res_oop_1[1]))
        print("OOP to func: {}".format(res_oop_3[1] / res_func_3[1]))
    except ZeroDivisionError:
        pass


def task_02():
    """
    Solution for the task #2.

    Task 8 (Debug vs Release)
    """
    task_02_runner(fill=FILLER_INT)
