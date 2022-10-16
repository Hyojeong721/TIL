
n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

res = []

def dfs():
    if len(res) == m:
        print(*res)
        return

    for i in range(n):
        # print(res, i)
        res.append(arr[i])
        dfs()
        res.pop()

dfs()
