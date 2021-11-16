import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n, m = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]

    fly_sums = []
    row, col = 0, 0
    for i in range(n - m + 1):
        for j in range(n - m + 1):
            tmp = 0
            for k1 in range(m):
                for k2 in range(m):
                    tmp += mat[i+k1][j+k2]
            fly_sums.append(tmp)

    total = 0
    for f in range(len(fly_sums)):
        if fly_sums[f] > total:
            total = fly_sums[f]

    print('#{} {}'.format(t, total))