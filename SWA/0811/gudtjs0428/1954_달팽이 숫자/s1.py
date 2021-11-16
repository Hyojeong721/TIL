import sys
sys.stdin = open('input.txt')

def snail_nums(N):
    matrix = [[0] * N for _ in range(N)]
    i = 0
    j = 0
    min_row = 0
    min_col = 0
    max_row = N
    max_col = N
    n = 1
    while n <= N ** 2:
        while j < max_col and n < N ** 2 + 1:
            matrix[i][j] = n
            j += 1
            n += 1
        min_row += 1
        i += 1
        j -= 1
        while i < max_row and n < N ** 2 + 1:
            matrix[i][j] = n
            i += 1
            n += 1
        max_col -= 1
        i -= 1
        j -= 1
        while j >= min_col and n < N ** 2 + 1:
            matrix[i][j] = n
            j -= 1
            n += 1
        max_row -= 1
        j += 1
        i -= 1
        while i >= min_row and n < N ** 2 + 1:
            matrix[i][j] = n
            i -= 1
            n += 1
        min_col += 1
        i += 1
        j += 1

    return matrix

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    print('#{}'.format(test_case))
    for row in snail_nums(N):
        for n in row:
            print(n, end=' ')
        print()