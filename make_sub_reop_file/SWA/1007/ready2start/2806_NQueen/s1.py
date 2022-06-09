import sys
sys.stdin = open('input.txt')


def get_n_queen(count, n):
    """
    n x n의 보드에 n개의 퀸을 서로 공격하지 못하게 놓는 경우의 수를 구한다.
    Args:
        count: 현재까지 놓은 퀸의 개수
        n: 보드판의 가로, 세로 길이
    """
    global board

    if count == n:
        global total
        total += 1
        return

    for c in range(n):
        for r in range(count):
            # 1. 위쪽 검사
            if board[r][c]:
                break

            # 2. 왼쪽 위 대각선 검사
            if c - count + r >= 0 and board[r][c - count + r]:
                break

            # 3. 오른쪽 위 대각선 검사
            if c + count - r < n and board[r][c + count - r]:
                break
        # break로 빠져나오지 않았다면, 즉 해당 위치에 퀸을 놓을 수 있다면
        # 해당 위치에 퀸을 놓은 다음, 다시 다음 줄에서 탐색을 진행한다.
        else:
            board[count][c] = True
            get_n_queen(count + 1, n)
            board[count][c] = False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [[False] * N for _ in range(N)]
    total = 0

    get_n_queen(0, N)
    print("#{} {}".format(tc, total))
