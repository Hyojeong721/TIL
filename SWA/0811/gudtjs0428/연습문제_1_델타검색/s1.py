# P8

import sys
sys.stdin = open('input.txt')

def abs_delta(matrix):
    abss = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            if j > 0:
                abss += abs(matrix[i][j] - matrix[i][j-1])
            if j < len(matrix[i]) - 1:
                abss += abs(matrix[i][j] - matrix[i][j+1])
            if i > 0:
                abss += abs(matrix[i][j] - matrix[i-1][j])
            if i < len(matrix) - 1:
                abss += abs(matrix[i][j] - matrix[i+1][j])
    return abss

T = int(input())
for tc in range(1, T + 1):
    n = int(input())
    matrix = [list(map(int, input().split())) for _ in range(n)]
    print('#{} {}'.format(tc, abs_delta(matrix)))