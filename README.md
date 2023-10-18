Description

This is a console-based Minesweeper game that can be played both manually by a player and automatically by an AI. Minesweeper is a classic game where players need to reveal cells without hitting a mine. The numbers in the revealed cells indicate the number of adjacent mines.
Features

    Variable Board Size and Mine Count: The player can specify the board size and number of mines at the start of the game.
    Two Modes of Play: Play manually or let the AI make decisions.
    Timer: The game times the player's (or AI's) performance from start to finish.
    AI Strategy: The AI first looks for deterministic moves based on revealed numbers, and if none are found, it uses a probabilistic approach.

How to Play

    Run the script.
    Enter the desired board size.
    Specify the number of mines (maximum is board size squared minus one).
    Choose a mode:
        manual: You decide where to reveal or flag cells.
        ai: Watch the AI make moves.
    If playing manually, on each turn:
        Choose an action: reveal or flag.
        Enter the row and column of the cell you want to interact with.
    The game ends when all non-mine cells are revealed or when a mine is hit.

Functions

    initializeBoard(size, numMines): Returns a board of given size with a specified number of mines.
    printBoard(board, mines, reveal=False): Displays the game board. Mines can optionally be revealed.
    startTimer(): Starts a timer.
    stopTimer(startTime): Stops the timer and prints elapsed time.
    countMines(mines, row, col): Counts the number of mines adjacent to a given cell.
    revealCells(board, mines, row, col): Reveals a cell and its neighbors recursively if they don't have adjacent mines.
    hasWon(board, mines): Checks if the player has won by revealing all non-mine cells.
    aiMove(board, mines): AI determines its next move based on the current state of the board.
    getValidInt(prompt, minValue=None, maxValue=None): Helper function to get a valid integer input from the user.
    main(): Main game loop.

Notes

    The AI uses a basic deterministic strategy combined with a probabilistic fallback for its moves. This means it's not guaranteed to win every game, especially on larger boards with many mines.

To-Do

    Add GUI support for a more visually appealing experience.
    Enhance AI algorithms to improve win rates on larger boards.