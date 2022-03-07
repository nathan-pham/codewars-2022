import os

__dirname = os.path.dirname(__file__)

with open(os.path.join(__dirname, "./input.txt")) as file:
    size, *coords = file.read().strip().split('\n')[:-1]

    x_size, y_size = [int(n) for n in size.split(' ')]

    grid = [['#' for _ in range(x_size)] for _ in range(y_size)]
    
    for coord in coords:
        y, *xs = [n.replace(':', '') for n in coord.strip().split(' ')]
        for x in xs:
            if '-' in x:
                x_start, x_end = [int(n) for n in x.split('-')]
                
                for i in range(x_start, x_end + 1):
                    grid[int(y)][i] = ' '
            else:
                grid[int(y)][int(x)] = ' '

    for row in grid:
        print("".join(row))