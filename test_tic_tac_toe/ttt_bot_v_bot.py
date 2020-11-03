import os
import time
from test_tic_tac_toe.Agent import *
from test_tic_tac_toe.print_util import *


def main():
    game = GameState.new_game()
    bots = {
        Player.o: MinimaxAgent(),
        Player.x: MinimaxAgent()
    }
    while not game.is_over():
        time.sleep(0.3)
        os.system('cls')
        print(chr(27) + "[2J")
        print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)


if __name__ == '__main__':
    main()
