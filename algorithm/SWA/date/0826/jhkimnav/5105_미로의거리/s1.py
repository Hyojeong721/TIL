# visited
import sys
sys.stdin = open('input.txt')

def bfs(S):
    # 상 우 하 좌 (시계방향)
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]
    ni = 0
    nj = 0
    global maze, N, visited

    q = []
    q.append(S)
    visited[S[0]][S[1]] = 1

    while q:
        pre = q.pop(0)
        if maze[pre[0]][pre[1]] == 3:
            return visited[pre[0]][pre[1]] - 2
        for k in range(4):
            ni = pre[0] + dy[k]
            nj = pre[1] + dx[k]
            if ni in range(N) and nj in range(N) and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                q.append([ni, nj])
                visited[ni][nj] = visited[pre[0]][pre[1]] + 1

    return 0


# 0 : 통로
# 1 : 벽
T = int(input())
for TC in range(1, T+1):
    # 미로의 크기
    N = int(input())
    maze = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    S = []
    for n in range(N):
        maze[n] = list(map(int, input()))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                S = [i, j]

    answer = bfs(S)
    print('#{} {}'.format(TC, answer))