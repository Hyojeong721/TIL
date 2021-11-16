import sys
sys.stdin = open('input.txt')

def snail_nums(N, matrix, x=0, y=0, n=0):
    # 일케하면 안되쥬 ㅋㅋ
    while n < N ** 2 + 1:
        if n == N ** 2:
            return matrix
        try:
            if matrix[y][x] == 0:
                n += 1
                matrix[y][x] = n
                x += 1
            else:
                x += 1
        except:
            try:
                x -= 1
                if matrix[y][x] == 0:
                    n += 1
                    matrix[y][x] = n
                    y += 1
                else:
                    y += 1
            except:
                try:
                    x -= 1
                    if matrix[y][x]:
                        n += 1
                        matrix[y][x] = n
                        x -= 1
                    else:
                        x -= 1
                except:
                    try:
                        x += 1
                        if matrix[y][x] == 0:
                            n += 1
                            matrix[y][x] = n
                            y -= 1
                        else:
                            snail_nums(N, x, y, n)
                    except:
                        snail_nums(N, x, y, n)

    # for n in range(N ** 2):
    #     if n < len(matrix[0]):
    #         matrix[0][n] = n + 1
    #     elif n -(len(matrix[0]) - 1)< len(matrix[-1]) - 1:
    #         matrix[i][-1] = n

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    print('#{}'.format(tc))
    matrix = [[0] * N for _ in range(N)]
    for row in snail_nums(N, matrix):
        for n in row:
            print(n, end=' ')
        print()