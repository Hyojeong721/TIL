n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []
visited = [False]*n


def dfs():
    global ans
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    overlap = 0
    for i in range(n):
        if not visited[i] and overlap != arr[i]:
            res.append(arr[i])
            overlap = arr[i]
            dfs()
            res.pop()

dfs()



