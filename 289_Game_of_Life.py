'''

According to the Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

Given a board with m by n cells, each cell has an initial state live (1) or dead (0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies, as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population..
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
Write a function to compute the next state (after one update) of the board given its current state. The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously.

Example:

Input:
[
  [0,1,0],
  [0,0,1],
  [1,1,1],
  [0,0,0]
]
Output:
[
  [0,0,0],
  [1,0,1],
  [0,1,1],
  [0,1,0]
]
Follow up:

Could you solve it in-place? Remember that the board needs to be updated at the same time: You cannot update some cells first and then use their updated values to update other cells.
In this question, we represent the board using a 2D array. In principle, the board is infinite, which would cause problems when the active area encroaches the border of the array. How would you address these problems?

Thoughts:
    This problem is quite complex, so we will need to use multiple functions. Basically, we need a function to store
    the values of each cell after comparison, one function to do the comparison, and another function to update the
    stored values into the 0/1 values. We will have to iterate over the entire matrix once. For each cell,
    we will look at its all neighbors.
'''

directions = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]


# function definition
def gameOfLife(board):  # return None since the change is done in-place.
    # null case
    if not board:
        return

    # mark alive to dead cell as -1, mark dead to alive cell as 2
    # define the directions

    # iterate over the entire matrix
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:  # if the current cell is dead
                if count_nb(board, i, j) == 3:
                    board[i][j] = 2 # dead to alive
            else:  # if the current cell is alive
                if count_nb(board, i, j) > 3 or count_nb(board, i, j) < 2:
                    board[i][j] = -1 # alive to dead

    update(board)


# define the rules for counting neighbors
def count_nb(board, i, j):
    alive = 0
    for d in directions:
        row = i + d[0]
        col = j + d[1]
        if 0 <= row < len(board) and 0 <= col < len(board[0]):  # make sure the cell is inside the board
            if board[row][col] == 1 or board[row][col] == -1:  # if the cell is alive, count plus one
                alive += 1
    return alive


# define the function for updating the stored values into zeroes and ones
def update(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 2:  # if the cell is alive
                board[i][j] = 1
            elif board[i][j] == -1:  # if the cell is dead
                board[i][j] = 0


# main test run
if __name__ == "__main__":
    test_input = [
        [0, 1, 0],
        [0, 0, 1],
        [1, 1, 1],
        [0, 0, 0]
    ]
    gameOfLife(test_input)
    print(test_input)
