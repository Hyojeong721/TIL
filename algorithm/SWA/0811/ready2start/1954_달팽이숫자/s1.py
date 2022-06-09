import sys
sys.stdin = open("input.txt")


def make_snail(n):
    """
    (n X n) 크기의 달팽이를 만든다.

    r, c: 현재 위치의 열과 행
    i: dr, dc 배열 내의 인덱스
    current: 현재 입력해야 할 숫자
    """
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 모든 값이 0인 (n x n) 크기의 배열 생성
    board = [[0] * n for _ in range(n)]
    # 처음 board[0][0]으로 이동하도록 초기값을 (0, -1)로 설정
    r, c = 0, -1
    i, current = 0, 1

    while current <= n * n:
        # 배열의 인덱스가 유효하고 아직 해당 인덱스에 방문하지 않았다면
        if (0 <= r + dr[i] < n and 0 <= c + dc[i] < n
                and not board[r + dr[i]][c + dc[i]]):
            r, c = r + dr[i], c + dc[i]
            board[r][c] = current
            current += 1
        else:
            i = (i + 1) % 4

    return board


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    snail_board = make_snail(N)

    print("#{}".format(tc))
    for r in range(N):
        for c in range(N):
            print(snail_board[r][c], end=" ")
        print()
