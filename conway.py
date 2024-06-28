import shutil
import sys
import time
import os

MAP_FILE = "map.txt"

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

def conway_step(mapa):
    new_map = [list(line) for line in mapa]
    for i in range(len(mapa)):
        for j in range(len(mapa[i])):
            count = 0
            for x in range(i-1, i+2):
                for y in range(j-1, j+2):
                    if x >= 0 and x < len(mapa) and y >= 0 and y < len(mapa[i]) and not (x == i and y == j):
                        if mapa[x][y] == '1':
                            count += 1
            if mapa[i][j] == '1':
                if count < 2 or count > 3:
                    new_map[i][j] = '0'
            else:
                if count == 3:
                    new_map[i][j] = '1'
    return new_map

def live(filename):
    try:
        with open(filename, 'r') as file:
            mapa = [list(line.strip()) for line in file]
        new_map = conway_step(mapa)
        with open(filename, 'w') as file:
            for line in new_map:
                file.write(''.join(line) + '\n')
    except FileNotFoundError:
        print(f"File {filename} not found while trying to make it live.")
    except Exception as e:
        print(f"An error occurred while trying make the file {filename} live.")
        print(e)
# HACER UNA FUNCION BOOLEANA QUE RECIBE UN 9*9 Y DEVUELVE SI VIVE O MUERE
#

def live_map():
    live(MAP_FILE)

def conway():
    print("Hello, World! I'm using Python!")
    print_map()

    while True:
        time.sleep(1)
        clear_console()
        live_map()
        print_map()
        print_time()

def main():
    conway()

if __name__ == "__main__":
    main()