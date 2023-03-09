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
    try:
        if sys.argv[1] and sys.argv[1] == 'battles':
            num = int(sys.argv[2])
            player1_algo = CORRESPONDANCE_TABLE[sys.argv[3]]
            player2_algo = CORRESPONDANCE_TABLE[sys.argv[4]]

            tally = engine.repeated_battles(player1_algo, player2_algo, num)
            print(f'{num} battles done.\nResults: {sys.argv[3]} won {tally[0]} battles, {sys.argv[4]} won {tally[1]} battles, {tally[2]} battle(s) was(ere) drawn.')
            sys.exit(0)
    except IndexError as ex:
        pass

    while True:
        inp = "Which AI do you want to battle today:\n"
        for algo in CORRESPONDANCE_TABLE.keys():
                inp += "---> "
                inp += algo
                inp += "\n"

        x = input(inp)
        if x not in CORRESPONDANCE_TABLE:
            print("Unknown AI. Please try again.")
        else:            
            ai = CORRESPONDANCE_TABLE[x]
            break

    result = engine.play(ai, simple_AIs.human_player)