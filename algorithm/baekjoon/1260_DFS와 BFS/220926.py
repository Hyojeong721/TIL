import sys
sys.stdin = open('input.txt')
from collections import deque

#정점 N, 간선 M, 구할 점 V
N, M, V = map(int, input().split())
arr = [[] for i in range(N+1)]
visited = [ False for _ in range(N+1)]
visited_bfs = [ False for _ in range(N+1)]

def dfs(i):
    for v in arr[i]:
        if not visited[v]:
            print(v, end = ' ')
            visited[v] = True
            dfs(v)

def bfs(i):
    que = deque()
    que.append(i)
    while que:
        now = que.popleft()
        if not visited_bfs[now]:
            print(now, end= ' ')
            visited_bfs[now] = True
            for k in arr[now]:
                que.append(k)

# 간선 정보 입력
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
    arr[a].sort()
    arr[b].sort()


# 모든 점 돌기

if not visited[V]:
    visited[V] = True
    print(V, end=' ')
    dfs(V)
print()
if not visited_bfs[V]:
    bfs(V)