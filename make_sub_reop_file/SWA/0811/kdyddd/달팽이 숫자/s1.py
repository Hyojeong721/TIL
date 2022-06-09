import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    board = [[0 for col in range(N)] for row in range(N)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    x = -1
    y = 0
    direction = 0
    num = 1
    for i in range(N, 0, -1):
        if i == N:
            for j in range(i):
                x += dx[direction % 4]
                y += dy[direction % 4]
                board[y][x] = num
                num += 1
            direction += 1
        else:
            for j in range(i):
                x += dx[direction % 4]
                y += dy[direction % 4]
                board[y][x] = num
                num += 1
            direction += 1
            for j in range(i):
                x += dx[direction % 4]
                y += dy[direction % 4]
                board[y][x] = num
                num += 1
            direction += 1


    print(f'#{test_case}')

    for i in range(N):
        nums = ''
        for j in range(N):
            nums += str(board[i][j])
            if j != N:
                nums += ' '
        print(nums)
