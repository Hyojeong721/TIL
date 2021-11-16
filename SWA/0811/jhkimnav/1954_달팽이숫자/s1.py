import sys
sys.stdin = open('input.txt')

T = int(input())
dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]
for test_case in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    k = 1
    i = 0
    j = -1
    status = 0
    while k <= N*N:
        i = i + dy[status % 4]
        j = j + dx[status % 4]
        if 0 <= i < N and 0 <= j < N and arr[i][j] == 0:
            arr[i][j] = k
        else:
            i -= dy[status % 4]
            j -= dx[status % 4]
            status += 1
            continue
        k += 1


    print('#{}'.format(test_case))
    for i in range(N):
        for j in range(N):
            print(arr[i][j], end=' ')
        print()

