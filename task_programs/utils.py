"""
Auxiliary functions.
"""
import platform
from typing import Optional


# TODO consider introducing the Adapter class (for the sake of dependency inversion)


def get_processor_type() -> Optional[str]:
    """
    Define and return the processor type e.g. 'amdk6'.

    Fairly portable.
    """
    return platform.processor()


def get_machine_type() -> Optional[str]:
    """
    Define and return the machine type e.g. 'i386'.

    Fairly portable.
    """
    return platform.machine()


def get_system_type() -> Optional[str]:
    """
    Define and return the OS type e.g. 'Linux', 'Windows' or 'Java'.

    Fairly portable.
    """
    return platform.system()
