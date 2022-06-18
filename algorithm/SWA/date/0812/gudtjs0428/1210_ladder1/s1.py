import sys
sys.stdin = open('input.txt')

def get_start_point(matrix):
    for i in range(100):
        if matrix[99][i] == 2:
            x = i

    for i in range(98, -1, -1):
        j = 1
        if x != 0 and matrix[i][x-j] == 1:
            while x != 0 and x-j >= 0 and matrix[i][x-j] == 1:
                j += 1
            x -= j - 1
        elif x != 99 and matrix[i][x+j] == 1:
            while x != 99 and x+j <= 99 and matrix[i][x+j] == 1:
                j += 1
            x += j - 1
        matrix[i][x] = 2

    for i in range(100):
        if matrix[0][i] == 2:
            return i

T = 10
for tc in range(1, T + 1):
    input()
    matrix = []
    for i in range(100):
        matrix.append(list(map(int, input().split())))
    print('#{} {} '.format(tc, get_start_point(matrix)))