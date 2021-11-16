import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 90도 회전
    arr_90 = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_90[i][j] = arr[N-1-j][i]

    # 180도 회전
    arr_180 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_180[i][j] = arr[N-i-1][N-j-1]

    # 270도 회전
    arr_270 = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            arr_270[i][j] = arr[j][N-i-1]
    print(arr)
    print(arr_90)
    print(arr_180)
    print(arr_270)

