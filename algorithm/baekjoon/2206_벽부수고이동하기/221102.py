import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().rstrip())) for _ in range(N)]
res = -1
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
visited = [[[0]*2 for _ in range(M)] for _ in range(N)]

que = deque()
que.append((0, 0, 0))
visited[0][0][0] = 1

def isrange(i, j):
    if 0<=i<N and 0<=j<M:
        return True
    return False

def dfs():
    while que:
        i, j, w = que.popleft()
        if i == N-1 and j == M-1:
            return visited[i][j][w]

        for k in range(4):
            ni, nj = i+di[k], j+dj[k]

            if isrange(ni, nj):
                # 이동가능한 곳, 방문한적 없는 곳
                if arr[ni][nj] == 0 and visited[ni][nj][w] == 0:
                    visited[ni][nj][w] = visited[i][j][w] + 1
                    que.append((ni, nj, w))
                # 벽을 안부스고 온 경우, 벽이고
                elif arr[ni][nj] == 1 and w == 0:
                    visited[ni][nj][w+1] = visited[i][j][w] + 1
                    que.append((ni, nj, w+1))
    return -1
print(dfs())

# dfs 내부 while문을 함수 안에 안 넣고 그냥 밖에서 돌리면 시간 초과나고
# 내부에 넣고 돌리면 통과하는 마법