import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    text = file.read().strip()

    left = text.count("(")
    right = text.count(")")

    # find pairs of matching parenthesis
    # (()) will result in 2 pairs
    pairs = []
    for i in range(left):
        for j in range(right):
            if i == j:
                pairs.append((i, j))

    print(f"Total left: {left}")
    print(f"Total right: {right}")
    print(f"Total pairs: {len(pairs)}")

    balanced = len(pairs) == left == right

    print("Balanced" if balanced else "Unbalanced")