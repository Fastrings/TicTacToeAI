import sys
import engine
import simple_AIs
import minimax

CORRESPONDANCE_TABLE = {
    'random': simple_AIs.random_ai,
    'get_winning': simple_AIs.finds_winning_move_ai,
    'get_winning_and_losing': simple_AIs.finds_winning_and_losing_moves_ai,
    'human': simple_AIs.human_player,
    'minimax': minimax.minimax_ai,
}

if __name__ == "__main__":
    player1_algo = CORRESPONDANCE_TABLE[sys.argv[1]]
    player2_algo = CORRESPONDANCE_TABLE[sys.argv[2]]

    engine.play(player1_algo, player2_algo)