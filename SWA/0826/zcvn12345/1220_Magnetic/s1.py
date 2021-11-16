import sys
sys.stdin = open('input.txt')


T = 10

for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            y = 0 + i
            if mat[y][j] == 1:
                while y < N:
                    if mat[y][j] != 2:
                        mat[y][j] = 1
                        y += 1
                    else:
                        break
            elif mat[y][j] == 2:
                while y > -1:
                    if mat[y][j] != 1:
                        mat[y][j] = 2
                        y -= 1
                    else:
                        break

    count = 0
    for i in range(N-1):
        for j in range(N):
            if mat[i][j] == 1 and mat[i+1][j] == 2:
                count += 1

    print('#{0} {1}'.format(tc, count))
