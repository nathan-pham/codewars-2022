import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    text = file.read().strip()

    left = text.count("(")
    right = text.count(")")

    # get the number of pairs of valid parentheses
    stack = []
    valid = 0

    for char in text:
        if char == "(":
            stack.append(char)
        elif char == ")":
            if len(stack) > 0:
                stack.pop()
                valid += 1
            else:
                stack.append(char)

    print(f"Total left: {left}")
    print(f"Total right: {right}")
    print(f"Total pairs: {valid}")
    print("Unbalanced" if len(stack) > 0 else "Balanced")