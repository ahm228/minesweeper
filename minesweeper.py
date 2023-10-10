import random

def initializeBoard(size, numMines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = set()

    while len(mines) < numMines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

        if (row, col) not in mines:
            mines.add((row, col))

    return board, mines

def printBoard(board, mines, reveal=False):
    size = len(board)

    # Print column headers
    print("   ", end='')

    for colNum in range(size):
        print(f"{colNum} ", end='')

    print("\n" + "  " + "-" * (size * 2))

    for row in range(size):
        print(f"{row}|", end=' ')

        for col in range(size):
            cell = board[row][col]
            
            # If the cell is a mine and we are in reveal mode
            if (row, col) in mines and reveal:
                print('M', end=' ')
            # If the cell is flagged
            elif cell == 'F':
                print('F', end=' ')
            # If the cell is unrevealed
            elif cell == ' ':
                print('.', end=' ')
            # Otherwise, display the cell's value (e.g., a number)
            else:
                print(cell, end=' ')

        print()

def countMines(mines, row, col):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            r, c = row + i, col + j
            if (r, c) in mines:
                count += 1

    return count

def revealCells(board, mines, row, col):
    if board[row][col] != ' ':
        return
    
    mineCount = countMines(mines, row, col)

    if mineCount == 0:
        board[row][col] = '0'  # Mark the cell as a '0' cell

        for i in range(-1, 2):
            for j in range(-1, 2):
                r, c = row + i, col + j
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == ' ':
                    revealCells(board, mines, r, c)

    else:
        board[row][col] = str(mineCount)


def hasWon(board, mines):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row, col) not in mines and board[row][col] == ' ':
                return False
            
    return True

def main():
    size = int(input("Enter board size: "))
    numMines = int(input("Enter number of mines: "))
    board, mines = initializeBoard(size, numMines)
    # Create the list of numbers outside the while loop
    alreadyRevealed = ['F'] + [str(x) for x in range(1, 9)]
    
    while True:
        printBoard(board, mines)
        action = input("Choose action (reveal/flag): ").strip().lower()

        while action not in ['reveal', 'flag']:
            print("Invalid action. Please choose either 'reveal' or 'flag'.")
            action = input("Choose action (reveal/flag): ").strip().lower()

        row, col = map(int, input("Enter row and column separated by space (e.g., 3 4): ").split())
        
        while row < 0 or row >= size or col < 0 or col >= size or board[row][col] in alreadyRevealed:
            print("Invalid input. Please enter a valid row and column.")
            row, col = map(int, input("Enter row and column separated by space (e.g., 3 4): ").split())

        if action == 'flag':
            if board[row][col] == ' ':
                board[row][col] = 'F'
            elif board[row][col] == 'F':
                board[row][col] = ' '
            continue
        
        if (row, col) in mines:
            print("You hit a mine! Game over.")
            printBoard(board, mines, reveal=True)
            break

        else:
            revealCells(board, mines, row, col)
            
            if hasWon(board, mines):
                print("Congratulations! You've revealed all safe cells.")
                printBoard(board, mines, reveal=True)
                break

if __name__ == '__main__':
    main()