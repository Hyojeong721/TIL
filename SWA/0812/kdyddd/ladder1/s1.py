import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T + 1):

    case = int(input())

    board = []
    x = 99
    y = 99

    for i in range(100):
        ladder = list(map(int, input().split()))
        board.append(ladder)
        if i == 99:
            for j in range(100):
                if ladder[j] == 2:
                    x = j

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    direction = 0
    while y != 0:

        if direction == 0:
            for i in range(2, 4):
                if 0 <= x + dx[i] < 100 and board[y + dy[i]][x + dx[i]] != 0:
                    direction = i
            if direction == 0:
                y -= 1
        elif direction == 2:
            if 0 <= x + dx[2] and board[y + dy[2]][x +dx[2]] != 0:
                x -= 1
            else:
                direction = 0
                y -= 1
        elif direction == 3:
            if x + dx[i] < 100 and board[y + dy[3]][x +dx[3]] != 0:
                x += 1
            else:
                direction = 0
                y -= 1
    print(f'#{test_case} {x}')











