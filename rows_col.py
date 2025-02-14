
puzzle = [
    [3, 5, 0, 6, 2, 7, 0, 0, 0],
    [0, 6, 9, 8, 0, 3, 2, 0, 7],
    [0, 0, 0, 5, 0, 4, 0, 1, 0],
    [7, 3, 0, 9, 0, 0, 5, 6, 1],
    [8, 0, 0, 0, 0, 0, 4, 0, 0],
    [6, 0, 0, 0, 0, 1, 3, 0, 0],
    [0, 2, 0, 3, 0, 9, 0, 4, 5],
    [0, 0, 0, 0, 7, 5, 8, 0, 0],
    [5, 7, 3, 2, 0, 0, 0, 0, 6]
]

def sudoku_solver(board):
    
    empty_spot = find_empty_cell(board)

    if not empty_spot:
        return True 
    else:
        row, col = empty_spot

    for num in range(1, 10):
        if is_valid_move(board, num, (row, col)):
            board[row][col] = num 

            if sudoku_solver(board):
                return True  

            board[row][col] = 0  

    return False  

def is_valid_move(board, num, pos):
    
    row, col = pos

    
    if num in board[row]:
        return False

    
    if num in [board[i][col] for i in range(9)]:
        return False

   
    box_x, box_y = (col // 3) * 3, (row // 3) * 3
    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num:
                return False

    return True 

def print_sudoku(board):
    
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - -")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            print(board[i][j] if board[i][j] != 0 else ".", end=" ")

        print()

def find_empty_cell(board):
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) 
    return None 


print("Initial Sudoku Board:")
print_sudoku(puzzle)


if sudoku_solver(puzzle):
    print("\nSolved Sudoku:")
    print_sudoku(puzzle)
else:
    print("\nThis Sudoku puzzle is unsolvable!")
