import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    matrix = []
    result = 1
    for i in range(9):
        matrix.append(list(map(int, input().split())))

    for i in matrix:
        check = [0] * 10
        for j in i:
            check[j] += 1
        if max(check) > 1:
            result = 0

    for i in range(9):
        check = [0] * 10
        for j in range(9):
            check[matrix[j][i]] += 1
        if max(check) > 1:
            result = 0

    for i in range(0, 7, 3):
        check = [0] * 10
        for a in range(3):
            for b in range(3):
                check[matrix[i+a][i+b]] += 1
        if max(check) > 1:
            result = 0

    print('#{0} {1}'.format(tc, result))

