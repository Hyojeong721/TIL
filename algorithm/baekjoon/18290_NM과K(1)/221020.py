#이 격자판에서 칸 K개를 선택할 것이고,
# 선택한 칸에 들어있는 수를 모두 더한 값의 최댓값을 구하려고 한다.
# 단, 선택한 두 칸이 인접하면 안된다.
N, M, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
res = 0
visited = [[False]*M for _ in range(N)]
di, dj = [-1, 1, 0, 0], [0, 0, -1, 1]

def dfs(now, choice, temp, inject):
    global visited, res
    print(now, choice, temp, inject, res)

    if len(choice) == K:
        res = max(temp, res)
        return

    for k in range(4):
        ni, nj = now[0] + di[k], now[1] + dj[k]
        if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
            visited[ni][nj] = True
            inject.append((ni, nj))

    for i in range(now[0], N):
        for j in range(M):
            if (i, j) not in choice and not visited[i][j]:
                visited[i][j] = True
                choice.append((i, j))
                dfs((i, j), choice, temp+arr[i][j], inject)
                choice.pop()

                for inj in inject:
                    x, y = inj[0], inj[1]
                    visited[x][y] = False
                inject.clear()

dfs((0, 0), [(0, 0)], arr[0][0], [])
print(res)