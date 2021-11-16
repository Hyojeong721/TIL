import sys
sys.stdin = open('input.txt')
T = 10


def start_point(ladder, x_point):
    now_x = x_point
    now_y = 99
    d = 0
    dx = [1, -1, 0]
    dy = [0, 0, -1]

    while now_y > 0:
        move_x = now_x + dx[d]

        if move_x < 0 or move_x >= 100:
            d = (d+1) % 2
            now_y -= 1
            continue

        if ladder[now_x][now_y - 1] == 1:
            now_y -= 1
            continue

        if ladder[move_x][now_y] != 0:
            now_x = move_x
            continue

        if ladder[move_x][now_y] == 0:
            now_y -= 1
            continue

    return now_x


for _ in range(T):
    tc = int(input())
    board = [list(map(int, input().split())) for k in range(100)]
    start = board[-1].index(2)
    print(start_point(board, start))
