import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    has_app, yes, *lines =file.read().strip().split('\n')[:-1]

    for line in lines:
        if has_app in line:
            print(line)
        else:
            pass