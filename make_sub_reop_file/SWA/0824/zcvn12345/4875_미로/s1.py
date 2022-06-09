import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start = (i, j)
            elif maze[i][j] == '3':
                end = (i, j)
            elif maze[i][j] == '1':
                visited[i][j] = 1


    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    stack = [start]
    y = start[0]
    x = start[1]

    while stack:
        a = stack.pop()
        y = a[0]
        x = a[1]
        if visited[y][x] == 0:
            visited[y][x] = 1
            for i in range(4):
                ty = y + dy[i]
                tx = x + dx[i]
                if 0 <= tx < N and 0 <= ty < N and visited[ty][tx] == 0:
                    stack.append((ty, tx))


    print(visited[end[0]][end[1]])




        





