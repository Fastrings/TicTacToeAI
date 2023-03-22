import src.engine as engine
import src.other.utils as utils
import copy
import src.computers.simple_AIs as simple_AIs
from math import inf as infinity

cache = {} # cache to reduce computing time

def minimax_ai(board, current_player):
    
    legal_moves = utils.get_all_legal_moves(board)
    
    if len(legal_moves) == 9:
        return simple_AIs.get_random_move(board)
    
    bestVal = -infinity
    bestMove = (-1, -1)

    for move in legal_moves: # get score for every move
        new_board = copy.deepcopy(board)
        new_board = engine.make_move(new_board, move, current_player)
        moveVal = minimax(new_board, 0, False, current_player)

        if moveVal > bestVal: # only keep the best score
            bestMove = move
            bestVal = moveVal

    return bestMove

def minimax(board, depth, isMax, player_to_optimize):
    winner = engine.get_winner(board)

    if winner is not None: # terminal node
        if winner == player_to_optimize:
            return 10 - depth
        elif winner == utils.get_opponent(player_to_optimize):
            return -10 + depth
    elif engine.check_board_full(board): # terminal node
        return 0
    
    cache_key = str(board)
    if cache_key not in cache: # only compute score if board not in cache

        legal_moves = utils.get_all_legal_moves(board)
        if isMax: # we are maximizing so we compute the best score for the current player
            best = -infinity
            for move in legal_moves:
                new_board = copy.deepcopy(board)
                new_board = engine.make_move(new_board, move, player_to_optimize)

                best = max(best, minimax(new_board, depth + 1, not isMax, player_to_optimize))
            cache[cache_key] = best
        else: # we are minimizing so we compute the worst score for the opponent
            best = infinity
            for move in legal_moves:
                new_board = copy.deepcopy(board)
                new_board = engine.make_move(new_board, move, utils.get_opponent(player_to_optimize))

                best = min(best, minimax(new_board, depth + 1, not isMax, player_to_optimize))
            cache[cache_key] = best
    
    return cache[cache_key]