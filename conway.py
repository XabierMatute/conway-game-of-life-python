import shutil
import sys

MAP_FILE = "map.txt"

def print_map():
    with open(MAP_FILE, 'r') as file:
            shutil.copyfileobj(file, sys.stdout)

def conway():
    print("Hello, World! I'm using Python!")
    print_map()

def main():
    conway()

if __name__ == "__main__":
    main()