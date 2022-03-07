import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    lines = file.read().strip().split('\n')
    person_scores = []

    for line in lines:
        line = line.split(' ')
        person = line[-1]
        scores = line[:-1]
        total_score = 0
        for i in range(0, len(scores), 2):
            a = int(scores[i])
            b = int(scores[i + 1])

            total_score += max(a - b, 0)

        person_scores.append((person, total_score))

    person_scores.sort(key=lambda x: x[1], reverse=True)

    for (person, score) in person_scores:
        print(f"{person} {score}")
