from gotypes import Point


def is_point_an_eye(board, point, color):    # 判断该点是否为一个真眼
    if board.get(point) is not None:
        return False
    for neighbor in point.neighbors():
        if board.is_on_grid(neighbor):
            neighbor_color = board.get(neighbor)
            if neighbor_color != color:
                return False  # 相邻点必须为同色棋子

    friendly_corners = 0
    off_board_corners = 0
    corners = [
        Point(point.row-1, point.col-1),
        Point(point.row-1, point.col+1),
        Point(point.row+1, point.col-1),
        Point(point.row+1, point.col+1),
    ]
    for corner in corners:
        if board.is_on_grid(corner):
            corner_color = board.get(corner)
            if corner_color == color:
                friendly_corners += 1    # 若四个对角线上的点都在棋盘内，则至少有三个为同色说明为真眼；若有点在棋盘外，则四个点都必须是同色
        else:
            off_board_corners += 1
    if off_board_corners > 0:
        return off_board_corners+friendly_corners == 4
    return friendly_corners >= 3
