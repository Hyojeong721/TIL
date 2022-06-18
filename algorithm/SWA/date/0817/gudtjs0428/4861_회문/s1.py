import sys
sys.stdin = open('input.txt')

def if_circular(N, M, matrix):
    x = 0
    y = 0
    for i in range(N):
        for j in range(N - M + 1):
            check1 = 1      # 가로에 회문 존재시
            check2 = 1      # 세로에 회문 존재시
            k = 0
            while k < M//2:
                if matrix[i][j + k] == matrix[i][j + M - 1 - k]:
                    k += 1
                else:
                    check1 = 0
                    k = 0
                    break
            while k < M//2:
                if matrix[j + k][i] == matrix[j + M - 1 - k][i]:
                    k += 1
                else:
                    check2 = 0
                    k = 0
                    break
        if check1 == 1 or check2 == 1:
            x = j
            y = i
            break

    circular = ''
    if check1 == 1:
        for j in range(M):
            circular += matrix[y][x+j]
        return circular
    else:
        for i in range(M):
            circular += matrix[x+i][y]
        return circular


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    matrix = [input() for _ in range(N)]
    print('#{} {}'.format(tc, if_circular(N, M, matrix)))