import random
from agent.base import Agent
from agent.helpers import is_point_an_eye
from goboard_slow import Move
from gotypes import Point


class RandomBot(Agent):  # 继承Agent类
    def select_move(self, game_state):
        candidates = []
        for r in range(1, game_state.board.num_rows + 1):  # range（）函数为前一个参数到后一个参数之间，包括之前，不包括之后
            for c in range(1, game_state.board.num_cols + 1):
                candidate = Point(r, c)
                if game_state.is_valid_move(Move.play(candidate)) and \
                        not is_point_an_eye(game_state.board, candidate, game_state.next_player):
                    candidates.append(candidate)
        if not candidates:
            return Move.pass_turn()
        return Move.play(random.choice(candidates))


'''每次下棋前扫描棋盘上可以下的所有点存入candidate中，再用随机函数从这些点中随机选一个点作为下的位置'''
