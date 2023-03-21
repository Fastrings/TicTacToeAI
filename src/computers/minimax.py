
import src.engine as engine
import src.other.utils as utils
import copy


def minimax_ai(board, current_player):
    best_move = None
    best_score = None

    legal_moves = utils.get_all_legal_moves(board)

    for move in legal_moves:
        new_board = copy.deepcopy(board)
        new_board = engine.make_move(new_board, move, current_player)

        opponent = utils.get_opponent(current_player)

        score = minimax_score(new_board, opponent, current_player)

        if best_score is None or score > best_score:
            best_move = move
            best_score = score
    
    return best_move

def minimax_score(board, player_to_move, player_to_optimize):
    """
    Calculates the score of a given state, meaning that a higher score is a better
    move for player 1 and a lower score is a better move for player 2.
    """

    #if board in terminal state, return score immediately
    winner = engine.get_winner(board)
    if winner is not None:
        #x has won -> return 10
        if winner == player_to_optimize:
            return 10
        else:
            #o has won -> return -10
            return -10
    #draw -> return 0
    elif engine.check_board_full(board):
        return 0

    #get all legal moves
    scores = []
    legal_moves = utils.get_all_legal_moves(board)
    #look at all these moves at assign them a score
    for move in legal_moves:
        #make the move
        new_board = copy.deepcopy(board)
        new_board = engine.make_move(board, move, player_to_move)

        opponent = utils.get_opponent(player_to_move)

        #get minimax score for the resulting board
        opponent_best_response_score = minimax_score(new_board, opponent, player_to_optimize)
        scores.append(opponent_best_response_score)
    
    #if current player is X we maximimize
    if player_to_move == player_to_optimize:
        return max(scores)
    #otherwise we minimize
    else:
        return min(scores)