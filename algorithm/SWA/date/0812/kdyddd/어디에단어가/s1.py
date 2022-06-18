import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N, K = list(map(int, input().split()))
    board = []

    for i in range(N):
        temp = list(map(int, input().split()))
        board.append(temp)

    answer = 0
    for i in range(N):
        cnt1 = 0
        cnt2 = 0
        for j in range(N):
            if cnt1 == K and board[i][j] == 0:
                answer += 1
                cnt1 = 0

            if board[i][j] == 1:
                cnt1 += 1
                if cnt1 == K and j == N - 1:
                    answer += 1
            else:
                cnt1 = 0

            if cnt2 == K and board[j][i] == 0:
                answer += 1
                cnt2 = 0

            if board[j][i] == 1:
                cnt2 += 1
                if cnt2 == K and j == N - 1:
                    answer += 1
            else:
                cnt2 = 0

    print(f'#{test_case} {answer}')







