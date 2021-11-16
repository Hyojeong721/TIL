import sys
sys.stdin = open('input.txt')

def snail(N):
    """
    N * N 격자를 시계방향으로 돌며 채운 결과를 출력 후, 1 반환

    """
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]
    k = 0
    cnt = 1
    i, j = 0, -1
    mat = [[0] * N for _ in range(N)]

    while cnt <= N * N:
        ni, nj = i + di[k], j + dj[k]
        if 0 <= ni < N and 0 <= nj < N and mat[ni][nj] == 0:
            mat[ni][nj] = cnt
            cnt += 1
            i, j = ni, nj
        else:
            k = (k + 1) % 4

    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=' ')
        print()

    return 1

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    snail(N)
