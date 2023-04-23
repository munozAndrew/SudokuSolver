# SudokuSolver
This is a Python program that solves Sudoku puzzles using backtracking and recursion.
Usage
### Usage
To use the solver, simply run the 'solver' function and pass in the Sudoku board as a 2D list, where empty cells are represented as 0. The solver will modify the original boardin place, filling in the correct values for empty cells
### How it Works
The solver uses a recursive backtracking algorithm to fill in the Sudoku board. It starts by finding the first empty cell, and then tries each possible value (1-9) for that cell. if a value is valid (i.e. It doesnt conflict with any other values within the same row, column, or 3x3 sub-grid), the solver recursively tries to fill in the next empty cell. If the solver reaches the end of the baord(i.e. there are no more empty cells), it returns 'True' to indicate that the puzzle has been solved. If at any point the solver reaches a dead end (i.e. It can't find a valid value for an empty cell), it backtracks to the previous cell and tries the next possible value.
