import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    arr = [[0] + list(map(int, input().split())) + [0] for _ in range(N)]
    arr.insert(0, [0]*(N+2))
    arr.append([0]*(N+2))

    row = 0
    for i in range(1, N+2):
        count = 1
        for j in range(1, N+2):
            if arr[i][j] == 1:
                if arr[i][j] == arr[i][j-1]:
                    count += 1
            else:
                if count == K:
                    row += 1
                    count = 1
                else:
                    count = 1

    col = 0

    for j in range(1, N+2):
        count = 1
        for i in range(1, N+2):
            if arr[i][j] == 1:
                if arr[i][j] == arr[i-1][j]:
                    count += 1
            else:
                if count == K:
                    col += 1
                    count = 1
                else:
                    count = 1

    print(f'#{tc} {row+col}')







