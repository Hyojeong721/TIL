import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # 테스트케이스 넘버
    N = int(input())
    print('#{}'.format(tc))

    # 달팽이 숫자
    curR = 0
    curC = 0
    value = 1
    board = [[0] * N for _ in range(N)]

    # 우 하 좌 상
    drow = [0, 1, 0, -1]
    dcol = [1, 0, -1, 0]
    mode = 0

    while value <= N * N:
        # 1. 현재 위치(시작점)에 value=1(초기값) 입력
        board[curR][curC] = value

        # 2-1. 다음 위치로 이동
        newR = curR + drow[mode]
        newC = curC + dcol[mode]

        # 2-2. 위치가 유효한지 확인 (유효X: 자리가 없거나 이미 값이 있는 경우)
        if newR < 0 or newR >= N or newC < 0 or newC >= N or board[newR][newC]:
            # 2-3. 유효하지 않은 경우 mode 변경
            mode = (mode + 1) % 4

        # 3. value 값 채워넣기
        value += 1

        # 4. 현재 좌표 업데이트
        curR += drow[mode]
        curC += dcol[mode]

    for i in range(N):
        for j in board[i]:
            print(j, end=" ")
        print()
