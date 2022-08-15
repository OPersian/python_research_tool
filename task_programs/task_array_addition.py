"""
Task on arrays addition.

Add a number to array's elements.

Array sizes: 100000, 200000, 300000.
Comparisons: T(200000)/T (100000), T(300000)/T (100000).

TODO consider as future feature:
 Relative measurement: number of times a program gets executed during the given time, `SECONDS_TO_WAIT`.
"""
import time
from typing import Any
from numbers import Number

from task_programs.task import Task, TaskConfig
from task_programs.constants import (
    DEFAULT_MEASUREMENTS_VALUE,
    FILLER_INT,
    MAX_NUMBER,
)


# Arrays sizes (number of elements in an array)
SMALL = 100000
MEDIUM = 200000
LARGE = 300000

# Value to add to every array element.
VALUE_TO_ADD = 10

SMALL_MEASUREMENTS_NUMBER = 10
MEDIUM_MEASUREMENTS_NUMBER = 100
LARGE_MEASUREMENTS_NUMBER = 500

# Value used for relative measurement
SECONDS_TO_WAIT = 2


class ArrayAdditionTaskConfig(TaskConfig):
    """
    The Array Addition Task Configuration logic.
    """

    small_size = SMALL
    medium_size = MEDIUM
    large_size = LARGE

    small_measurements_number = SMALL_MEASUREMENTS_NUMBER
    medium_measurements_number = MEDIUM_MEASUREMENTS_NUMBER
    large_measurements_number = LARGE_MEASUREMENTS_NUMBER


class ArrayAdditionTask(Task):
    """
    The Array Addition Task logic.
    """

    # TODO incorporate measurements value into the client code
    def __init__(
        self,
        data_size: int,
        data_type: Number,
        measurements_number: int = DEFAULT_MEASUREMENTS_VALUE,
    ):
        """
        Initialize the task with given parameters.
        """
        self.data_size = data_size  # number of elements in an array
        self.data_type = data_type
        self.measurements_number = measurements_number
        self.filler = self._define_numeric_filler(data_type)  # a value to fill the data structure with

    def unmeasured_logic(self, *args: Any, **kwargs: Any) -> tuple:  # NOQA
        """
        Auxiliary logic which won't be measured.

        i.e. array initialization.
        """
        array = (self.filler,) * self.data_size
        return array

    def measured_logic(self, array: tuple) -> tuple:
        """
        Provide the result and absolute measurement of array addition execution time.

        Return:
            tuple of addition result (tuple) and duration of program execution, seconds (float).
        """
        min_duration = MAX_NUMBER
        result = None

        for _ in range(self.measurements_number):

            # After array init
            start = time.time()

            intermediary_result = (n + VALUE_TO_ADD for n in array)

            end = time.time()

            cur_duration = end - start

            if cur_duration < min_duration:
                min_duration = cur_duration
                result = intermediary_result

        return result, min_duration


def measure_rel_array_addition(elements_number: int, filler: Number = FILLER_INT) -> int:
    """
    Provide relative measurement of array addition execution time.

    TODO: incorporate this logic into relative measurement for task_programs.task.Task.run()

    Arguments:
        elements_number (int): number of elements in an array.
        filler (Numeric): a value to fill the data structure with.

    Return:
        number of times a program gets executed during the given time, `SECONDS_TO_WAIT` (int)
    """
    array = [filler] * elements_number

    count = 0
    tick_initial = time.time()

    while time.time() - tick_initial < SECONDS_TO_WAIT:
        _ = [n + VALUE_TO_ADD for n in array]  # NOQA
        count += 1

    return count
