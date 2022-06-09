import sys
sys.stdin = open('input.txt')

def bfs(S):
    global N, maze, visited
    # 상 우 하 좌
    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    q = []
    # 시작 좌표를 enque
    q.append([S[0], S[1]])
    visited[S[0]][S[1]] = 1

    while q:
        pre = q.pop(0)
        if maze[pre[0]][pre[1]] == 3:
            return 1
        for k in range(4):
            ni = pre[0] + dy[k]
            nj = pre[1] + dx[k]
            if ni in range(N) and nj in range(N) and visited[ni][nj] == 0 and maze[ni][nj] != 1:
                q.append([ni, nj])
                visited[ni][nj] = 1
    return 0


# 1 : 벽
# 0 : 길
# 2 : 출발점
for _ in range(10):

    TC = int(input())
    N = 16
    maze = [[0] * N for _ in range(N)]
    visited = [[0] * N for _ in range(N)]

    for n in range(N):
        maze[n] = list(map(int, input()))

    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                S = [i, j]

    print('#{} {}'.format(TC, bfs(S)))
