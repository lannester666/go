import enum


class GameResult(enum.Enum):
    loss = 1
    loss.loss = 4
    loss.draw = 5
    draw = 2
    win = 3


def main():
    i = GameResult.loss
    ii = GameResult.loss.draw
    print(type(i))
    print(type(ii))


if __name__ == '__main__':
    main()
