import sys
sys.stdin = open('input.txt')

T = int(input())

def sudoku(mat):
    for i in range(9):
        row = [0] * 10
        col = [0] * 10

        for j in range(9):
            num_row = mat[i][j]   # 행 검사
            num_col = mat[j][i]   # 열 검사

            if row[num_row]: return 0
            if col[num_col]: return 0

            row[num_row] = 1
            col[num_col] = 1

            ##################
            # 3 * 3 검사
            if i % 3 == 0 and j % 3 == 0:
                sqr = [0] * 10
                for k in range(i, i+3):
                    for l in range(j, j+3):
                        num_sqr = mat[k][l]
                        if sqr[num_sqr]: return 0
                        sqr[num_sqr] = 1
    return 1

for t in range(1, T+1):
    mat = [list(map(int, input().split())) for _ in range(9)]
    result = sudoku(mat)

    print('#{} {}'.format(t, result))
