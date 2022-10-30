n, m = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
res = []

def dfs(s):
    global ans
    if len(res) == m:
        print(' '.join(map(str, res)))
        return

    overlap = 0
    for i in range(s, n):
        if overlap != arr[i]:
            res.append(arr[i])
            overlap = arr[i]
            dfs(i)
            res.pop()

dfs(0)



