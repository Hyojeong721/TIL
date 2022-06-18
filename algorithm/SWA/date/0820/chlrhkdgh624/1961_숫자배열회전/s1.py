import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # import given matrix
    N = int(input())
    numbers_90 = []
    for _ in range(N):
        numbers_90.extend(list(map(int, input().split())))
    numbers_180 = numbers_90[:]
    numbers_270 = numbers_90[:]

    matrix_90 = [[0]*N for i in range(N)]
    matrix_180 = [[0] * N for i in range(N)]
    matrix_270 = [[0] * N for i in range(N)]

    # 90 degree rotation
    for col in range(N-1, -1, -1):
        for row in range(N):
            matrix_90[row][col] = numbers_90.pop(0)

    # 180 degree rotation
    for row in range(N-1, -1, -1):
        for col in range(N-1, -1, -1):
            matrix_180[row][col] = numbers_180.pop(0)

    # 270 degree rotation
    for col in range(N):
        for row in range(N-1, -1, -1):
            matrix_270[row][col] = numbers_270.pop(0)

    print(f'#{tc}')
    for i in range(N):
        print(''.join(map(str, matrix_90[i])), end=' ')
        print(''.join(map(str, matrix_180[i])), end=' ')
        print(''.join(map(str, matrix_270[i])))





