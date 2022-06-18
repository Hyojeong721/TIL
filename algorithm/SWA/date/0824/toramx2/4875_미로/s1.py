import sys
sys.stdin = open('input.txt')

def route(x, y):
    global result
    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if nx in range(N) and ny in range(N):
            if maze[nx][ny] == 3:
                result = 1
                return result
            elif maze[nx][ny] == 0:
                maze[nx][ny] = 1
                route(nx, ny)

T = int(input())

for test_case in range(1,T+1):
    N = int(input())
    maze = []
    for _ in range(N):
        maze.append(list(map(int, input())))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j
    result = 0
    route(x, y)
    print("#{} {}".format(test_case, result))