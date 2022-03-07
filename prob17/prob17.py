import os
from functools import reduce

__dirname = os.path.dirname(__file__)

import math

def round_decimals_up(number:float, decimals:int=2):
    """
    Returns a value rounded up to a specific number of decimal places.
    """
    if not isinstance(decimals, int):
        raise TypeError("decimal places must be an integer")
    elif decimals < 0:
        raise ValueError("decimal places has to be 0 or more")
    elif decimals == 0:
        return math.ceil(number)

    factor = 10 ** decimals
    return math.ceil(number * factor) / factor


def parse_input(line):
    var, *rest = line.split(' ')

    return [int(x) for x in rest]

with open(os.path.join(__dirname, "./input.txt")) as file:
    W, L, D, R, P = [parse_input(line) for line in file.read().strip().split('\n')]

    size = [W, L, D]
    size = [sum([x[0] * 12, x[1]]) for x in size]

    total_value = reduce(lambda x, y : x * y, size) / 46656.0

    cubic_yards_R = round_decimals_up(total_value * 0.80, 3)
    cubic_yards_P = round_decimals_up(total_value * 0.20, 3)

    print(f"R {cubic_yards_R:.3f} cu yd")
    print(f"P {cubic_yards_P:.3f} cu yd")

    result = round_decimals_up(cubic_yards_R * R[0] + cubic_yards_P * P[0], 2)
    print(f"T {result:.2f} dollars")

#     R 101.115 cu yd
# P 25.279 cu yd
# T 126.40 dollars
