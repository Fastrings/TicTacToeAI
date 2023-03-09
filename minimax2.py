import engine
import utils
import copy
import simple_AIs
from math import inf as infinity

def minimax_ai(board, current_player):
    
    if len(utils.get_all_legal_moves(board)) == 9:
        return simple_AIs.get_random_move(board)
    
    bestVal = -infinity
    bestMove = (-1, -1)

    for i in range(engine.BOARD_HEIGHT):
        for j in range(engine.BOARD_WIDTH):
            if board[i][j] is None:
                new_board = copy.deepcopy(board)
                new_board = engine.make_move(new_board, (i, j), current_player)
                moveVal = minimax(new_board, 0, False)

                if moveVal > bestVal:
                    bestMove = (i, j)
                    bestVal = moveVal

    return bestMove

def minimax(board, depth, isMax):
    winner = engine.get_winner(board)

    if winner is not None:
        if winner == engine.PLAYERS[0]:
            return 10 - depth
        elif winner == engine.PLAYERS[1]:
            return -10 + depth
    elif engine.check_board_full(board):
        return 0
    
    if isMax:
        best = -infinity
        for i in range(engine.BOARD_HEIGHT):
            for j in range(engine.BOARD_WIDTH):
                if board[i][j] is None:
                    new_board = copy.deepcopy(board)
                    new_board = engine.make_move(new_board, (i, j), engine.PLAYERS[0])

                    best = max(best, minimax(new_board, depth + 1, not isMax))
        return best
    else:
        best = infinity
        for i in range(engine.BOARD_HEIGHT):
            for j in range(engine.BOARD_WIDTH):
                if board[i][j] is None:
                    new_board = copy.deepcopy(board)
                    new_board = engine.make_move(new_board, (i, j), engine.PLAYERS[1])

                    best = min(best, minimax(new_board, depth + 1, not isMax))
        return best