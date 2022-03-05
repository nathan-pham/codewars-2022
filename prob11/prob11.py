import os
import re

__dirname = os.path.dirname(__file__)

vowels = "aeiou"
punctuation = "!@#$%^&*()_+=-[]\{}|;':\",./<>?"

with open(os.path.join(__dirname, "./input.txt")) as file:
    statements = []
    lines = file.read().strip().split("\n")[:-1]
    
    for line in lines:
        translated = []
        for word in line.split(" "):
            if word[0].lower() not in vowels and len(word) == 2:
                translated.append(word)
            elif word[0].lower() in vowels:
                pass
            else:
                possible_punctuation = word[-1]
                word = word[1:] + word[0] + "-squeak"
                # replace all punctuation regex
                word = re.sub(r"[!@#$%^&*()_+=-[]\{}|;':", "", word)
                word += possible_punctuation if possible_punctuation in punctuation else ""
                translated.append(word)
        statements.append(translated)            

    for statement in statements:
        print(statement)