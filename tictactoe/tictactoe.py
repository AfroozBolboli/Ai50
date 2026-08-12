"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):

    """
    Returns player who has the next turn on a board.
    """

    # Count the empty cells in the board
    empty_count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                empty_count += 1

    # If empty cells are odd then it is X's turn, otherwise it is O's turn
    if empty_count == 0:
        raise Exception("No empty slots.")
    elif empty_count % 2 == 0:
        return O
    elif empty_count % 2 == 1: 
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i is row j is column range 0, 1, and 2
    """
    # Basically return the coordinates of empties
    raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    One can win the game with three of their moves in 
    a row horizontally, vertically, or diagonally.
    """
    #there will be at most one winner 
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """

    print("I am in terminal function")
    if not EMPTY in board:
        return True
    else:
        return False



def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """

    # assume utility will only be called on a board if terminal(board) is True
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    """
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the minimax function should return None.
    """
    raise NotImplementedError
