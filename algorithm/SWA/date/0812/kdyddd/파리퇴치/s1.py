import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, M = list(map(int, input().split()))
    board = []

    for i in range(N):
        temp = list(map(int, input().split()))
        board.append(temp)

    max_num = 0
    for i in range(N - (M - 1)):
        for j in range(N - (M - 1)):
            temp = 0
            for k in range(M):
                for l in range(M):
                    temp += board[i + k][j + l]
            if temp > max_num:
                max_num = temp

    print(f'#{test_case} {max_num}')










