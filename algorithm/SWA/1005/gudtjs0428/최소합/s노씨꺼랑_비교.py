import sys
sys.stdin = open('sample_input.txt')

def get_least_sum1(matrix, sums1, N, i, j, sum_route):

    sum_route += matrix[i][j]
    if i == N-1 and j == N-1:
        sums1.append(sum_route)
        return
    if j in range(N-1):
        j += 1
        get_least_sum1(matrix, sums1, N, i, j, sum_route)
        j -= 1
    if i in range(N-1):
        i += 1
        get_least_sum1(matrix, sums1, N, i, j, sum_route)
        i -= 1

def get_least_sum(matrix, sums, N, i, j, sum_route):

    sum_route += matrix[i][j]
    if i == N-1 and j == N-1:
        sums.append(sum_route)
        return
    if j in range(N-1):
        j += 1
        get_least_sum1(matrix, sums, N, i, j, sum_route)
        j -= 1
    if i in range(N-1):
        i += 1
        get_least_sum1(matrix, sums, N, i, j, sum_route)


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    sums1 = []
    sums = []

    get_least_sum1(matrix, sums1, N, 0, 0, 0)
    get_least_sum(matrix, sums, N, 0, 0, 0)
    print('#{} {}'.format(test_case,sums1))
    print('#{} {}'.format(test_case, sums))