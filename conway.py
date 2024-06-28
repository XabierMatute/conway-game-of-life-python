import shutil
import sys
import time
import os

MAP_FILE = "map.txt"

DEAD_CELL = '.'
LIVE_CELL = '0'

# game rules
# 1. Any live cell with fewer than two live neighbours dies, as if by underpopulation.
# 2. Any live cell with two or three live neighbours lives on to the next generation.
NUMBER_OF_NEIGHBOURS_TO_SURVIVE = [2, 3]
# 3. Any live cell with more than three live neighbours dies, as if by overpopulation.
# 4. Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction.
NUMBER_OF_NEIGHBOURS_TO_BORN = [3]

FRECUENCY = 0.042

def print_file(file):
    try :
        with open(file, 'r') as file:
            shutil.copyfileobj(file, sys.stdout)
    except FileNotFoundError:
        print(f"File {file} not found while trying to print it.")
    except Exception as e:
        print(f"An error occurred while trying to print the file {file}.")
        print(e)

def print_map():
    print_file(MAP_FILE)

def print_time():
    print(time.strftime("\n%Y-%m-%d %H:%M:%S", time.localtime()))

def clear_console():
    os.system('clear')

def get_environment(map, i, j):
    env = []
    for x in range(i - 1, i + 2):
        for y in range(j - 1, j + 2):
            if x >= 0 and x < len(map) and y >= 0 and y < len(map[x]):
                if x != i or y != j:
                    env.append(map[x][y])
            else:
                env.append(DEAD_CELL)
    return env

def should_born_cell(envyronment):
    return envyronment.count(LIVE_CELL) in NUMBER_OF_NEIGHBOURS_TO_BORN

def should_born(map, i, j):
    return should_born_cell(get_environment(map, i, j))

def should_survive_cell(envyronment):
    return envyronment.count(LIVE_CELL) in NUMBER_OF_NEIGHBOURS_TO_SURVIVE

def should_survive(map, i, j):
    return should_survive_cell(get_environment(map, i, j))

def conway_step(map):
    new_map = [list(line) for line in map]
    for i in range(len(map)):
        for j in range(len(map[i])):
            if map[i][j] == DEAD_CELL:
                if should_born(map, i, j):
                    new_map[i][j] = LIVE_CELL
            elif map[i][j] == LIVE_CELL:
                if not should_survive(map, i, j):
                    new_map[i][j] = DEAD_CELL
    return new_map

def update_game_state(filename):
    with open(filename, 'r') as file:
        map = [list(line.strip()) for line in file]
    nex_step_map = conway_step(map)
    with open(filename, 'w') as file:
        for line in nex_step_map:
            file.write(''.join(line) + '\n')

def live(filename):
    try:
        update_game_state(filename)

    except FileNotFoundError:
        print(f"File {filename} not found while trying to make it live.")
    except Exception as e:
        print(f"An error occurred while trying make the file {filename} live.")
        print(e)
# HACER UNA FUNCION BOOLEANA QUE RECIBE UN 3*3(9) Y DEVUELVE SI VIVE O MUERE
#

def live_map():
    live(MAP_FILE)

import itertools

def game_loop():
    for loop in itertools.count():
        time.sleep(FRECUENCY)
        clear_console()
        live_map()
        print_map()
        print_time()
        print(f"Loop: {loop}")

def conway():
    try:
        game_loop()

    except KeyboardInterrupt:
        print("Game stopped by user.")
    except Exception as e:
        print("An error occurred while running the game.")
        print(e)

def main():
    # para saber que todo va bien
    print("Hello, World! I'm using Python!")
    print_map()

    conway()



if __name__ == "__main__":
    main()