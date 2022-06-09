import sys
sys.stdin = open("input.txt")


def rotate_board(board, N):
    """
    인자로 들어온 2차원 배열을 시계 방향으로 90도 회전시킨 새 배열을 반환한다.

    Args:
        board: 회전시킬 2차원 배열
        N : 2차원 배열의 길이
    Returns:
        new_board: 시계 방향으로 90도 회전시킨 2차원 배열
    """
    new_board = []

    for c in range(N):
        sub_board = []

        for r in range(N - 1, -1, -1):
            sub_board.append(board[r][c])

        new_board.append(sub_board)

    return new_board


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = []

    for _ in range(N):
        board.append([str(x) for x in input().split()])

    total = [[] for _ in range(N)]

    # 각각 90도, 180도, 270도 회전한 배열을 board에 저장하여 출력한다.
    for _ in range(3):
        board = rotate_board(board, N)
        for i, sub_board in enumerate(board):
            total[i].append(''.join(sub_board))

    print("#{}".format(tc))

    for x in total:
        print(" ".join(x))

