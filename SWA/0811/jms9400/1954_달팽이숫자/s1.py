import sys
sys.stdin = open('input.txt')

T = int(input())


for tc in range(1, T + 1):
    n = int(input())

    print('#{}'.format(tc))

    arr = [[0] * n for _ in range(n)]
    score = 1

    dx = [0, 1, 0, -1] #우하좌상
    dy = [1, 0, -1, 0]
    k = 0
    x = 0
    y = -1

    while score <= (n * n):
        nx = x + dx[k%4]
        ny = y + dy[k%4]
        if nx in range(n) and ny in range(n) and arr[nx][ny] == 0:
            arr[nx][ny] = score
            score += 1
            x, y = nx, ny
        else:
            k += 1


    for i in range(n):
        for j in range(n):
            print(arr[i][j], end=" ")
        print()