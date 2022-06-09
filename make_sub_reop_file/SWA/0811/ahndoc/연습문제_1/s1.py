import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    total = 0
    print(arr)

    for i in range(N):
        for j in range(N):
            for dr , dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:    # 0:우 / 1:하 / 2:좌 / 3:상
                ni = i + dr
                nj = j + dc
                if 0 <= ni < N and 0 <= nj < N:
                    value = arr[i][j] - arr[ni][nj]
                    if value < 0:
                        value = (-1) * value
                    total += value

    print('#{} {}'.format(test_case, total))

