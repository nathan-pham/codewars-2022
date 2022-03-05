import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    numbers = file.read().strip().split('\n')[:-1]

    even = []
    odd = []

    for n in numbers:
        if int(n) % 2 == 0:
            even.append(n)
        else: 
            odd.append(n)

    if len(even) == 0 or len(odd) == 0:
        print("NO LIST PROBLEMS FOUND")
    elif len(even) > len(odd):
        print(f"{odd[0]} is not even")
    elif len(odd) > len(even):
        print(f"{even[0]} is not odd")
    else:
        print("NO LIST PROBLEMS FOUND")