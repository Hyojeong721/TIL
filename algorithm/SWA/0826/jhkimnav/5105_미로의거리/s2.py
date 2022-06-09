# distance
import sys
sys.stdin = open('input.txt')

def bfs(S):
    # 상 우 하 좌 (시계방향)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    global maze, N, visited, dis

    q = []
    q.append(S)
    visited[S[0]][S[1]] = 1
    dis[S[0]][S[1]] = 0

    while q:
        pre = q.pop(0)
        if maze[pre[0]][pre[1]] == 3:
            return dis[pre[0]][pre[1]] - 1
        for k in range(4):
            ni = pre[0] + dy[k]
            nj = pre[1] + dx[k]
            if ni in range(N) and nj in range(N) and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = 1
                dis[ni][nj] = dis[pre[0]][pre[1]] + 1

    return 0


# 0 : 통로
# 1 : 벽
T = int(input())
for TC in range(1, T+1):
    # 미로의 크기
    N = int(input())
    maze = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    dis = [[0] * N for _ in range(N)]

    S = []
    for n in range(N):
        maze[n] = list(map(int, input()))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                S = [i, j]

    answer = bfs(S)
    print('#{} {}'.format(TC, answer))