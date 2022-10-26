#이 격자판에서 칸 K개를 선택할 것이고,
# 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다.
# 단, 선택한 두 칸이 인접하면 안된다.
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]
res = -10000

def dfs(cnt, x, y, temp):
    global res, visited
    if cnt == K:
        res = max(res, temp)
        return

    for i in range(x, N):
        for j in range(y if i == x else 0, M):
            if visited[i][j]:
                continue
            ok = True

            for k in range(4):
                ni, nj = i+di[k], j+dj[k]
                if 0 <= ni < N and 0 <= nj < M:
                    if visited[ni][nj]:
                        ok = False

            if ok:
                visited[i][j] = True
                # print(cnt+1, i, j, temp+arr[i][j])
                dfs(cnt+1, i, j, temp+arr[i][j])
                visited[i][j] = False

dfs(0, 0, 0, 0)
print(res)