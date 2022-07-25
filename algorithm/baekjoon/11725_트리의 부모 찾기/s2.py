import sys
from collections import deque
sys.stdin = open("input.txt")


N = int(input())
arr = [[] for _ in range(N+1)]
visited = [0 for _ in range(N+1)]
visited[1] = 1
que = deque()

for _ in range(N-1):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)
# print(arr)
que.append(1)
def bfs():
    while que:
        now = que.popleft()
        for x in arr[now]:
            if visited[x] == 0 :
                visited[x] = now
                que.append(x)
        print(que)

bfs()

# print("=======")
for k in range(2, N+1):
    print(visited[k])
