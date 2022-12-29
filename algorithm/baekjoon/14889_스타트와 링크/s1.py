def dfs(cnt, idx):
    global res
    if cnt == N//2:
        power1 = 0
        power2 = 0
        for i in range(N):
            for j in range(N):
                if visited[i] and visited[j]:
                    power1 += arr[i][j]
                elif not visited[i] and not visited[j]:
                    power2 += arr[i][j]
        res = min(abs(power1-power2), res)
        return

    for i in range(idx, N):
        if not visited[i]:
            visited[i] = True
            dfs(cnt+1, i+1)
            visited[i] = False

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [False]*(N)
res = 1e9

dfs(0, 0)
print(res)