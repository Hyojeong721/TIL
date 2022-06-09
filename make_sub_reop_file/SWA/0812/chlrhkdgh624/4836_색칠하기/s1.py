import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    matrix = [[0] * 10 for _ in range(10)]
    N = int(input())
    colors = []
    for i in range(N):
        info = list(map(int, input().split()))
        colors.append(info)

    for color in colors:
        for row in range(color[0], color[2] + 1):
            for col in range(color[1], color[3] + 1):
                if matrix[row][col] == color[4]:
                    pass
                else:
                    matrix[row][col] += color[4]

    purple = 0
    for i in range(10):
        for j in range(10):
            if matrix[i][j] == 3:
                purple += 1

    print(f'#{tc} {purple}')

