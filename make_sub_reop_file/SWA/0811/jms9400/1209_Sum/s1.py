import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T + 1):

    n = int(input())

    arr = [list(map(int, input().split())) for _ in range(100)]

    # total 1 가로, total2 세로, total3 대각선 (왼쪽위에서 오른쪽아래), total4 대각선(오른쪽위에서 왼쪽아래)
    result = 0
    total3 = 0
    total4 = 0

    for i in range(100):
        total1 = 0
        total2 = 0
        for j in range(100):
            total1 += arr[i][j]
            total2 += arr[j][i]
            if i == j:
                total3 += arr[i][j]
            elif i + j == 99:
                total4 += arr[i][j]
        if total1 > result:
            result = total1
        if total2 > result:
            result = total2
    if total3 > result:
        result = total3
    if total4 > result:
        result = total4

    print('#{} {}'.format(n, result))