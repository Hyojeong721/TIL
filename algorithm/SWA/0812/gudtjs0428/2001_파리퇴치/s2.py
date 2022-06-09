import sys
sys.stdin = open('input.txt')

def most_total(N, M, matrix):
    i = j = n = m = 0
    max_total = 0
    total = 0
    while i < N - M + 1:
        while j < N - M + 1:
            while n < M:
                while m < M:
                    total += matrix[i+n][j+m]
                    m += 1
                m = 0
                n += 1
            if total > max_total:
                max_total = total
            total = 0
            n = 0
            j += 1
        j = 0
        i += 1
    return max_total


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(test_case, most_total(N, M, matrix)))