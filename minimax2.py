import engine
import utils
import copy
import simple_AIs
from math import inf as infinity


cache = {}

def minimax_ai(board, current_player):
    
    legal_moves = utils.get_all_legal_moves(board)
    
    if len(legal_moves) == 9:
        return simple_AIs.get_random_move(board)
    
    bestVal = -infinity
    bestMove = (-1, -1)

    for move in legal_moves:
        new_board = copy.deepcopy(board)
        new_board = engine.make_move(new_board, move, current_player)
        moveVal = minimax(new_board, 0, False)

        if moveVal > bestVal:
            bestMove = move
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
    
    cache_key = str(board)
    if cache_key not in cache:

        legal_moves = utils.get_all_legal_moves(board)
        if isMax:
            best = -infinity
            for move in legal_moves:
                new_board = copy.deepcopy(board)
                new_board = engine.make_move(new_board, move, engine.PLAYERS[0])

                best = max(best, minimax(new_board, depth + 1, not isMax))
            cache[cache_key] = best
        else:
            best = infinity
            for move in legal_moves:
                new_board = copy.deepcopy(board)
                new_board = engine.make_move(new_board, move, engine.PLAYERS[1])

                best = min(best, minimax(new_board, depth + 1, not isMax))
            cache[cache_key] = best
    
    return cache[cache_key]