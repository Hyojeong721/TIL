import sys
sys.stdin = open('input.txt')

dx = [0, 1]
dy = [1, 0]

def dfs(x, y):
    global res, tmp
    if res < tmp:
        return
    if x == n-1 and y == n-1:
        res = tmp
        return
    for d in range(2):
        nx = x + dx[d]
        ny = y + dy[d]
        if nx < 0 or nx >= n or ny < 0 or ny >= n:
            continue
        if (nx, ny) not in visited:
            visited.append((nx, ny))
            tmp += arr[nx][ny]
            dfs(nx, ny)
            tmp -= arr[nx][ny]
            visited.remove((nx, ny))

T = int(input())
for tc in range(1, T+1):
    n = int(input())
    arr = [list(map(int,input().split())) for _ in range(n)]
    visited = []
    res = 987654321
    tmp = arr[0][0]
    dfs(0,0)
    print("#{} {}".format(tc, res))