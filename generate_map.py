from conway import DEAD_CELL, LIVE_CELL, MAP_FILE
import random


# MAP_FILE = 'random.txt'

def generate_blank_square_map(filename, size):
    with open(filename, 'w') as file:
        for i in range(size):
            file.write(DEAD_CELL * size + '\n')

def generate_random_map(filename, size):
    with open(filename, 'w') as file:
        for i in range(size):
            line = ''
            for j in range(size):
                line += LIVE_CELL if random.randint(0, 1) == 1 else DEAD_CELL
            file.write(line + '\n')

def main():
    generate_random_map(MAP_FILE,42)

if __name__ == '__main__':
    main()