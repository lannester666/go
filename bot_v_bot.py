
import os

from pip._vendor.colorama.ansi import clear_screen

import agent
from agent import naive
import goboard_slow
import gotypes
from utils import print_board, print_move
import time


def main():
    st = time.time()
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bots = {
        gotypes.Player.black: agent.naive.RandomBot(),
        gotypes.Player.white: agent.naive.RandomBot(),
    }
    while not game.is_over():
        # time.sleep(0.3)
        # os.system('cls')
        # # print(chr(27)+"[2J")
        # # clear_screen()
        # print_board(game.board)
        bot_move = bots[game.next_player].select_move(game)
        # print_move(game.next_player, bot_move)
        game = game.apply_move(bot_move)
    et = time.time()
    print(et-st)


if __name__ == '__main__':
    main()
