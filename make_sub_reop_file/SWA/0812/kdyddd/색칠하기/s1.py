import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):

    case = int(input())

    board = [[0 for col in range(10)] for row in range(10)]

    answer = 0

    for i in range(case):
        color = list(map(int, input().split()))
        for j in range(color[0], color[2] + 1):
            for k in range(color[1], color[3] + 1):
                if board[j][k] == 0:
                    board[j][k] = color[4]
                else:
                    if board[j][k] != color[4]:
                        board[j][k] = -1
    for i in range(10):
        for j in range(10):
            if board[i][j] == -1:
                answer += 1

    print(f'#{test_case} {answer}')