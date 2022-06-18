import sys
sys.stdin = open("input.txt")


def dfs(i, j, cnt, temp):
    global res
    if cnt == 4:
        res = max(res, temp)
        return

    for dir in range(4):
        ni, nj = i + di[dir], j + dj[dir]
        if 0 <= ni < N and 0 <= nj < N and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, cnt+1, temp+arr[ni][nj])
            visited[ni][nj] = False

def exec():
    # ㅗ,ㅏ,ㅜ,ㅓ 탐색해야함.
    return



di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]
res = -1e9

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        visited[i][j] = True
        dfs(i, j, 1, arr[i][j])
        visited[i][j] = False

print(res)