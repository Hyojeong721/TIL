import sys
sys.stdin = open('input.txt')

# 비효율적.. 수업때 가르쳐주신게 매우 효율적

def if_sudoku(sudoku):
    for i in range(9):
        stack = []
        for j in range(9):
            if sudoku[i][j] not in stack:
                stack.append(sudoku[i][j])
            else:
                return 0
        stack = []
        for j in range(9):
            if sudoku[j][i] not in stack:
                stack.append(sudoku[j][i])
            else:
                return 0
        stack = []

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            stack = []
            for k in range(3):
                for l in range(3):
                    if sudoku[i+k][j+l] not in stack:
                        stack.append(sudoku[i+k][j+l])
                    else:
                        return 0
            stack = []
    return 1

T = int(input())
for test_case in range(1, T + 1):
    sudoku = [list(map(int, input().split())) for _ in range(9)]
    print('#{} {}'.format(test_case, if_sudoku(sudoku)))