import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0]*10 for _ in range(10)]
    info = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    n = 0
    # n은 색칠 영역
    for n in range(N):
        for row in range(info[n][0], info[n][2]+1):
            for col in range(info[n][1], info[n][3] + 1):
                arr[row][col] += info[n][4]


    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] == 3:
                result += 1


    print('#{} {}'.format(tc, result))
