import sys
sys.stdin = open('input.txt')

T = int(input())



for test_case in range(1, T + 1):

    N, M = list(map(int, input().split()))


    board = []

    for i in range(N):
        board.append(input())

    str_list = []

    for i in range(N):
        temp = ''
        for j in range(N - M + 1):
            str_list.append(board[i][j:j + M])
    break