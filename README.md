# Sudoku-Solver
Overview

This is a simple Sudoku solver implemented in Python using a backtracking algorithm. The program takes an incomplete 9x9 Sudoku board as input and finds a valid solution by recursively filling in empty cells.

Features

Uses backtracking to efficiently solve Sudoku puzzles.

Prints the Sudoku board before and after solving.

Displays a neatly formatted board with separators for better readability.

Returns a message if the puzzle is unsolvable.

How It Works

The program searches for an empty cell (represented as 0).

It tries placing numbers 1-9 in that cell, checking if the move is valid.

If a number is valid, it proceeds to the next empty cell.

If it reaches a dead-end, it backtracks to the previous step and tries a different number.

The process continues until the entire board is filled correctly.

Code Structure

sudoku_solver(board): Recursively solves the Sudoku board using backtracking.

is_valid_move(board, num, pos): Checks if a number can be placed at a given position.

find_empty_cell(board): Finds the next empty cell.

print_sudoku(board): Displays the Sudoku board in a readable format.


                                          Initial Sudoku Board:
                                          
                                            3 5 .  | 6 2 7  | . . . 
                                            . 6 9  | 8 . 3  | 2 . 7 
                                            . . .  | 5 . 4  | . 1 . 
                                            - - - - - - - - - - - - -
                                            7 3 .  | 9 . .  | 5 6 1 
                                            8 . .  | . . .  | 4 . . 
                                            6 . .  | . . 1  | 3 . . 
                                            - - - - - - - - - - - - -
                                            . 2 .  | 3 . 9  | . 4 5 
                                            . . .  | . 7 5  | 8 . . 
                                            5 7 3  | 2 . .  | . . 6 

                                            Solved Sudoku:

                                            3 5 1  | 6 2 7  | 9 8 4 
                                            4 6 9  | 8 1 3  | 2 5 7 
                                            2 8 7  | 5 9 4  | 6 1 3 
                                            - - - - - - - - - - - - -
                                            7 3 4  | 9 8 2  | 5 6 1
                                            8 1 5  | 7 3 6  | 4 2 9
                                            6 9 2  | 4 5 1  | 3 7 8
                                            - - - - - - - - - - - - -
                                            1 2 8  | 3 6 9  | 7 4 5
                                            9 4 6  | 1 7 5  | 8 3 2
                                            5 7 3  | 2 4 8  | 1 9 6
