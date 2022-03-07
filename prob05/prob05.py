import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    number_str = file.read().strip()
    number_float = float(number_str)
    last_number = int(number_str[-1])
    

    if last_number == 7:
        number_float += 0.02

    elif last_number % 2 != 0:
        number_float -= 0.09

    elif last_number > 7:
        number_float -= 4

    elif last_number < 4:
        number_float += 6.78

    print(f"{number_float:.2f}")