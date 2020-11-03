from test_tic_tac_toe.types_ import Player, Point

COLS = 'ABCDEFGHGKLMNOPQRST'  # 去除I
STONE_TO_CHAR = {
    None: ' . ',
    Player.x: ' x ',
    Player.o: ' o ',
}


def print_move(player, move):
    move_str = '%s%d' % (COLS[move.point.col - 1], move.point.row)
    print('%s %s' % (player, move_str))


def print_board(board):
    for row in range(3, 0, -1):   # 从大到小
        bump = " "
        line = []
        for col in range(1, 4):
            stone = board.get(Point(row=row, col=col))
            line.append(STONE_TO_CHAR[stone])
        print('%s%d %s' % (bump, row, ''.join(line)))
    print('    ' + '  '.join(COLS[:3]))


def point_from_coords(coords):
    col = COLS.index(coords[0])+1
    row = int(coords[1:])
    return Point(row, col)
