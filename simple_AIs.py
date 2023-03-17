import random
import utils
import copy
import exceptions
import sys

BOARD_HEIGHT = 3
BOARD_WIDTH = 3

def get_winner(board):
    """
    This function is used to get the winner of the game, if there is one. This
    function takes in 1 argument, the board, and returns the player (X or O) 
    that won, or None if there is no winner.
    """

    def checkRows(board):
        """
        This function is used to check for a winner in the rows of a board. This
        function takes in 1 argument, the board, and returns the player (X or O) 
        that won, or None if there is no winner.
        """
        for row in board:
            if len(set(row)) == 1:
                return row[0]
        return None
    
    def checkDiagonals(board):
        """
        This function is used to check for a winner in the diagonals of a board. This
        function takes in 1 argument, the board, and returns the player (X or O) 
        that won, or None if there is no winner.
        """
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)- i - 1] for i in range(len(board))])) == 1:
            return board[0][len(board) - 1]
        return None

    tr = [[row[i] for row in board] for i in range(max(len(r) for r in board))]

    for b in [board, tr]:
        res = checkRows(b)
        if res is not None:
            return res
        
    return checkDiagonals(board)

def get_random_move(board):
    legal_moves = utils.get_all_legal_moves(board)
    return random.choice(legal_moves)

def get_winning_move(board, current_player):
    legal_moves = utils.get_all_legal_moves(board)
    for move in legal_moves:
        new_board = copy.deepcopy(board)
        new_board[move[0]][move[1]] = current_player
        winner = get_winner(new_board)
        if winner == current_player:
            return move

def random_ai(board, current_player):
    #look at board
    #get all legal moves
    #return one at random
    return get_random_move(board)

def finds_winning_move_ai(board, current_player):
    #look at board
    #get all legal moves
    #if one makes player win the game : return it
    winning_move = get_winning_move(board, current_player)
    if winning_move is not None:
        return winning_move
    #otherwise : return random move
    return get_random_move(board)

def finds_winning_and_losing_moves_ai(board, current_player):
    #look at board
    #get all legal moves
    #if one makes player win the game: return it
    winning_move = get_winning_move(board, current_player)
    if winning_move is not None:
        return winning_move
    #if one makes opponent win the game : return it
    opponent = utils.get_opponent(current_player)
    opponent_winning_move = get_winning_move(board, opponent)
    if opponent_winning_move is not None:
        return opponent_winning_move
    #otherwise: return random move
    return get_random_move(board)

def mid_ai(board, current_player):
    winning_move = get_winning_move(board, current_player)
    if winning_move is not None:
        return winning_move

    opponent = utils.get_opponent(current_player)
    opponent_winning_move = get_winning_move(board, opponent)
    if opponent_winning_move is not None:
        return opponent_winning_move
    
    if board[1][1] is None:
        return (1, 1)
    
    corners = [(0, 0), (2, 0), (0, 2), (2, 2)]
    open_corners = [c for c in corners if board[c[0]][c[1]] is None]
    if open_corners:
        return random.choice(open_corners)
    
    return get_random_move(board)

def human_player(board, current_player):

    x = utils.get_input(f"What is your move's X coordinate ? (input number between 0 and {BOARD_HEIGHT - 1})")
    y = utils.get_input(f"What is your move's Y coordinate ? (input number between 0 and {BOARD_WIDTH - 1})")

    try:
        x = int(x)
    except ValueError:
        raise exceptions.NotANumberException(x)
    
    try:
        y = int(y)
    except ValueError:
        raise exceptions.NotANumberException(y)
    
    return (x, y)