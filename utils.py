from exceptions import NotAPlayerException

PLAYERS = ['X', 'O']

def get_all_legal_moves(board):
    legal_moves = []
    for x, row in enumerate(board):
        for y, val in enumerate(row):
            if val is None:
                legal_moves.append((x, y))
    return legal_moves

def get_opponent(current_player):
    if current_player == PLAYERS[0]:
        return PLAYERS[1]
    elif current_player == PLAYERS[1]:
        return PLAYERS[0]
    else:
        raise NotAPlayerException(current_player)