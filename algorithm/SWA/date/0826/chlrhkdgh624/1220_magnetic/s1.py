import sys
sys.stdin = open('input.txt')


def magnetic(current):
    global N
    deadlock = 0
    for row in current:
        queue = ''
        for magnet in row:
            queue += str(magnet)
        queue = queue.replace('0', '')
        for x in range(len(queue) - 1):
            if queue[x] == '1' and queue[x + 1] == '2':
                deadlock += 1

    return deadlock


T = 10

for tc in range(1, T + 1):
    N = int(input())
    info = [list(map(int, input().split())) for _ in range(N)]
    board = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            board[j][i] = info[i][j]

    result = magnetic(board)
    print(f'#{tc} {result}')