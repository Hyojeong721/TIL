import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    answer = 0
    N = int(input())
    arr = [[0] * N for i in range(N)]
    for i in range(N):
        arr[i] = list(map(int, input().split()))

    # 상 우 하 좌
    dx = [0, 1, 0, -1]
    dy = [-1, 0, 1, 0]

    for i in range(N):
        for j in range(N):
            for k in range(4):
                ni = i + dy[k]
                nj = j + dx[k]
                if ni >= 0 and ni < N and nj >= 0 and nj < N:
                    answer += abs(arr[i][j] - arr[ni][nj])

    print('#{} {}'.format(test_case, answer))
