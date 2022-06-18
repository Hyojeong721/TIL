import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):

    N = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    ans = 0

    # 가로
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += board[i][j]
        if temp > ans:
            ans = temp

    # 세로
    for i in range(100):
        temp = 0
        for j in range(100):
            temp += board[j][i]
        if temp > ans:
            ans = temp

    # 오른쪽 아래로 가는 대각선
    temp = 0
    for i in range(100):
        for j in range(100):
            if i == j:
                temp += board[i][j]
    if temp > ans:
        ans = temp

    # 왼쪽 아래로 가는 대각선
    temp = 0
    for i in range(100):
        for j in range(100):
            if i + j == 99:
                temp += board[i][j]
    if temp > ans:
        ans = temp

    print('#{} {}'.format(tc, ans))