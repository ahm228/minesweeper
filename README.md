A simple command-line implementation of the classic Minesweeper game. In this game, you need to reveal cells without hitting a mine. You can also flag cells that you believe contain mines.
Features

    Interactive grid with row and column numbers for easy cell selection.
    Option to either reveal a cell or flag it.
    Automatically reveals cells with no adjacent mines and provides count of adjacent mines when a cell is revealed.
    Win condition check, to determine if all safe cells have been revealed.

Usage

Run the script to play the game:
python minesweeper.py

Game Flow:

    Input the board size.
    Input the number of mines.
    Choose an action:
        reveal to reveal a cell.
        flag to flag or unflag a cell.
    Enter row and column number separated by a space to select a cell (e.g., 3 4).
    The game continues until either all safe cells are revealed or a mine is hit.

Functions

    initializeBoard(size, numMines): Generates a board of given size with the specified number of mines.
    printBoard(board, mines, reveal=False): Prints the game board. If reveal is set to True, it will show mines.
    countMines(mines, row, col): Counts the number of mines adjacent to a given cell.
    revealCells(board, mines, row, col): Reveals cells recursively if no adjacent mines are present.
    hasWon(board, mines): Checks if all safe cells have been revealed to determine win condition.
    main(): The main game loop where user interactions take place.