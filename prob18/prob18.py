import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    file.read().strip().split('\n')
    print(file.read())

#     12,[13;18],[22-23;47-49],0,-33,[6;23;43;-1]
# There were many happy clouds in the sky today.
# But gray skies are on the way.
# In other news the last days of Christmas sale at Crazy Johns is ending soon,
# right in time for the New Year, so . . .
# run, walk, skip or jump down to the location nearest you.
# If that isn't enough, we'll have April joining us for Action News at 11!
