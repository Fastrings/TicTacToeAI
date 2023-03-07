import sys
import engine

if __name__ == "__main__":
    player1_algo_name = sys.argv[1]
    player2_algo_name = sys.argv[2]

    engine.play(player1_algo_name, player2_algo_name)