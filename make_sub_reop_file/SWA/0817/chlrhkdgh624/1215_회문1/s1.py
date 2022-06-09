import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    N = int(input())
    board = [list(input()) for _ in range(8)]
    count = 0

    # 가로 방향
    for row in range(8):
        for col in range(8-N+1):
            sequence = board[row][col:col+N]
            sequence_reverse = [sequence[i] for i in range(N-1, -1, -1)]
            if sequence == sequence_reverse:
                count += 1
    # 세로방향
    for col in range(8):
        for row in range(8-N+1):
            sequence = []
            for j in range(N):
                sequence += board[row+j][col]
            sequence_reverse = [sequence[i] for i in range(N-1, -1, -1)]
            if sequence == sequence_reverse:
                count += 1

    print(f'#{tc} {count}')

