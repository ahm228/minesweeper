Description:

This script allows you to play a simple console version of the Minesweeper game. The board's size and number of mines can be set by the user at the start of the game.
Features:

    Customizable board size.
    Customizable number of mines.
    Ability to reveal a cell or flag it.
    Checks for game victory condition.
    Reveals the entire board with mines at the end of the game.

Functions:

    initializeBoard(size, numMines): Initializes a board of a given size with a specified number of mines.
    printBoard(board, mines, reveal=False): Prints the current state of the board. Can reveal all mines if specified.
    countMines(mines, row, col): Counts the number of mines surrounding a given cell.
    revealCells(board, mines, row, col): Recursively reveals cells starting from a given cell.
    hasWon(board, mines): Checks if the user has won the game.
    main(): The main gameplay loop.

How to play:

    Run the script.
    Enter the desired board size and number of mines.
    Choose between the actions: 'reveal' or 'flag'.
    Enter the row and column (separated by space) where you want to perform the action.
    The game continues until you either reveal a mine or reveal all safe cells.

Instructions:

    reveal: Choose this action if you believe the chosen cell is safe and doesn't contain a mine. If the cell contains a mine, the game ends.
    flag: Use this action if you suspect a mine in the chosen cell. You can toggle the flag on and off by choosing this action on a previously flagged cell.
    To win the game, you need to reveal all cells that don't contain mines without revealing a mine.

Tips:

    The game board displays numbers which indicate how many mines are adjacent to that cell.
    Use these numbers to deduce where the mines are located.
    Flagging suspected mines can help in making safer choices during the game.

Dependencies:

    Python's built-in random library.