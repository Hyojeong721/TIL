import sys
sys.stdin = open('input.txt')

def find_path(x, y):
    queue = []
    visited[x][y] = 1
    dist[x][y] = 0

    dx = [-1, 0, 1, 0]
    dy = [0, 1, 0, -1]

    queue.append([x,y])
    while queue:
        x, y = queue.pop(0)
        if maze[x][y] == 3:
            return dist[x][y] - 1
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if nx in range(N) and ny in range(N) and visited[nx][ny] == 0 and maze[nx][ny] != 1:
                queue.append([nx, ny])
                visited[nx][ny] = 1
                dist[nx][ny] = dist[x][y] + 1
    return 0

T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dist = [[0] * N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                x, y = i, j

    result =  find_path(x, y)
    print("#{} {}".format(test_case, result))