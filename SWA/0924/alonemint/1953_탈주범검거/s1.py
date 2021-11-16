import sys
from pprint import pprint
sys.stdin = open('sample_input.txt')

T = int(input())

def find_route(board, num, row, col):
    #우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    res = []
    for i in range(4):
        if 0 <= row + dr[i] < len(board) and 0 <= col + dc[i] < len(board[0]):
            res.append([row + dr[i], col + dc[i]])
    if num == 1:
        return res
    my_res = []
    if num == 2:
        if [row + dr[3], col + dc[3]] in res:
            my_res.append([row + dr[3], col + dc[3]])
        if [row + dr[1], col + dc[1]] in res:
            my_res.append([row + dr[1], col + dc[1]])
        return my_res
    elif num == 3:
        if [row + dr[0], col + dc[0]] in res:
            my_res.append([row + dr[0], col + dc[0]])
        if [row + dr[2], col + dc[2]] in res:
            my_res.append([row + dr[2], col + dc[2]])
        return my_res
    elif num == 4:
        if [row + dr[0], col + dc[0]] in res:
            my_res.append([row + dr[0], col + dc[0]])
        if [row + dr[3], col + dc[3]] in res:
            my_res.append([row + dr[3], col + dc[3]])
        return my_res
    elif num == 5:
        if [row + dr[0], col + dc[0]] in res:
            my_res.append([row + dr[0], col + dc[0]])
        if [row + dr[1], col + dc[1]] in res:
            my_res.append([row + dr[1], col + dc[1]])
        return my_res
    elif num == 6:
        if [row + dr[1], col + dc[1]] in res:
            my_res.append([row + dr[1], col + dc[1]])
        if [row + dr[2], col + dc[2]] in res:
            my_res.append([row + dr[2], col + dc[2]])
        return my_res
    elif num == 7:
        if [row + dr[3], col + dc[3]] in res:
            my_res.append([row + dr[3], col + dc[3]])
        if [row + dr[2], col + dc[2]] in res:
            my_res.append([row + dr[2], col + dc[2]])
        return my_res
    return []

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())

    board = [list(map(int, input().split())) for _ in range(N)]
    time_board = [[0] * M for _ in range(N)]
    queue = [[R,C]]
    time_board[R][C] = 1
    while queue:
        v = queue.pop(0)

        for route in find_route(board, board[v[0]][v[1]], v[0], v[1]):
            if board[route[0]][route[1]] > 0 and time_board[route[0]][route[1]] == 0:
                if [v[0],v[1]] in find_route(board, board[route[0]][route[1]], route[0], route[1]):
                    time_board[route[0]][route[1]] = time_board[v[0]][v[1]] + 1
                    queue.append(route)
    cnt = 0
    for i in range(N):
        for j in range(M):
            if 0 < time_board[i][j] <= L:
                cnt += 1
    print(f'#{tc} {cnt}')