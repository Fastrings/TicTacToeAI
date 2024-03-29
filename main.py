import sys
import src.engine as engine
import src.other.utils as utils
from src.computers import simple_AIs, minimax, minimax2
from src.other.battles import repeated_battles

CORRESPONDANCE_TABLE = {
    'random': simple_AIs.random_ai,
    'get_winning': simple_AIs.finds_winning_move_ai,
    'get_winning_and_losing': simple_AIs.finds_winning_and_losing_moves_ai,
    'human': simple_AIs.human_player,
    'minimax': minimax.minimax_ai,
    'minimax2': minimax2.minimax_ai,
    'mid': simple_AIs.mid_ai,
}


if __name__ == "__main__":
    try:
        if sys.argv[1] and sys.argv[1] == 'battles':
            num = int(sys.argv[2])
            player1 = (sys.argv[3], CORRESPONDANCE_TABLE[sys.argv[3]])
            player2 = (sys.argv[4], CORRESPONDANCE_TABLE[sys.argv[4]])
            save = True if 'save' in sys.argv else False
            tally = repeated_battles(player1, player2, num, save)
            print(f'{num} battle(s) done.\nResults: {sys.argv[3]} won {tally[0]} battles, {sys.argv[4]} won {tally[1]} battles, {tally[2]} battle(s) was(ere) drawn.')
            sys.exit(0)
        if sys.argv[1] == 'help':
            utils.print_help(CORRESPONDANCE_TABLE)
            sys.exit(0)
        if sys.argv[1] and sys.argv[1] != 'help':
            print("Invalid use of program. Please see the help section 'main.py help' for more information.")
            sys.exit(0)
    except IndexError as ex:
        pass

    while True:
        inp = "Which AI do you want to battle today:\n" # list all available AI opponents
        for algo in CORRESPONDANCE_TABLE.keys():
                inp += "---> "
                inp += algo
                inp += "\n"

        x = utils.get_input(inp)
        if x not in CORRESPONDANCE_TABLE:
            print("Unknown AI. Please try again.")
            continue
        else:            
            ai = CORRESPONDANCE_TABLE[x]
            x = utils.get_input("Do you want to play first?(Y/N)")
            break

    if x == 'N':
        result = engine.play(ai, simple_AIs.human_player)
    else:
        result = engine.play(simple_AIs.human_player, ai)