import sys
sys.stdin = open('input.txt')


N = int(input())
x, y = map(int, input().split())
visited = [False] * (N+1)
M = int(input())
arr = [[] for _ in range(N+1)]

for m in range(M):
    fa, son = map(int, input().split())
    arr[fa].append(son)
    arr[son].append(fa)

res = -1

def dfs(a, y, cnt):
    global res
    if a == y:
        res = cnt+1
        return

    for k in arr[a]:
        if not visited[k]:
            visited[k] = True
            dfs(k, y, cnt+1)

dfs(x, y, 0)
if res != -1:
    print(res-1)
else:
    print(res)