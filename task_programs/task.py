"""
Interface for a task.
"""

from abc import ABC, abstractmethod
from typing import Any


class Task(ABC):
    """
    The Task Interface for all tasks to follow.
    """

    small_size = None
    medium_size = None
    large_size = None

    # User-defined class (if applicable)
    custom_data_type = None


    # TODO make it obligatory
    # Could be any built-in, standard or non-standard Python datatype
    chosen_data_type = "SomeDataType"

    @staticmethod
    def unmeasured_logic() -> Any:
        """
        Auxiliary logic which won't be measured e.g. arrays initialization.
        """
        return 0

    @abstractmethod
    def measured_logic(self, *args) -> Any:  # NOQA
        """
        Program logic to run and measure, e.g. arrays addition.
        """
        return 0

    @abstractmethod
    def run(self, *args, **kwargs) -> tuple:  # NOQA
        """
        Run the program and return its measurements as a tuple.

        It is usually a program() wrapped into measurements.

        Tuple contains:
        - result of the program e.g. sum of arrays addition;
        - time taken;
        - space taken;
        - TODO future feature: relative measurement e.g. number of program executions finished in n sec.
        """
        return 0, 0, 0
