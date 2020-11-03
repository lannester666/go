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
        os.system('cls')
        print(chr(27) + "[2J")
        print_board(game.board)
        if game.next_player == Player.x:
            human_move = input('-- ')  # input函数接收一个标准输入数据，返回为string类型
            point = point_from_coords(human_move.strip())  # 除去首尾的指定字符，默认为空格
            move = Move.play(point)
        else:
            move = bots[game.next_player].select_move(game)
            print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()
