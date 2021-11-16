import sys
sys.stdin = open('input.txt')

def get_most(N, M, matrix):
    totals = []
    for r in range(N-M+1):
        for c in range(N-M+1):
            total = 0
            for j in range(M):
                for k in range(M):
                    total += matrix[r+j][c+k]
            totals.append(total)

    return max(totals)


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = []
    for _ in range(N):
        matrix.append(list(map(int, input().split())))
    print('#{} {}'.format(tc, get_most(N, M, matrix)))