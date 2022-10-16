
n, m = map(int, input().split())
arr = list(map(int, input().split()))


res = []
ans = []

def dfs(start):
    if len(res) == m:
        print(*res)
        ans.append(res)
        return

    for i in range(start, n):
        # print(res, i)
        res.append(arr[i])
        dfs(i)
        res.pop()

arr.sort()
dfs(0)
