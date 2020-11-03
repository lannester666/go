
import os, sys
import agent
from agent import naive
import goboard_slow
import gotypes
from utils import print_board, print_move, point_from_coords
import time


def main():
    board_size = 9
    game = goboard_slow.GameState.new_game(board_size)
    bot = agent.naive.RandomBot()
    while not game.is_over():
        # time.sleep(0.3)
        os.system('cls')
        # print(chr(27)+"[2J")
        print_board(game.board)
        if game.next_player == gotypes.Player.black:
            human_move = input('-- ')  # input函数接收一个标准输入数据，返回为string类型
            point = point_from_coords(human_move.strip())  # 除去首尾的指定字符，默认为空格
            print(point)
            move = goboard_slow.Move.play(point)
            print_move(game.next_player, move)
        else:
            move = bot.select_move(game)
            print_move(game.next_player, move)
        game = game.apply_move(move)


if __name__ == '__main__':
    main()
