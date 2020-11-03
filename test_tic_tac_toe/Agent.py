import enum
import random

from agent.base import Agent
from .funcs import *


class GameResult(enum.Enum):
    loss = 1
    draw = 2
    win = 3


def reverse_game_result(game_result):
    if game_result == GameResult.loss:
        return GameResult.win
    if game_result == GameResult.win:
        return GameResult.loss
    else:
        return GameResult.draw


def best_result(game_state: GameState):
    if game_state.is_over():
        if game_state.winner() == game_state.next_player:
            return GameResult.win
        elif game_state.winner() is None:
            return GameResult.draw
        else:
            return GameResult.loss
    best_result_so_far = GameResult.loss
    for candidate_move in game_state.legal_moves():
        next_state = game_state.apply_move(candidate_move)
        opponent_best_result = best_result(next_state)
        my_result = reverse_game_result(opponent_best_result)
        if my_result.value > best_result_so_far.value:
            best_result_so_far = my_result
    return best_result_so_far


class MinimaxAgent(Agent):
    def select_move(self, game_state: GameState):
        winning_moves = []
        drawing_moves = []
        losing_moves = []
        for possible_move in game_state.legal_moves():
            next_state = game_state.apply_move(possible_move)
            opponent_best_result = best_result(next_state)
            my_result = reverse_game_result(opponent_best_result)
            if my_result == GameResult.win:
                winning_moves.append(possible_move)
            elif my_result == GameResult.draw:
                drawing_moves.append(possible_move)
            else:
                losing_moves.append(possible_move)
        if winning_moves:
            return random.choice(winning_moves)
        if drawing_moves:
            return random.choice(drawing_moves)
        return random.choice(losing_moves)