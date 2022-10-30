n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []
visited = [False]*n


def dfs(s):
    if len(res) == m:
        print(*res)
        return

    for i in range(s, n):
        if not visited[i]:
            res.append(arr[i])
            dfs(i)
            visited[i] = True
            res.pop()
            visited[i] = False

dfs(0)