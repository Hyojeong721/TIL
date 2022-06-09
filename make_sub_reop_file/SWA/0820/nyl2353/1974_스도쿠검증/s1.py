import sys
sys.stdin = open('input.txt')


def is_sudoku(mat):
    """
    스도쿠가 맞으면 1, 아니면 0을 반환하는 함수

    :param mat: 1~9 범위의 정수로 이뤄진 9x9 배열
    :return: boolean
    """
    for i in range(9):
        row = [0] * 10
        col = [0] * 10
        for j in range(9):
            # 가로 검사
            if row[mat[i][j]]:
                return 0
            row[mat[i][j]] = 1

            # 세로 검사
            if col[mat[j][i]]:
                return 0
            col[mat[j][i]] = 1

            # 3x3 검사
            if not i % 3 and not j % 3:
                square = [0] * 10
                for r in range(i, i + 3):
                    for c in range(j, j + 3):
                        if square[mat[r][c]]:
                            return 0
                        square[mat[r][c]] = 1

    return 1


T = int(input())
for tc in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{0} {1}'.format(tc, is_sudoku(sudoku)))