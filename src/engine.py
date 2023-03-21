from .other.exceptions import NotANumberException, NotEmptySpaceException, NotAPlayerException, OutOfBoardException
from copy import deepcopy

BOARD_HEIGHT = 3
BOARD_WIDTH = 3
PLAYERS = ['X', 'O']

def new_board():
    """
    This function is used to create a new board. It takes in 0 arguments and
    returns a new empty grid of dimensions BOARD_HEIGHT * BOARD_WIDTH.
    """

    return [[None] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

def render(board, output=True):
    """
    This function is used to pretty-print a board. It takes in 1 argument,
    a board to print to the terminal, and returns nothing.
    """
    ret = ""

    for line in board:
        if output:
            print('|', end='')
        else:
            ret += "|"
        for move in line:
            to_print = move if move is not None else ' '
            if output:
                print(f' {to_print} ', end='|')
            else:
                ret += f' {to_print} |'
        if output:
            print('')
        else:
            ret += "\n"
    
    if not output:
        return ret

def make_move(board, coords, player):
    """
    This function is used to make a move on the board. It takes in 3
    arguments : the board, the coordinates of the move and the player 
    making the move. If the move is illegal, the function raises an
    exception accordignly. If the move is legal the function returns a 
    new board with the move made.
    """
    x, y = coords[0], coords[1]

    if x >= BOARD_HEIGHT or y >= BOARD_WIDTH:
        raise OutOfBoardException(x, y)
    elif board[x][y] is not None:
        raise NotEmptySpaceException(board[x][y])
    elif player not in PLAYERS:
        raise NotAPlayerException(player)

    new_board = deepcopy(board)
    new_board[x][y] = player
    return new_board

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

def check_board_full(board):
    """
    This function checks whether the board is full. It takes in 1 argument,
    the board, and returns True if the board is full, false otherwise.
    """

    for col in board:
        for sq in col:
            if sq is None:
                return False
    return True

def play(player1_algo, player2_algo, silent=True):
    """
    The main engine function that runs the game.
    """
    turn = 0
    board = new_board()
    players = [
        (PLAYERS[0], player1_algo),
        (PLAYERS[1], player2_algo),
    ]

    while True:
        current_player_symbol, current_player_algo = players[turn % 2]
        if turn != 0:
            render(board, output=silent)
        if silent:
            print("----------------------------------------")
        try:
            move_coords = current_player_algo(board, current_player_symbol)
        except NotANumberException as ex:
            print(ex.__str__())
            continue
        try:
            board = make_move(board, move_coords, current_player_symbol)
        except OutOfBoardException as ex:
            print(ex.__str__())
            continue
        except NotEmptySpaceException as ex:
            print(ex.__str__())
            continue
        except NotANumberException as ex:
            print(ex.__str__())
            continue

        winner = get_winner(board)

        if winner is not None:
            render(board, output=silent)
            if silent:
                print("----------------------------------------")
            print(f'WINNER IS {winner}!!!!!')
            return winner

        if check_board_full(board):
            render(board, output=silent)
            if silent:
                print("----------------------------------------")
            print("IT'S A DRAW!!!!!")
            return 'D'

        turn += 1
