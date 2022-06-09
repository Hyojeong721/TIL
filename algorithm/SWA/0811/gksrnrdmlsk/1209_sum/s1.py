import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    lst = [list(map(int, input().split())) for _ in range(100)]
    result_lst = []
    for i in range(100):
        total = 0
        for j in range(100):
            total += lst[i][j]
        result_lst.append(total)

    for i in range(100):
        total = 0
        for j in range(100):
            total += lst[j][i]
        result_lst.append(total)

    total = 0
    for k in range(100):
        total += lst[0 + k][0 + k]
    result_lst.append(total)

    total = 0
    for l in range(100):
        total += lst[0 + l][99 - l]
    result_lst.append(total)

    print('#{} {}'.format(tc, max(result_lst)))