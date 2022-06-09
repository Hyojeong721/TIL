import sys
sys.stdin = open('input.txt')

T = int(input())

def comb(N, K, board):
    answer = 0
    if N == 0:
        if K == 0:
            return 1
        else:
            return 0

    for i in range(12):
        if board[i]:
            continue
        print(N)
        print('-----------')
        board[i] = True
        answer += comb(N - 1, K - i - 1, board)

    return answer

for test_case in range(1, T + 1):

    input_text = list(map(int, input().split()))

    N = input_text[0]
    K = input_text[1]
    board = [False, False, False, False, False, False, False, False, False, False, False, False]

    answer = comb(2, 4, board)







