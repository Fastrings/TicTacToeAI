import sys
import engine
import simple_AIs
import minimax
import minimax2

CORRESPONDANCE_TABLE = {
    'random': simple_AIs.random_ai,
    'get_winning': simple_AIs.finds_winning_move_ai,
    'get_winning_and_losing': simple_AIs.finds_winning_and_losing_moves_ai,
    'human': simple_AIs.human_player,
    'minimax': minimax.minimax_ai,
    'minimax2': minimax2.minimax_ai,
}


if __name__ == "__main__":
    if sys.argv[1] == 'battles':
        num = int(sys.argv[2])
        player1_algo = CORRESPONDANCE_TABLE[sys.argv[3]]
        player2_algo = CORRESPONDANCE_TABLE[sys.argv[4]]

        tally = engine.repeated_battles(player1_algo, player2_algo, num)
        print(f'{num} battles done.\nResults: {sys.argv[3]} won {tally[0]} battles, {sys.argv[4]} won {tally[1]} battles, {tally[2]} battle(s) was(ere) drawn.')
        sys.exit(0)

    player1_algo = CORRESPONDANCE_TABLE[sys.argv[1]]
    player2_algo = CORRESPONDANCE_TABLE[sys.argv[2]]

    if sys.argv[2] == "better_minimax":
        player1_algo, player2_algo = player2_algo, player1_algo

    result = engine.play(player1_algo, player2_algo)