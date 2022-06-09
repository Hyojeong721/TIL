import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    n = int(input())
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    data = [[0] * n for _ in range(n)]

    curR = 0
    curC = 0
    value = 1
    mode = 0
    while value <= n * n:
        data[curR][curC] = value
        newR = curR + dy[mode]
        newC = curC + dx[mode]
        if new