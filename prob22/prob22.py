import os

__dirname = os.path.dirname(__file__)

SI_UNITS = [
    "",
    "deca",
    "hecto",
    "kilo",
    "mega",
    "giga",
    "tera",
    "peta",
    "exa",
    "zetta",
    "yotta",
    "bronto",
    "gego"
]

NUMBER_TO_WORD = { 0: "zero", 1: "one", 2: "two", 3: "three", 4: "four", 5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine", 10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen", 14: "fourteen", 15: "fifteen", 16: "sixteen", 17: "seventeen", 18: "eighteen", 19: "nineteen", 20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety" }

with open(os.path.join(__dirname, "./input.txt")) as file:
    number = file.read().strip() # 6000009004

    SI_UNITS = [u + "bytes" for u in SI_UNITS]
    expanded = []

    # convert number into expanded form with SI_UNITS

    separated = [number[i:i+3] for i in range(0, len(number), 3)]
    words = []
    for digit in separated:
        word = [NUMBER_TO_WORD.get(int(char), 'zero') for char in list(digit)]

        for i in range(len(word)):
            if word[i] != "zero":
                if i == 0:
                    word[i] = word[i] + " hundred"
                elif i == 1:
                    word[i] = word[i] + "ty"

        # filter out zeros
        word = ''.join([w for w in word if w != "zero"])
        if len(word):
            words.append(word)


    # six gigabytes, nine kilobytes and four bytes
    # e.g. 6000009004 -> six gigabytes, nine kilobytes and four bytes

    # words = list(reversed(words))
    for i in range(len(words)):
        expanded.append(words[i] + " " + SI_UNITS[i])
    # words = list(reversed(words))
        

    print(expanded)