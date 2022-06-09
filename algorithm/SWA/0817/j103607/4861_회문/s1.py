import sys

sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())

    for n in range(N):
        str_board = list(input())
        # print(str_board)

        for i in range(N):
            str_board[i:i+M//2+1]