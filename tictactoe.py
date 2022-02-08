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
    if terminal(board):
        return None
    
    count_x = count_o = 0
    for i in range(3):
        count_x = count_x + board[i].count(X)
        count_o = count_o + board[i].count(O)

    if count_x is count_o:
        return X
    else:
        return O
    #raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    if terminal(board):
        return None
    
    action_list = []
    for i in range(3):
        for j in range(3):
            if board[i][j] is EMPTY:
                action_list.append((i,j))
    
    return action_list

    #raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    active_player = player(board)
    resulting_board = copy.deepcopy(board)
    resulting_board[action[0]][action[1]] = active_player
    return resulting_board
    #raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    #checking in rows and coloums
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2]:
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i]:
            return board[0][i]
    
    # checking for diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0]:
        return board[0][2]
    
    #No winner
    return None
    #raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise
    """
    if winner(board):
        return True
    
    for list in board:
        if EMPTY in list:
            return False
    return True

    #raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if X == winner(board):
        return 1
    elif O == winner(board):
        return -1
    else:
        return 0
    raise NotImplementedError


def min_value(board):
    """
    Returns the optimal 
    """
    if terminal(board):
        return utility(board)
    
    ret_value = math.inf
    for action in actions(board):
        ret_value = min(ret_value, max_value(result(board,action)))
    
    return ret_value


def max_value(board):
    """
    Returns the optimal 
    """
    if terminal(board):
        return utility(board)
    
    ret_value = - math.inf
    for action in actions(board):
        ret_value = max(ret_value, min_value(result(board,action)))
    
    return ret_value


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    current_player = player(board)
    if terminal(board):
        return None
    
    ret_action = None

    if current_player is X:
        ret_val = - math.inf
        for action in actions(board):
            out_val = max_value(board)
            if out_val > ret_val:
                ret_action = action
        
    else:
        ret_val = math.inf
        for action in actions(board):
            out_val = min_value(board)
            if out_val < ret_val:
                ret_action = action
    
    return ret_action
    #raise NotImplementedError
