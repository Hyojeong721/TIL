import sys
sys.stdin = open("input.txt")


def check_sudoku(board):
    """스도쿠 배열을 인자로 받아, 유효한지 검사한다.

    Args:
        board: 스도쿠 숫자 (9 X 9 크기의 2차원 배열)
    Returns:
        스도쿠 배열이 유효하면 True, 아니면 False
    """
    sudoku_set = {1, 2, 3, 4, 5, 6, 7, 8, 9}

    # 1. 가로 검사
    for x in board:
        if set(x) != sudoku_set:
            return False

    # 2. 세로 검사
    for c in range(9):
        numbers = set()
        for r in range(9):
            numbers.add(board[r][c])

        if numbers != sudoku_set:
            return False

    # 3. 3 X 3 격자 검사
    for r in range(0, 9, 3):
        for c in range(0, 9, 3):
            numbers = set()

            for i in range(r, r + 3):
                for j in range(c, c + 3):
                    numbers.add(board[i][j])

            if numbers != sudoku_set:
                return False

    return True


T = int(input())

for tc in range(1, T + 1):
    board = []

    for _ in range(9):
        board.append([int(x) for x in input().split()])

    print("#{} {}".format(tc, int(check_sudoku(board))))
