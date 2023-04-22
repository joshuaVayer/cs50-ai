"""
Tic Tac Toe Player
"""
import copy
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
    X_count = 0
    O_count = 0

    for line in board:
        for cell in line:
            if cell == X:
                X_count += 1
            elif cell == O:
                O_count += 1

    # Game is finished
    if O_count + X_count == 9:
        return None

    if X_count > O_count:
        return O
    else:
        return X


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    available_actions = list()

    for i, line in enumerate(board):
        for j, cell in enumerate(line):
            if cell == EMPTY:
                available_actions.append((i, j))

    return available_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    if action not in actions(board):
        raise Exception("Invalid action")

    copied_board = copy.deepcopy(board)

    line, cell = action
    copied_board[line][cell] = player(board)

    return copied_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """

    for i in range(3):
        valid_line = all(board[i][j] == board[i][0] for j in range(3))
        if valid_line:
            return board[i][0]

        valid_column = all(board[j][i] == board[0][i] for j in range(3))
        if valid_column:
            return board[0][i]

        if board[0][0] is board[1][1] is board[2][2]:
            return board[0][0]

        if board[0][2] is board[1][1] is board[2][0]:
            return board[0][2]

    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    has_winner = winner(board) is not None
    if has_winner:
        return True

    is_tie = all(cell is not None for line in board for cell in line)
    return is_tie


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    game_winner = winner(board)

    if game_winner == X:
        return 1
    elif game_winner == O:
        return -1
    else:
        return 0

def max_value(board):
    v = -math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = max(v, min_value(result(board, action)))
        return v


def min_value(board):
    v = math.inf

    if terminal(board):
        return utility(board)

    for action in actions(board):
        v = min(v, max_value(result(board, action)))
        return v


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    best_action = None
    if player(board) == X:
        v = -math.inf
        for action in actions(board):
            v = max(v, min_value(result(board, action)))
            if v == min_value(result(board, action)):
                best_action = action
        return best_action
    else:
        v = math.inf
        for action in actions(board):
            v = min(v, max_value(result(board, action)))
            if v == max_value(result(board, action)):
                best_action = action
        return best_action
