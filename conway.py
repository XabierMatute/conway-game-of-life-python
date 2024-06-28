import shutil
import sys

MAP_FILE = "map.txt"

def print_file(file):
    with open(file, 'r') as file:
        shutil.copyfileobj(file, sys.stdout)

def print_map():
    print_file(MAP_FILE)

def conway():
    print("Hello, World! I'm using Python!")
    print_map()

def main():
    conway()

if __name__ == "__main__":
    main()