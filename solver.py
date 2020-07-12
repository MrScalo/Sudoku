# Checking which number (1-9) fits in the empty place and backtracking it in order to replace it with a higher one if
# needed
def solve(board):
    find = findEmpty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1, 10):
        if valid(board, i, (row, col)):
            board[row][col] = i

            # executing solve() in solve() itself (backtracking)
            if solve(board):
                return True

            board[row][col] = 0

    return False


# Checking if a number is valid in the x and y coordinate and in the 3x3 box
def valid(board, number, position):
    # Checking row
    for i in range(len(board[0])):
        if board[position[0]][i] == number and position[1] != i:
            return False

    # Checking column
    for i in range(len(board)):
        if board[i][position[1]] == number and position[0] != i:
            return False

    # Checking box
    boxX = position[1] // 3
    boxY = position[0] // 3

    for i in range(boxY * 3, boxY * 3 + 3):
        for j in range(boxX * 3, boxX * 3 + 3):
            if board[i][j] == number and (i, j) != position:
                return False

    return True


# Finding the next empty place in the board
def findEmpty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0 or board[i][j] == "#":
                return i, j  # row, col

    return None


# Printing the board in the console
def printBoard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("+ + + + + + + + + + + +")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" + ", end="")

            if board[i][j] == 0:
                board[i][j] = "#"

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")