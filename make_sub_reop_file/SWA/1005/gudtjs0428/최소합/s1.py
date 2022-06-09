import sys
sys.stdin = open('sample_input.txt')

def get_least_sum(matrix, N, least_sum, i=0, j=0, sum_route=0):
    sum_route += matrix[i][j]
    if sum_route > least_sum:
        return sum_route
    if i == N-1 and j == N-1:
        if sum_route < least_sum:
            return sum_route
    if j != N-1:
        j += 1
        least_sum = get_least_sum(matrix, N, least_sum, i, j, sum_route)
        j -= 1
    if i != N-1:
        i += 1
        least_sum = get_least_sum(matrix, N, least_sum, i, j, sum_route)
    return least_sum


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    least_sum = 0
    for i in range(N):
        least_sum += matrix[0][i]
    for i in range(N):
        least_sum += matrix[i][N-1]
    least_sum -= matrix[0][N-1]
    least_sum = get_least_sum(matrix, N, least_sum)
    print('#{} {}'.format(test_case, least_sum))