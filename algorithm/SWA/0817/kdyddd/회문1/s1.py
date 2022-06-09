import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):

    length = int(input())

    size = 8

    answer = 0

    board = []

    for i in range(size):
        board.append(input())

    for i in range(size):
        for j in range(size - length + 1):
            row = True
            column = True
            for k in range(length // 2):
                if board[i][j + k] != board[i][j + length - 1 - k]:
                    row = False

            for k in range(length // 2):
                if board[j + k][i] != board[j + length - 1 - k][i]:
                    column = False

            if row:
                answer += 1
            if column:
                answer += 1

    print(f'#{test_case} {answer}')