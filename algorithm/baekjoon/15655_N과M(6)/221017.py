n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def dfs(s):
    if len(res)==m:
        print(*res)
        return

    for i in range(s, n):
        res.append(arr[i])
        dfs(i+1)
        res.pop()

dfs(0)