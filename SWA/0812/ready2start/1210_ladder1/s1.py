import sys
sys.stdin = open("input.txt")


def get_start_col(board, c):
    """사다리의 도착 위치의 열을 인자로 받아 출발 위치의 열을 구한다.
       (도착 위치에서 사다리를 타고 올라가서 출발 위치를 찾는다.)

    while (맨 위에 도달할 때까지)
        왼쪽으로 갈 수 있다면 갈 수 있을 때까지 왼쪽으로 이동하고
        오른쪽으로 갈 수 있다면 갈 수 있을 때까지 오른쪽으로 이동하고
        양쪽 모두 갈 수 없다면 위로 1칸 이동한다.

    board: 사다리
    c: 도착 위치의 열
    nr, nc: 현재 탐색 위치의 행/열
    """
    nr, nc = 99, c

    while nr > 0:
        if nc > 0 and board[nr][nc - 1] == 1:
            while nc > 0 and board[nr][nc - 1] == 1:
                nc -= 1
            # 같은 막대를 계속 왕복하지 않도록
            # 막대를 타고 옆으로 이동한 후에는 한 칸 올려준다.
            nr -= 1
            continue

        if nc < 99 and board[nr][nc + 1] == 1:
            while nc < 99 and board[nr][nc + 1] == 1:
                nc += 1
            nr -= 1
            continue

        nr -= 1

    return nc


T = 10

for _ in range(T):
    tc = int(input())
    board = []

    for _ in range(100):
        board.append(list(map(int, input().split())))

    # 도착 좌표 설정
    for c in range(100):
        if board[99][c] == 2:
            end_c = c
            break

    start_c = get_start_col(board, end_c)
    print("#{} {}".format(tc, start_c))
