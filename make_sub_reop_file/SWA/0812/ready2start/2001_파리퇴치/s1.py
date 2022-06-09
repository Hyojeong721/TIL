import sys
sys.stdin = open("input.txt")


def get_accumulate(board, N):
    """
    주어진 2차원 배열(board)와 행과 열의 수가 같으며,
    board[0][0]을 왼쪽 위 모서리, board[r][c]를 오른쪽 아래 모서리로 하는
    직사각형의 모든 요소의 합을 저장한 2차원 누적합 배열을 만든다.

    | 1 | 2 | 3 | 4 |       | 1 | 3  | 6  | 10 |
    | 5 | 6 | 7 | 8 |  ==>  | 6 | 14 | 24 | 36 |
    | 1 | 2 | 3 | 4 |       | 7 | 17 | 30 | 46 |

    """
    accumulate = [[0] * N for _ in range(N)]

    for r in range(N):
        for c in range(N):
            accumulate[r][c] = board[r][c]
            if c > 0:
                accumulate[r][c] += accumulate[r][c - 1]

    for c in range(N):
        for r in range(1, N):
            accumulate[r][c] += accumulate[r - 1][c]

    return accumulate


def get_max(board, N, M):
    """
    2차원 배열에서 주어진 크기의 정사각형을 선택했을 때
    그 안에 있는 요소의 합의 최대값을 구한다.

    board: 주어진 2차원 배열
    N: board의 가로, 세로 길이
    M: 정사각형의 가로, 세로 길이

    accumulate: 2차원 누적합 배열
    max_value: 정사각형 내의 요소의 합의 최대값 (리턴값)
    """
    accumulate = get_accumulate(board, N)
    max_value = 0

    for r in range(N - M + 1):
        for c in range(N - M + 1):
            current = accumulate[r - 1 + M][c - 1 + M]
            if r > 0:
                current -= accumulate[r - 1][c - 1 + M]
            if c > 0:
                current -= accumulate[r - 1 + M][c - 1]
            if r > 0 and c > 0:
                current += accumulate[r - 1][c - 1]

            if current > max_value:
                max_value = current

    return max_value


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = []

    for _ in range(N):
        board.append(list(map(int, input().split())))

    max_value = get_max(board, N, M)
    print("#{} {}".format(tc, max_value))
