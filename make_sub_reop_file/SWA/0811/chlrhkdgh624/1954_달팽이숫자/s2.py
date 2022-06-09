import sys
sys.stdin = open('input.txt')

T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())

    arr = [[0]*N for _ in range(N)]
    i = 0
    j = 0
    num = 1
    d = 0

    while num <= N**2:
        arr[i][j] = num

        next_i = i + dy[d]
        next_j = j + dx[d]

        if next_i < 0 or next_i >= N or next_j < 0 or next_j >= N or arr[next_i][next_j]:
            d = (d+1) % 4

        num += 1

        i += dy[d]
        j += dx[d]

    print(f'#{tc}')
    for i in range(N):
        for j in arr[i]:
            print(j, end=' ')
        print()


