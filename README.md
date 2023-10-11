This program allows you to play the classic Minesweeper game. You can play manually, revealing or flagging cells on your own, or you can let an AI make moves for you.

## Features

1. **Variable Board Size:** User-defined board size.
2. **Two Modes:** Manual and AI. Play yourself or watch an AI.
3. **Reveal & Flag Mechanism:** Either reveal a cell or flag a suspected mine.
4. **AI Logic:** The AI calculates the safest cell based on mine probabilities.

## Functions

- `initializeBoard(size, numMines)`: Sets up the game board with mines placed randomly.
- `printBoard(board, mines, reveal=False)`: Displays the current game state. Mines are shown if the reveal argument is `True`.
- `countMines(mines, row, col)`: Counts the number of mines adjacent to a cell.
- `revealCells(board, mines, row, col)`: Reveals a cell and its surroundings if no mines are adjacent.
- `hasWon(board, mines)`: Checks if the player has won by revealing all non-mine cells.
- `ai_move(board, mines)`: The AI logic for choosing the next cell to reveal.
- `main()`: Main game loop.

## How to Play

1. Run the program.
2. Choose the size of the board and the number of mines.
3. Choose the game mode (manual or AI).
4. If in manual mode:
   - Choose to either `reveal` or `flag` a cell.
   - Enter the row and column of the cell you want to reveal or flag.
5. If in AI mode, simply watch the AI make its moves.
6. The game ends when all safe cells are revealed or when a mine is hit.

Note

The AI uses a simple probability-based algorithm to make its decisions. The AI calculates the probability of each unrevealed cell containing a mine, based on the number of adjacent mines, and chooses the cell with the lowest probability.