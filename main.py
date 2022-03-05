import sys
import os


resolve = lambda *args: os.path.join(*args)
__dirname = os.path.dirname(__file__)


python_template = """
import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    print(file.read())
"""


def main(args) -> None:
    file, number = args 

    problem = f"prob{number.zfill(2)}"

    os.mkdir(resolve(__dirname, problem))

    with open(resolve(__dirname, problem, f"{problem}.py"), "w") as file:
        file.write(python_template.strip())

    with open(resolve(__dirname, problem, "input.txt"), "w") as file:
        file.write("")


if __name__ == "__main__":
    main(sys.argv)