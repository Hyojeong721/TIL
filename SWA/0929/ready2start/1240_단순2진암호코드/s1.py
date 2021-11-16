import sys
sys.stdin = open('input.txt')


cipher_dict = {
    '0001101': 0, '0011001': 1,
    '0010011': 2, '0111101': 3,
    '0100011': 4, '0110001': 5,
    '0101111': 6, '0111011': 7,
    '0110111': 8, '0001011': 9,
}

T = int(input())
for C in range(1, T + 1):
    N, M = map(int, input().split())
    board = []

    for _ in range(N):
        board.append(input())

    # 암호의 시작 위치를 찾는다.
    start = [0, 0]

    for r in range(N):
        # 앞에서부터 찾을 경우, 패턴이 잘못 매칭되는 경우가 발생함.
        # 모든 숫자의 암호코드가 1로 끝나기 때문에
        # 뒤에서부터 탐색하여 1을 찾는 방식으로 암호코드의 위치를 탐색함.
        for c in range(M - 1, 6, -1):
            if board[r][c] == '1':
                start = [r, c - 55]
                break
        # 시작 위치를 찾았다면 탐색을 종료한다.
        if start != [0, 0]:
            break

    # codes: 전체 암호코드
    # total: 검증을 위한 합 (10의 배수가 되어야 유효한 코드)
    codes = []
    total = 0
    nr, nc = start

    for i in range(8):
        code = cipher_dict[board[nr][nc:nc + 7]]
        codes.append(code)
        nc += 7

    for i in range(8):
        if i % 2 == 0:
            total += (codes[i] * 3)
        else:
            total += codes[i]

    if total % 10 == 0:
        print("#{} {}".format(C, sum(codes)))
    else:
        print("#{} {}".format(C, 0))
