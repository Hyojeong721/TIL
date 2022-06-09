import sys
sys.stdin = open('input.txt')

dr = [0, 1]
dc = [1, 0]

def find(r, c, cursum):
    global ans

    if cursum > ans:
        return

    if (r, c) == (N-1, N-1):
        if ans > cursum:
            ans = cursum
        return

    for i in range(2):
        nr = r + dr[i]
        nc = c + dc[i]

        if 0 <= nr < N and 0 <= nc < N:
            find(nr, nc, cursum + arr[nr][nc])


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    ans = N * N * 10
    c = arr[0][0]
    find(0, 0, c)
    print('#{} {}'.format(tc, ans))