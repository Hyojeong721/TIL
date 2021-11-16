import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전
    arr90 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr90[i][j] = arr[N-1-j][i]
    # 0,0 0,1 0,2     2,0 1,0 0,0
    # 1,0 1,1 1,2     2,1 1,1 0,1
    # 2,0 2,1 2,2     2,2 1,2 0,2

    # 180도 회전
    arr180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr180[i][j] = arr[N-1-i][N-1-j]

    # 270도 회전
    arr270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr270[i][j] = arr[j][N-1-i]

    print('#{}'.format(tc))
    for i in range(N):
        print(''.join(map(str, arr90[i])), end=' ')
        print(''.join(map(str, arr180[i])), end=' ')
        print(''.join(map(str, arr270[i])), end='')
        print()