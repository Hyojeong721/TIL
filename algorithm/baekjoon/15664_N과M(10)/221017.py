from collections import deque

n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []
visited = [False]*n
ans = deque()

def dfs(s):
    global ans
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    overlap = 0
    for i in range(s, n):
        if not visited[i] and overlap != arr[i]:
            res.append(arr[i])
            visited[i] = True
            overlap = arr[i]
            dfs(i+1)
            visited[i] = False
            res.pop()

dfs(0)



