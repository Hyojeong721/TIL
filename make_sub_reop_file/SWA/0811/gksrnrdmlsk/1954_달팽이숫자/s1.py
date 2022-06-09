import sys
sys.stdin = open('input.txt')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

T = int(input())
for tc in range(1, T + 1):
    k = 0
    N = int(input())
    lst = [[0] * N for _ in range(N)]
    i = 0
    j = -1
    cnt = 0
    while cnt < N * N:
        if 0 <= i + dx[k] <= N -1 and 0 <= j + dy[k] <= N -1 and lst[i + dx[k]][j + dy[k]] == 0:
            cnt += 1
            lst[i + dx[k]][j + dy[k]] = cnt
            i = i + dx[k]
            j = j + dy[k]
        else:
            k = (k + 1) % 4

    print('#{}'.format(tc))
    for idx in range(N):
        print(' '.join(list(map(str, lst[idx]))))
