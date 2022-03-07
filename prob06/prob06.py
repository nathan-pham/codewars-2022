import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    P, r, t = [float(n) for n in file.read().strip().split('\n')]

    I = P * r * t

    print(f"{I:.2f}")