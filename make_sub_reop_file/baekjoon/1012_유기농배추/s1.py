import sys
from collections import deque
sys.stdin = open('input.txt')
# 최소의 배추흰지렁이 마리수 출력

def bfs(graph, m, n):
    que = deque()
    que.append((m, n))
    graph[m][n] = 0
    dx = [0, 0, -1, 1]
    dy = [1, -1, 0, 0]

    while que:
        x, y = que.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= M or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                que.append((nx, ny))

    return




T = int(input()) #테스트 케이스 갯수

for tc in range(T):
    # M*N 가로*세로 길이 / K는 배추 갯수
    M, N, K = map(int, input().split())
    cnt = 0
    graph = [[0]*N for _ in range(M)]
    # 배추 있는 자리 1로 채움
    for i in range(K):
        x, y = map(int, input().split())
        graph[x][y] = 1
    print(graph)
    for m in range(M):
        for n in range(N):
            if graph[m][n] == 1:
                bfs(graph, m, n)
                cnt += 1

    print(cnt)