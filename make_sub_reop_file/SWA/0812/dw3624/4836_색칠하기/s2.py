import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    N = int(input())
    mat = [[0] * 10 for _ in range(10)]   # 빈 리스트 생성
    colors = [list(map(int, input().split())) for _ in range(N)]
    # print(colors)


    for color in colors:
        r1, r2 = color[0], color[2]
        c1, c2 = color[1], color[3]
        col = color[4]

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                if mat[i][j] != col and mat[i][j] != 3: # 색이 중복되지 않으며 보라가 아닌경우
                    mat[i][j] += col
    # print(mat)


    cnt = 0
    for row in range(10):
        for col in range(10):
            if mat[row][col] == 3:
                cnt += 1

    print('#{} {}'.format(t, cnt))