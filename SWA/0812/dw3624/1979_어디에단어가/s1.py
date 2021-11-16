import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    n, k = map(int, input().split())
    mat = [list(map(int, input().split())) for _ in range(n)]
    for m in mat:
        m.insert(0, 0)
        m.append(0)
    mat.insert(0, [0] * len(mat[0]))
    mat.append([0] * len(mat[0]))

    blank = 0
    cnt_row = 0
    for row in range(len(mat)):
        for col in range(len(mat)):
            if mat[row][col] == 1:   # 해당 칸이 1인 경우
                if mat[row][col - 1] == 0:  # 왼쪽 칸이 0인 경우 (공백 시작)
                    blank = 1               # blank 1 추가
                elif mat[row][col + 1] == 0:    # 오른쪽 칸이 0인 경우 (공백 끝)
                    blank += 1                  # blank 1 추가
                    if blank == k:      # blank 크기가 k 인 경우
                        cnt_row += 1    # cnt_row 1 추가
                else:
                    blank += 1  # blank 1 추가

    blank = 0
    cnt_col = 0
    for col in range(len(mat)):
        for row in range(len(mat)):
            if mat[row][col] == 1:
                if mat[row - 1][col] == 0:
                    blank = 1
                elif mat[row + 1][col] == 0:
                    blank += 1
                    if blank == k:
                        cnt_col += 1
                else:
                    blank += 1

    result = cnt_row + cnt_col

    print('#{} {}'.format(t, result))