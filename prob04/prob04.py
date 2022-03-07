import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    numbers = file.read().strip().split('\n')[:-1]

    for n in numbers:
        print(int(n, 3))