"""
Interface for a task.
"""

from abc import ABC, abstractmethod
from typing import Any

from task_programs.constants import (
    DEFAULT_MEASUREMENTS_VALUE,
    FILLER_FLOAT,
    FILLER_INT,
)


class TaskConfig(ABC):
    """
    The Task Configuration Interface for all tasks to follow.
    """

    # TODO make the size obligatory
    # Data sizes, e.g. 10000 elements in an array
    small_size = None
    medium_size = None
    large_size = None

    # User-defined class (if applicable)
    custom_data_type = None

    # TODO possible data types
    # TODO make it enum-like, closer to enum (made for validation!)


# TODO do we need inheritance from TaskConfig and why?
class Task(ABC, TaskConfig):
    """
    The Task Interface for all tasks to follow.

    Contains the program's chosen parameters: data type, data size, etc.
    """

    @abstractmethod
    def __init__(self, *args: Any, **kwargs: Any):  # NOQA
        self.data_size = None
        # TODO make fields obligatory
        # Could be any built-in, standard or non-standard Python datatype
        self.data_type = None  # TODO do it better
        self.measurements_number = DEFAULT_MEASUREMENTS_VALUE

    @staticmethod
    def _define_numeric_filler(data_type):
        """
        Infer the filler value to fill the data structure with.
        """
        if isinstance(data_type, int):
            filler = FILLER_INT
        elif isinstance(data_type, float):
            filler = FILLER_FLOAT
        else:
            raise ValueError("Unsupported data type for array addition.")
        return filler

    @abstractmethod
    def unmeasured_logic(self, *args: Any, **kwargs: Any) -> Any:  # NOQA
        """
        Auxiliary logic which won't be measured e.g. arrays initialization.
        """
        return 0

    @abstractmethod
    def measured_logic(self, *args: Any, **kwargs: Any) -> Any:  # NOQA
        """
        Program logic to run and measure, e.g. arrays addition.
        """
        return 0

    def run(self, *args: Any, **kwargs: Any) -> tuple:  # NOQA
        """
        Run the program and return its measurements as a tuple.

        It is usually a combination of other methods (measured logic, unmeasured logic, etc).

        Tuple contains:
        - result of the program e.g. sum of arrays addition;
        - time spent, seconds;
        - TODO future feature: space taken, bytes;
        - TODO future feature: relative measurement e.g. number of program executions finished in n sec.
        """
        param = self.unmeasured_logic(*args, **kwargs)
        result, time_spent = self.measured_logic(param)
        return result, time_spent
