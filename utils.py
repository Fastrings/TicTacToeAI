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
    
def print_help(table):
    print("Welcome to the help section of this TicTacToe program!")
    print("How to use this program?")
    print("- If you want to battle an AI yourself, enter 'main.py' in the terminal and more instructions will be prompted.")
    print("- If you want AIs to battle themselves, enter 'main.py battles ai1 ai2' in the terminal, where ai1 and ai2", end='')
    print(" are the names of the AIs you want to send to battle.")
    print("Here are all the AIs available:")
    for algo in table.keys():
        print("---> ", end='')
        print(algo)