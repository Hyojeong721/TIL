N = int(input())
arr = list(map(int, input().split()))
visited = dict()

for k in range(N):
    visited[arr[k]] = False

res = []
def dfs(temp):
    global res
    if len(res) == N:
        print(*res)
        return

    if temp*2 in arr and not visited[temp*2]:
        res.append(temp*2)
        visited[temp*2] = True
        dfs(temp*2)
        res.pop()
        visited[temp*2] = False

    if temp % 3 == 0:
       if temp//3 in arr and not visited[temp//3]:
        res.append(temp//3)
        visited[temp//3] = True
        dfs(temp // 3)
        res.pop()
        visited[temp//3] = False

for i in range(N):
    res.append(arr[i])
    visited[arr[i]] = True
    dfs(arr[i])
    visited[arr[i]] = False
    res.pop()

