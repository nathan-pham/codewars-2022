import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    times = file.read().strip().split('\n')[1:]
    total_time = 0

    for time in times:
        minutes, seconds = [int(n) for n in time.split(':')]
        total_time += minutes * 60 + seconds

    # convert total time to MM:SS
    minutes = total_time // 60
    seconds = total_time % 60

    if minutes > 10:
        print(f"{minutes:02d}:{seconds:02d}")
    else:
        print(f"{minutes}:{seconds:02d}")