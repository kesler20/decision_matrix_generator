import math


def percent_error_calculation(original: float, new: float):
    return abs((new - original)*100/original)
