import random

def initialize_board(size, num_mines):
    board = [[' ' for _ in range(size)] for _ in range(size)]
    mines = set()
    while len(mines) < num_mines:
        row = random.randint(0, size - 1)
        col = random.randint(0, size - 1)
        if (row, col) not in mines:
            mines.add((row, col))
            board[row][col] = 'M'
    return board, mines

def print_board(board, mines, reveal=False):
    for row in range(len(board)):
        for col in range(len(board[0])):
            if (row, col) in mines and reveal:
                print('M', end=' ')
            elif board[row][col] == 'F':
                print('F', end=' ')
            elif (row, col) in mines:
                print('.', end=' ')
            else:
                print(board[row][col], end=' ')
        print()

def count_mines(mines, row, col):
    count = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            r, c = row + i, col + j
            if (r, c) in mines:
                count += 1
    return count

def reveal_cells(board, mines, row, col):
    if board[row][col] != ' ':
        return
    mine_count = count_mines(mines, row, col)
    if mine_count == 0:
        board[row][col] = ' '
        for i in range(-1, 2):
            for j in range(-1, 2):
                r, c = row + i, col + j
                if 0 <= r < len(board) and 0 <= c < len(board[0]):
                    reveal_cells(board, mines, r, c)
    else:
        board[row][col] = str(mine_count)

def main():
    size = int(input("Enter board size: "))
    num_mines = int(input("Enter number of mines: "))
    board, mines = initialize_board(size, num_mines)
    while True:
        print_board(board, mines)
        action = input("Choose action (reveal/flag): ").strip().lower()
        row, col = map(int, input("Enter row and column separated by space (e.g., 3 4): ").split())
        if action == 'flag':
            if board[row][col] == ' ':
                board[row][col] = 'F'
            elif board[row][col] == 'F':
                board[row][col] = ' '
            continue
        if (row, col) in mines:
            print("You hit a mine! Game over.")
            print_board(board, mines, reveal=True)
            break
        else:
            reveal_cells(board, mines, row, col)
            if all(cell == 'M' or cell != ' ' for row in board for cell in row):
                print("Congratulations! You've revealed all safe cells.")
                print_board(board, mines, reveal=True)
                break

if __name__ == '__main__':
    main()
