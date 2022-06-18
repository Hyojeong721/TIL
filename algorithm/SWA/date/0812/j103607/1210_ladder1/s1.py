import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):

    case_number = int(input())
    board = [list(map(int, input().split())) for _ in range(100)]

    # 도착지점 좌표 (x=99, y)
    for i in range(100):
        if board[99][i] == 2:
            y = i

    # 왼쪽에 1이 있는 동안 계속 왼쪽으로 -> 막히면 위로

    # 오른쪽에 1이 있는 동안 계속 오른쪽으로 -> 막히면 위로

    # else: 위로
