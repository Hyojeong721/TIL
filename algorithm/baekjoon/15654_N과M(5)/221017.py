n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def dfs():
    if len(res) == m:
        print(*res)
        return

    for num in arr:
        if num not in res:
            res.append(num)
            dfs()
            res.pop()

dfs()


