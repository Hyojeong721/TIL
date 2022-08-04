import sys
sys.stdin = open("input.txt")
from collections import deque

n = int(input())
a, b= map(int, input().split())
m = int(input())
arr = [[] for _ in range(n+1)]

for _ in range(m):
    bu, ja = map(int, input().split())
    arr[ja].append(bu)
    arr[bu].append(ja)

visited = [0]*(n+1)

def bfs(node):
    que = deque()
    que.append(node)
    while que:
        now = que.popleft()
        for n in arr[now]:
            if visited[n] == 0:
                visited[n] = visited[now]+1
                que.append(n)


bfs(a)
if visited[b] != 0:
    print(visited[b])
else:
    print(-1)

