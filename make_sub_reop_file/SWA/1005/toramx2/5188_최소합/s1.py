import sys
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if i == 0 and j == 0:
                continue
            elif i == 0:
                arr[i][j] += arr[i][j-1]
            elif j == 0:
                arr[i][j] += arr[i-1][j]
            else:
                arr[i][j] += min(arr[i][j-1], arr[i-1][j])

    print('#{} {}'.format(test_case, arr[N-1][N-1]))