import sys
sys.stdin = open('input.txt')


dx = [1, 0]   # 하
dy = [0, 1]   # 우

def dfs(x, y, total):

    for i in range(2):
        cx = x + dx[i]
        cy = y + dy[i]

        if x > N-1 or y > N-1:   # 범위 넘어가면 패스
            pass

        elif not visited[y][x]:   # 방문체크
            visited[y][x] = 1
            dfs(cx, cy, total+board[y][x])
            visited[y][x] = 0

    global result
    if x == N-1 and y == N-1:   # 도착한 경우
        total += board[y][x]

        if total < result:
            result = total
            return



T = int(input())
for tc in range(1, T+1):
    N = int(input())

    board = [list(map(int, input().split())) for _ in range(N)]
    visited = [[0 for _ in range(N)]for _ in range(N)]

    result = 99999999
    dfs(0, 0, 0)

    print('#{} {}'.format(tc, result))
