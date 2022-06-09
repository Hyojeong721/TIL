# 재귀 방식!
import sys
sys.stdin = open('input2.txt')


def solution(c, r):
    global goal_col, goal_row, maze, visited, N, result
    # 상 우 하 좌
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    if maze[c][r] == 3:
        result = 1
        return result

    if visited[c][r] == 0:
        visited[c][r] = 1

    # 상
    nc = c + dy[0]
    nr = r + dx[0]
    if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0 and maze[nc][nr] != 1:
        solution(nc, nr)
    # 우
    nc = c + dy[1]
    nr = r + dx[1]
    if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0 and maze[nc][nr] != 1:
        solution(nc, nr)

    # 하
    nc = c + dy[2]
    nr = r + dx[2]
    if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0 and maze[nc][nr] != 1:
        solution(nc, nr)

    # 좌
    nc = c + dy[3]
    nr = r + dx[3]
    if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0 and maze[nc][nr] != 1:
        solution(nc, nr)

    return result

T = int(input())

for TC in range(1, T+1):
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    maze = [[0] for _ in range(N)]
    result = 0

    # 입력받으며 시작, 도착 idx 찾기
    for n in range(N):
        maze[n] = list(map(int, input()))
        # 시작 idx(2) 찾기
        if maze[n].count(2):
            start_col, start_row = n, maze[n].index(2)

    print('#{} {}'.format(TC, solution(start_col, start_row)))
    print()