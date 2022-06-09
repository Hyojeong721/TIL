import sys

sys.stdin = open('input.txt')

T = 10
for tc in range(1, T + 1):

    # 구해야 하는 회문 길이
    N = int(input())

    # 글자판 (board)
    board = []
    for i in range(8):
        board += [input()]

    # 회문 개수 (count)
    count = 0
    for i in range(8):
        for j in range(8-N+1):

            # 가로
            string = board[i][j:j+N]
            if string[::] == string[::-1]:
                count += 1

            # 세로
            string = ''
            for k in range(N):
                string += board[j+k][i]
            if string[::] == string[::-1]:
                count += 1

    print('#{} {}'.format(tc, count))

'''
    # 가로
    count = 0
    for i in range(8):
        for j in range(8-N+1):
            string = board[i][j:j+N]
            if string[::] == string[::-1]:
                count += 1
    # 세로
    for j in range(8):
        for i in range(8-N+1):
            string = ''
            for k in range(N):
                string += board[i+k][j]
            if string[::] == string[::-1]:
                count += 1
    print('#{} {}'.format(tc, count))
'''

