"""
Task on arrays addition.

Add a number to array's elements.

Array sizes: 100000, 200000, 300000.
Comparisons: T(200000)/T (100000), T(300000)/T (100000).

TODO consider as future feature:
 Relative measurement: number of times a program gets executed during the given time, `SECONDS_TO_WAIT`.
"""
import sys
import time


# Arrays sizes
SMALL = 100000
MEDIUM = 200000
LARGE = 300000

# Filler number to populate an array with.
FILLER = 0
# Value to add to every array element.
VALUE_TO_ADD = 10

MAX_NUMBER = sys.maxsize
MEASUREMENTS_NUMBER = 100
SECONDS_TO_WAIT = 2


def measure_abs_array_addition(elements_number: int) -> int:
    """
    Provide absolute measurement of array addition execution time.

    Arguments:
        elements_number (int): number of elements in an array.

    Return:
        duration of program execution, seconds (float).
    """
    min_duration = MAX_NUMBER
    array = [FILLER] * elements_number

    for _ in range(MEASUREMENTS_NUMBER):
        start = time.time()

        _ = [n + VALUE_TO_ADD for n in array]

        end = time.time()

        cur_duration = end - start

        if cur_duration < min_duration:
            min_duration = cur_duration

        return min_duration


def measure_rel_array_addition(elements_number: int) -> int:
    """
    Provide relative measurement of array addition execution time.

    Arguments:
        elements_number (int): number of elements in an array.

    Return:
        number of times a program gets executed during the given time, `SECONDS_TO_WAIT` (int)
    """
    array = [FILLER] * elements_number

    count = 0
    tick_initial = time.time()

    while time.time() - tick_initial < SECONDS_TO_WAIT:
        _ = [n + VALUE_TO_ADD for n in array]
        count += 1

    return count


def task_01():
    """
    Solution for the task #1.

    - Arrays sum for sizes of 100000, 200000, 300000 elements;
    - absolute and relative time measurement.
    """
    print("Absolute measurement: ")

    duration_1 = measure_abs_array_addition(SMALL)
    duration_2 = measure_abs_array_addition(MEDIUM)
    duration_3 = measure_abs_array_addition(LARGE)

    print("{} sized array: {} sec".format(SMALL, duration_1))
    print("{} sized array: {} sec".format(MEDIUM, duration_2))
    print("{} sized array: {} sec".format(LARGE, duration_3))

    #  T(200000)/T (100000), T(300000)/T (100000)
    print("{} to {}: {}".format(MEDIUM, SMALL, duration_2 / duration_1))
    print("{} to {}: {}".format(LARGE, SMALL, duration_3 / duration_1))

    print("\nRelative measurement: ")

    times_1 = measure_rel_array_addition(SMALL)
    times_2 = measure_rel_array_addition(MEDIUM)
    times_3 = measure_rel_array_addition(LARGE)

    print("{} sized array: executed {} times".format(SMALL, times_1))
    print("{} sized array: executed {} times".format(MEDIUM, times_2))
    print("{} sized array: executed {} times".format(LARGE, times_3))

    print("{} to {}: {}".format(SMALL, MEDIUM, times_1 / times_2))
    print("{} to {}: {}".format(SMALL, LARGE, times_1 / times_3))
