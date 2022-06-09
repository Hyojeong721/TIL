import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    mat = [[0] * 10 for _ in range(10)]
    n = int(input())

    # 빈 matrix 생성
    colors = [list(map(int, input().split())) for _ in range(n)]

    for color in colors:
        for row in range(color[0], color[2] + 1):
            for col in range(color[1], color[3] + 1):
                mat[row][col] += color[4]

    # 보라색(값이 3)인 요소 탐색 및 카운팅
    purple = 0
    for mat_row in mat:
        for m in mat_row:
            if m == 3:
                purple += 1

    print('#{} {}'.format(t, purple))