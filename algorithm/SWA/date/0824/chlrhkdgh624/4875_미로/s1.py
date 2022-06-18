import sys
sys.stdin = open('input.txt')
T = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]


def path_find(arr, i, j):

    for d in range(4):
        next_i = i + dx[d]
        next_j = j + dy[d]
        if arr[next_i][next_j] == 2:
            return 1
        elif arr[next_i][next_j] == 0:
            path_find(arr, next_i, next_j)
        else:
            return 0


for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]

    start = []
    for row in range(N):
        for col in range(N):
            if maze[row][col] == 2:
                start.extend([row, col])

    path_find(maze, 4, 3)



