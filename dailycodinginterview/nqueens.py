def n_queens(n, board=[]):
    if n == len(board):
        return 1
    count = 0
    for i in range(n):
        board.append(i)
        if isValid(board):
            count += n_queens(n, board)
        board.pop()
    return count

def isValid(board):
    latest_col = board[-1]
    latest_row = len(board)-1
    for i in range(len(board)-1):
        diff = abs(latest_col - board[i])
        rowDiff = abs(latest_row - i)
        if diff == 0 or diff == rowDiff:
            return False
    return True

for i in range(10):
    print(n_queens(i))
