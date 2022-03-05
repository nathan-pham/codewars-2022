import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    PTS, FGA, FTA = [float(n) for n in file.read().strip().split(" ")]

    TS = 100 * PTS / (2 * (FGA + (0.44 * FTA)))

    print(f"{TS:.2f}%")