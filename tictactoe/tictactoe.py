"""
Tic Tac Toe Player
"""

import math
import copy 

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

    # Count the empty cells in the board.
    # count = sum([row.count(EMPTY) for row in board]) more experienced version

    empty_count = 0
    for row in board:
        for cell in row:
            if cell == EMPTY:
                empty_count += 1

    # If empty cells counts are odd then it is X's turn; otherwise it is O's turn.
    if empty_count % 2 == 0:
        return O
    elif empty_count % 2 == 1: 
        return X
    

def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    i is row j is column range 0, 1, and 2
    """
    # Find the coordinate/index of EMPTY in board
    possible_actions = set()

    for i, row in enumerate(board):
        for j, cell in enumerate(row):
            if cell == EMPTY:
                possible_actions.add((i, j))

    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """ 

    # Check if action is valid
    i = action[0]
    j = action[1]
    if i < 0 or i > 2 or j < 0 or j > 2:
        raise Exception("Invalid Action")

    copy_board = copy.deepcopy(board)

    # Check if that slot is empty
    if board[i][j] == EMPTY:
        copy_board[i][j] = player(board)
    else:
        raise Exception("Full slot.")

    return copy_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    One can win the game with three of their moves in 
    a row horizontally, vertically, or diagonally.
    """
    # Horizontally
    for row in board:
        if not row.count(EMPTY):
            if row[0] == row[1] == row[2]:
                return row[0]

    # Vertically
    row = 0
    for column in range(len(board)):
        if board[row][column] == board[row+1][column] == board[row+2][column]:
            if board[row][column] != EMPTY:
                return board[row][column]
        row = 0

    # Diagonally 
    # (0,0) (1,1) (2,2): Column is in the same order of the row.
    diagonal = set()
    for i in range(len(board)):
        diagonal.add(board[i][i])
        
    if len(diagonal) == 1 and EMPTY not in diagonal:
        return board[i][i]

    # Anti-Diagonal 
    # (0,2) (1,1) (2,0): Column is in reverse order of the row.
    anti_diagonal = set()
    for i, j in zip(range(len(board)), range(len(board)-1,-1,-1)):
        anti_diagonal.add(board[i][j])
        
    if len(anti_diagonal) == 1 and EMPTY not in anti_diagonal:
        return board[i][j]

    # The board is full and no winner yet so it is a Draw
    count_empty = sum(row.count(EMPTY) for row in board)
    if count_empty == 0 or count_empty == 9:
        return None

    # The game has not ended yet
    return False


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    
    count_empty = sum(row.count(EMPTY) for row in board)

    # Board full 
    if count_empty == 0:
        return True
    # Board completely empty
    elif count_empty == 9:
        return False
    
    # There is a winner, so game is over .
    if winner(board) != False:
        return True

    # Game is ongoing.
    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Assuming utility will only be called on a board if terminal(board) is True

    current_winner = winner(board)
    if current_winner == "X":
        return 1
    elif current_winner == "O":
        return -1
    elif current_winner == None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """

    """
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the best_move function should return None.
    """
    
    current_player = player(board)
    current_actions = actions(board)

    if terminal(board):
        return utility(board)
    
    if current_player == "O":
        min_value = float('+inf')

        for action in current_actions:
            eval = minimax(result(board, action))
            if type(eval) == int:
                min_value = min(min_value, eval)
                best_action = action 
            elif eval[0] < min_value:
                min_value = eval[0]
                best_action = action
            
        return min_value, best_action

    elif current_player == "X":   
        max_value = float('-inf')
    
        for action in current_actions:
            eval = minimax(result(board, action))
            if type(eval) == int:
                max_value = max(max_value, eval)
                best_action = action
            elif eval[0] > max_value:
                max_value = eval[0]
                best_action = action
            
        return max_value, best_action
           

def best_move(board):
    """
    Returns the optimal action for the current player on the board.
    
    The move returned should be the optimal action (i, j) that is one of the allowable actions on the board. 
    If multiple moves are equally optimal, any of those moves is acceptable.
    If the board is a terminal board, the best_move function should return None.
    """

    if terminal(board):
        return None
    
    best_action = minimax(board)[1]

    return best_action