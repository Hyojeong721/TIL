import sys
sys.stdin = open('input.txt')


# 인자로 들어온 두 수의 차의 절대값을 구한다.
def diff_abs(num1, num2):
    if num1 > num2:
        return num1 - num2
    else:
        return num2 - num1


def get_near_diff(board, r, c, N):
    """
    배열의 한 요소(board[r][c])의 이웃한 요소와의 차의 절대값을 구한다.

    |   | 1 |   |
    | 2 | 5 | 8 |  ==>  |1 - 5| + |2 - 5| + |8 - 5| + |9 - 5| = 14
    |   | 9 |   |

    N: 배열의 행, 열의 수
    total: 이웃한 요소와의 차의 절대값의 총합
    """
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    total = 0

    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0 <= nr < N and 0 <= nc < N:
            total += diff_abs(board[r][c], board[nr][nc])

    return total


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = []
    # 모든 요소의 (이웃한 요소와의 차의 절대값의 합)의 총합
    total = 0

    for _ in range(N):
        sub_board = list(map(int, input().split()))
        board.append(sub_board)

    for r in range(N):
        for c in range(N):
            temp = get_near_diff(board, r, c, N)
            total += temp

    print("#{} {}".format(tc, total))
