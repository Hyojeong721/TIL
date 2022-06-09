import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):
    N = int(input())
    board = []
    cnt = 0
    for _ in range(8):
        board.append(input())

    for chars in board:
        for i in range(9-N):
            if chars[i:i+N] == chars[i:i+N][::-1]:
                cnt += 1

    for j in range(8):
        chars = ''
        for temp in board:
            chars += temp[j]
        for i in range(9-N):
            if chars[i:i+N] == chars[i:i+N][::-1]:
                cnt += 1

    print('#{} {}'.format(tc, cnt))


