# Conway's Game of Life in Python

## Project Overview

This repository contains a Python implementation of **Conway's Game of Life**, a cellular automaton devised by mathematician John Conway. The project was developed as a personal challenge to prototype the game in Python within one day, despite limited prior experience with the language. The implementation focuses on simplicity and functionality, showcasing the game's rules and mechanics.

Conway's Game of Life is a zero-player game where the evolution of the grid is determined by its initial state and a set of rules. The game simulates life and death in a grid of cells, making it a fascinating exploration of emergent behavior.

## Structure

The repository is organized as follows:

### 1. **Main Files**
   - **`conway.py`**: Contains the core logic for the game, including functions to update the grid, apply the rules, and run the game loop.
   - **`generate_map.py`**: Provides utilities to generate initial grid states, including blank maps and random configurations.
   - **`map.txt`**: Stores the current state of the grid, which is updated during the game.
   - **`smile.txt`**: An example grid configuration resembling a smiley face.

### 2. **Supporting Files**
   - **`.gitignore`**: Specifies files and directories to be ignored by Git.
   - **`README.md`**: Documentation for the project.

## Game Rules

The implementation adheres to the classic rules of Conway's Game of Life:
1. Any live cell with fewer than two live neighbors dies (underpopulation).
2. Any live cell with two or three live neighbors survives.
3. Any live cell with more than three live neighbors dies (overpopulation).
4. Any dead cell with exactly three live neighbors becomes a live cell (reproduction).

## Competencies Developed

Working on this project helps develop the following skills:

- **Python Programming**: Writing Python scripts, managing files, and implementing algorithms.
- **Algorithm Design**: Translating Conway's rules into efficient code for grid updates.
- **File Manipulation**: Reading and writing grid states to files for persistence.
- **Problem-Solving**: Debugging and optimizing code to ensure correct behavior.
- **Creativity**: Designing initial grid configurations and experimenting with emergent patterns.

## How to Use This Repository

1. Clone the repository to your local machine:
   ```bash
   git clone <repository-url>
   ```
2. Run the game using the `conway.py` script:
   ```bash
   python3 conway.py
   ```
3. To generate a new grid, use the `generate_map.py` script:
   ```bash
   python3 generate_map.py
   ```

## Notes

- The game runs in the terminal and updates the grid in real-time.
- You can modify `map.txt` or use `generate_map.py` to create custom grid configurations.

## Conclusion

This project is a fun and educational exploration of Conway's Game of Life, showcasing the power of Python for prototyping and simulation. Whether you're new to Python or interested in cellular automata, this repository provides a great starting point for experimentation.

Enjoy exploring the patterns and behaviors of life!