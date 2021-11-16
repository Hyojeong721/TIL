# 스택 방식!
import sys
sys.stdin = open('input.txt')


def solution(c, r):
    result = 0
    global start_col, start_row, goal_col, goal_row, maze, visited, N
    stack = [c, r]
    # 상 우 하 좌
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    while len(stack):
        r = stack.pop()
        c = stack.pop()

        # 방문하지 않은 곳이라면
        if visited[c][r] == 0:
            visited[c][r] = 1

            for k in range(4):
                nc = c + dy[k]
                nr = r + dx[k]
                if 0 <= nc < N and 0 <= nr < N and visited[nc][nr] == 0 and maze[nc][nr] == 0:
                    stack.append(nc)
                    stack.append(nr)
                if nc == goal_col and nr == goal_row:
                    result = 1
                    return result

    return result


T = int(input())

for TC in range(1, T+1):
    N = int(input())
    visited = [[0 for _ in range(N)] for _ in range(N)]
    maze = [[0] for _ in range(N)]
    # 입력받으며 시작, 도착 idx 찾기
    for n in range(N):
        maze[n] = list(map(int, input()))
        # 시작 idx 찾기
        if maze[n].count(2):
            start_col, start_row = n, maze[n].index(2)
        # 도착 idx 찾기
        if maze[n].count(3):
            goal_col, goal_row = n, maze[n].index(3)

    answer = solution(start_col, start_row)

    print('#{} {}'.format(TC, answer))