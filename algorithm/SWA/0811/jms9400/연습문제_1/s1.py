import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    total = 0

    for i in range(n):
        for j in range(n):
            a = i - 1
            b = i + 1
            c = j - 1
            d = j + 1
            if a in range(n):
                total += abs(arr[i][j] - arr[a][j])
            if b in range(n):
                total += abs(arr[i][j] - arr[b][j])
            if c in range(n):
                total += abs(arr[i][j] - arr[i][c])
            if d in range(n):
                total += abs(arr[i][j] - arr[i][d])

    print('#{} {}'.format(tc, total))