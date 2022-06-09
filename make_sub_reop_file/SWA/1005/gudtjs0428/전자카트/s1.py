import sys
sys.stdin = open('sample_input.txt')

# 순열 코드로 어떻게 구현하지


def get_least_sum(N, matrix, least_sum, sum_route=0, j=1):
    for i in range(N):
        while j < N:
            if not visited[i]:
                sum_route += matrix[j][i]
                visited[i] = 1
                j = i
                get_least_sum(N, matrix, least_sum, i)
            else:
                i += 1
            if sum(visited) == N - 1:
                sum_route += matrix[i][1]





T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    matrix = [[]]
    for _ in range(N):
        matrix.append([0] + list(map(int, input().split())))
    visited = [0] * (N + 1)
    least_sum = 0
    for i in range(1, N):
        least_sum += matrix[i][i+1]
    least_sum += matrix[N][1]
    # print('#{} {}'.format(test_case, get_least_sum(N, matrix, least_sum)))
    print(least_sum)
