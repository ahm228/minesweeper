import random
import time

def initializeBoard(size, numMines):
    #Create an empty board
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = set()

    #Randomly place mines on the board.
    while len(mines) < numMines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)

        if (row, col) not in mines:
            mines.add((row, col))

    return board, mines

#This function prints the game board to console. If reveal is True, it shows the mines.
def printBoard(board, mines, reveal=False):
    size = len(board)

    #Print column headers
    print("   ", end='')
    for colNum in range(size):
        print(f"{colNum} ", end='')
    print("\n" + "  " + "-" * (size * 2))

    #Print each row of the board
    for row in range(size):
        print(f"{row}|", end=' ')

        for col in range(size):
            cell = board[row][col]
            
            #If the cell is a mine and we are in reveal mode
            if (row, col) in mines and reveal:
                print('M', end=' ')
            #If the cell is flagged
            elif cell == 'F':
                print('F', end=' ')
            #If the cell is unrevealed
            elif cell == ' ':
                print('.', end=' ')
            #Otherwise, display the cell's value (e.g., a number)
            else:
                print(cell, end=' ')

        print()

def startTimer():
    return time.time()

def stopTimer(startTime):
    endTime = time.time()
    elapsed = round(endTime - startTime, 2)
    print(f"\nTime taken: {elapsed} seconds")

#This function counts the number of mines adjacent to a given cell.
def countMines(mines, row, col):
    count = 0

    for i in range(-1, 2):
        for j in range(-1, 2):
            r, c = row + i, col + j
            if (r, c) in mines:
                count += 1

    return count

#This function reveals a cell and its surrounding cells recursively if no adjacent mines.
def revealCells(board, mines, row, col):
    if board[row][col] != ' ':
        return
    
    mineCount = countMines(mines, row, col)

    if mineCount == 0:
        board[row][col] = '0'  #Mark the cell as a '0' cell

        for i in range(-1, 2):
            for j in range(-1, 2):
                r, c = row + i, col + j
                if 0 <= r < len(board) and 0 <= c < len(board[0]) and board[r][c] == ' ':
                    revealCells(board, mines, r, c)

    else:
        board[row][col] = str(mineCount)

#Check if the player has won by revealing all non-mine cells
def hasWon(board, mines):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row, col) not in mines and board[row][col] == ' ':
                return False
            
    return True

def aiMove(board, mines):
    size = len(board)

    #Check for deterministic moves first
    for row in range(size):
        for col in range(size):
            if board[row][col].isdigit():
                adjUnrevealed = 0
                adjFlags = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        r, c = row + i, col +i
                        if 0 <= r < size and 0 <= c < size:
                            if board[r][c] == ' ':
                                adjUnrevealed += 1
                                targetR, targetC = r, c
                            elif board[r][c] == 'F':
                                adjFlags +=1
                #If the mine count is equal to adjacent flags + unrevealed cells, flag the unrevealed cells
                if adjUnrevealed == int(board[row][col]) - adjFlags and adjUnrevealed == 1:
                    return targetR, targetC
                
                #If the mine count is equal to the adjacent flags, reveal the unrevealed cells
                elif adjFlags == int(board[row][col]) and adjUnrevealed > 0:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            r, c = row + i, col + i
                            if 0 <= r < size and 0 <= c < size and board[r][c] == ' ':
                                return r, c
                            
    #If no deterministic move is found, revert to basic probabilistic approach
    probabilities = [[1 for _ in range(size)] for _ in range(size)]
    for row in range(size):
        for col in range(size):
            if board[row][col] == ' ':
                probabilities[row][col] = countMines(mines, row, col) / 8

    minProb = min(min(row) for row in probabilities)
    for row in range(size):
        for col in range(size):
            if probabilities[row][col] == minProb:
                return row, col

def getValidInt(prompt, minValue=None, maxValue=None):
    while True:
        try:
            value = int(input(prompt))
            if (minValue is not None and value < minValue) or (maxValue is not None and value > maxValue):
                raise ValueError
            return value
        
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
            if minValue is not None and maxValue is not None:
                print(f"The value should be between {minValue} and {maxValue}.")


def main():
    #Start the timer as soon as the game begins
    startTime = startTimer()

    #Get a valid size using the helper function
    size = getValidInt("Enter board size: ", 1)

    maxMines = (size * size) - 1
    numMines = getValidInt(f"Enter number of mines (maximum {maxMines}): ", 1, maxMines)
    
    board, mines = initializeBoard(size, numMines)
    
    #Create the list of numbers outside the while loop
    alreadyRevealed = ['F'] + [str(x) for x in range(1, 9)]
    
    mode = input("Choose mode (manual/ai): ").strip().lower()
    while mode not in ['manual', 'ai']:
        print("Invalid mode. Please choose either 'manual' or 'ai'.")
        mode = input("Choose mode (manual/ai): ").strip().lower()
    
    while True:
        printBoard(board, mines)
        
        if mode == 'ai':
            row, col = aiMove(board, mines)
            action = 'reveal'

        else:
            action = input("Choose action (reveal/flag): ").strip().lower()
            while action not in ['reveal', 'flag']:
                print("Invalid action. Please choose either 'reveal' or 'flag'.")
                action = input("Choose action (reveal/flag): ").strip().lower()
            
            #Get and validate the player's cell choice
            row = getValidInt("Enter row: ", 0, size-1)
            col = getValidInt("Enter column: ", 0, size-1)
            
            while board[row][col] in alreadyRevealed:
                print("Invalid input. This cell is already revealed or flagged.")
                row = getValidInt("Enter row: ", 0, size-1)
                col = getValidInt("Enter column: ", 0, size-1)
        
        if action == 'flag':
            if board[row][col] == ' ':
                board[row][col] = 'F'
            elif board[row][col] == 'F':
                board[row][col] = ' '
            continue
        
        if (row, col) in mines:
            print("You hit a mine! Game over.")
            printBoard(board, mines, reveal=True)
            stopTimer(startTime)  #Stop the timer and print elapsed time
            break
        
        else:
            revealCells(board, mines, row, col)
            
            if hasWon(board, mines):
                print("Congratulations! You've revealed all safe cells.")
                printBoard(board, mines, reveal=True)
                stopTimer(startTime)  #Stop the timer and print elapsed time
                break

if __name__ == '__main__':
    main()