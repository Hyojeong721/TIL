import sys
sys.stdin = open("input.txt")

# 시간초과를 위한 설정
sys.setrecursionlimit(5000)
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [[] for _ in range(N+1)]
visited = [False] * (N+1)

def dfs(start, depth):

    visited[start] = True

    for i in arr[start]:
        if not visited[i]:
            dfs(i, depth+1)

# 연결 그림 그리기
for _ in range(M):
    a, b = map(int, input().split())
    arr[a].append(b)
    arr[b].append(a)

cnt = 0

for i in range(1, N+1):
    if not visited[i]:
        if not arr[i]:
            visited[i] = True
            cnt += 1
        else:
            dfs(i, 0)
            cnt += 1
print(cnt)

