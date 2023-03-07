import simple_AIs
import engine

class TestClass:

    def test_random_ai(self):
        board = engine.new_board()

        move = simple_AIs.random_ai(board, 'X')
        assert type(move[0]) == int
        assert type(move[1]) == int
        assert move[0] >= 0
        assert move[0] <= 2 
        assert move[1] >= 0
        assert move[1] <= 2 

    def test_winning_ai(self):
        board = engine.new_board()

        board = engine.make_move(board, (0, 0), 'X')
        board = engine.make_move(board, (0, 1), 'X')
        board = engine.make_move(board, (2, 2), 'O')

        move = simple_AIs.finds_winning_move_ai(board, 'X')

        assert move == (0, 2)


    def test_winning_and_blocking_ai(self):
        board = engine.new_board()

        board = engine.make_move(board, (0, 0), 'X')
        board = engine.make_move(board, (1, 0), 'X')
        board = engine.make_move(board, (2, 2), 'O')

        move_win = simple_AIs.finds_winning_and_losing_moves_ai(board, 'X')
        move_block = simple_AIs.finds_winning_and_losing_moves_ai(board, 'O')

        assert move_win == (2, 0)
        assert move_block == (2, 0)