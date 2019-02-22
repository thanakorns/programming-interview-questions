def isValid(board, i, j):
    numberSet = set()
    for index in range(9):
        if board[i][index] != ".":
            if board[i][index] in numberSet:
                return False
            numberSet.add(board[i][index])

    numberSet = set()
    for index in range(9):
        if board[index][j] != ".":
            if board[index][j] in numberSet:
                return False
            numberSet.add(board[index][j])

    numberSet = set()
    tl_row = i - (i % 3)
    tl_col = j - (j % 3)
    for r in range(tl_row, tl_row + 3):
        for c in range(tl_col, tl_col + 3):
            if board[r][c] != ".":
                if board[r][c] in numberSet:
                    return False
                numberSet.add(board[r][c])
    return True


def isComplete(board):
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                return False
    return True


def sudoku_solve(board):
    if isComplete(board):
        return True
    for i in range(9):
        for j in range(9):
            if board[i][j] == ".":
                for number in range(1):
                    board[i][j] = str(number)
                    if isValid(board, i, j):
                        if sudoku_solve(board):
                            return True
                board[i][j] = "."
    return False


def find_first_empty(board):
    for i, row in enumerate(board):
        for j, val in enumerate(row):
            if val == '.':
                return i, j
    return False


print(sudoku_solve([[".", ".", ".", "7", ".", ".", "3", ".", "1"], ["3", ".", ".", "9", ".", ".", ".", ".", "."],
                    [".", "4", ".", "3", "1", ".", "2", ".", "."], [".", "6", ".", "4", ".", ".", "5", ".", "."],
                    [".", ".", ".", ".", ".", ".", ".", ".", "."], [".", ".", "1", ".", ".", "8", ".", "4", "."],
                    [".", ".", "6", ".", "2", "1", ".", "5", "."], [".", ".", ".", ".", ".", "9", ".", ".", "8"],
                    ["8", ".", "5", ".", ".", "4", ".", ".", "."]]))

'''
1.) given the board, loop through each row and column, try put a number there 1....9 if that row i and col j is .
2.) check isValid(board) with modified number 
3.) if isValid return false, we take the number out and replace it with a .
4.) if isValid return true, then we continue by calling sudoku_solve(board)
4.) if the board is filled out, we return true 

isValid
  At every row, there is exactly one occurence of 1-9
  At every col, there is exactly one occurence of 1-9
  at every box, there is exactly one ......1-9

'''