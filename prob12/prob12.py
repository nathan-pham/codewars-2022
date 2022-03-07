import math
import os

__dirname = os.path.dirname(__file__)

def parse_line(line):
    return [int(n) for n in line.split(' ')]

with open(os.path.join(__dirname, "./input.txt")) as file:
    to_build, inventory = file.read().strip().split('\n')[1:]
    to_build = parse_line(to_build)
    inventory = parse_line(inventory)

    mult = math.ceil(max([inventory[i] / to_build[i] for i in range(len(to_build))]))

    print(" ".join([str(to_build[i] * mult - inventory[i]) for i in range(len(to_build))]))