import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    faces = file.read().strip().split(' ')

    dictionary = {}

    for face in faces:
        dictionary[face] = dictionary.get(face, 0) + 1

    min_key = min(dictionary, key=dictionary.get)
    pos = faces.index(min_key) + 1

    print(f"#{pos} {min_key} you are out of control!")
    