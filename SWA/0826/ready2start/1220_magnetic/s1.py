import sys
sys.stdin = open("input.txt")


def count_deadlock(board, N):
    """
    주어진 2차원 배열에서 교착 상태의 개수를 구한다.
      - 배열 위에는 N극, 아래에는 S극이 있다.
      - 배열에서 1은 N극 자성체, 2는 S극 자성체다.
    Args:
        N: 배열의 가로, 세로 길이
    Returns:
        count: 교착상태의 개수
    """
    # ready: 1이 나오면 교착상태가 준비되었으므로 True
    # 이후 2가 나오면 count가 1 증가되고 ready는 다시 False가 된다.
    ready = False
    count = 0

    # 2차원 배열을 세로로 한 줄씩 읽는다.
    for c in range(N):
        for r in range(N):
            # 1이 나오면 교착상태가 준비되었음을 표시한다.
            if board[r][c] == 1:
                ready = True
            # 2가 나온 경우
            elif board[r][c] == 2:
                # 교착상태가 준비된 상태라면
                if ready:
                    # 교착상태의 개수를 하나 증가시키고 교착상태 준비를 False로 둔다.
                    count += 1
                    ready = False
        # 한 줄을 다 읽은 후에는, 다시 교착상태 준비를 False로 둔다.
        ready = False

    return count


T = 10

for tc in range(1, T + 1):
    N = int(input())
    board = [[int(x) for x in input().split()] for _ in range(N)]

    count = count_deadlock(board, N)
    print("#{} {}".format(tc, count))
