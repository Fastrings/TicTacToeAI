import pytest
import engine
from exceptions import OutOfBoardException, NotAPlayerException, NotEmptySpaceException, NotANumberException

class TestClass:

    def test_new_board(self):
        board = engine.new_board()

        assert board == [[None, None, None], [None, None, None], [None, None, None]]
        assert board != None

    def test_render(self):
        board = engine.new_board()
        strng = engine.render(board, output=False)
        assert strng == '|   |   |   |\n|   |   |   |\n|   |   |   |\n'
        board[0][0] = 'X'
        strng = engine.render(board, output=False)
        assert strng == '| X |   |   |\n|   |   |   |\n|   |   |   |\n'
    
    def test_make_move_legal(self):
        board = engine.new_board()
        board = engine.make_move(board, ('1', '1'), 'X')
        board = engine.make_move(board, ('2', '2'), 'O')
        assert board[0][0] == 'X'
        assert board[1][1] == 'O'

    def test_make_move_out_of_bounds(self):
        board = engine.new_board()
        with pytest.raises(OutOfBoardException):
            board = engine.make_move(board, ('1', '7'), 'X')
    
    def test_make_move_not_empty_space(self):
        board = engine.new_board()
        board = engine.make_move(board, ('1', '1'), 'X')
        with pytest.raises(NotEmptySpaceException):
            board = engine.make_move(board, ('1', '1'), 'X')

    def test_make_move_invalid_player(self):
        board = engine.new_board()
        with pytest.raises(NotAPlayerException):
            board = engine.make_move(board, ('1', '1'), 'bloop')
        
    def test_make_move_not_number_coords(self):
        board = engine.new_board()
        with pytest.raises(NotANumberException):
            board = engine.make_move(board, ('7', 'bloop'), 'X')

    def test_get_winner_X(self):
        board = engine.new_board()
        board = engine.make_move(board, ('1', '1'), 'X')
        board = engine.make_move(board, ('2', '2'), 'X')
        board = engine.make_move(board, ('1', '2'), 'O')
        board = engine.make_move(board, ('1', '3'), 'O')
        board = engine.make_move(board, ('3', '3'), 'X')
        assert engine.get_winner(board) == 'X'

    def test_get_winner_O(self):
        board = engine.new_board()
        board = engine.make_move(board, ('1', '1'), 'O')
        board = engine.make_move(board, ('2', '2'), 'O')
        board = engine.make_move(board, ('1', '2'), 'X')
        board = engine.make_move(board, ('1', '3'), 'X')
        board = engine.make_move(board, ('3', '3'), 'O')
        assert engine.get_winner(board) == 'O'

    def test_get_winner_noone(self):
        board = engine.new_board()
        board = engine.make_move(board, ('1', '1'), 'O')
        board = engine.make_move(board, ('2', '2'), 'O')
        board = engine.make_move(board, ('1', '2'), 'X')
        board = engine.make_move(board, ('1', '3'), 'X')
        assert engine.get_winner(board) == None

    def test_check_board_full(self):
        board = engine.new_board()
        board = engine.make_move(board, ('1', '1'), 'O')
        board = engine.make_move(board, ('2', '2'), 'O')
        board = engine.make_move(board, ('1', '2'), 'X')
        board = engine.make_move(board, ('1', '3'), 'X')
        board = engine.make_move(board, ('3', '3'), 'O')
        board = engine.make_move(board, ('2', '1'), 'O')
        board = engine.make_move(board, ('2', '3'), 'O')
        board = engine.make_move(board, ('3', '1'), 'O')
        board = engine.make_move(board, ('3', '2'), 'O')
        assert engine.check_board_full(board) == True

    def test_check_board_not_full(self):
        board = engine.new_board()
        assert engine.check_board_full(board) == False