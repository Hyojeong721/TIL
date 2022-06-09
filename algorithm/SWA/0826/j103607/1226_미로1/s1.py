import sys
sys.stdin = open('input.txt')


T = 10
for tc in range(1, T+1):

    N = int(input())
    maze = [list(map(int, input())) for _ in range(16)]

    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    stack = [(1, 1)]
    result = 0

    while stack:
        a = stack.pop()
        cx = a[0]
        cy = a[1]
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < 16 and 0 <= ny < 16:
                if maze[nx][ny] == 0:
                    stack.append((nx, ny))
                    maze[nx][ny] = 1
                elif maze[nx][ny] == 3:
                    result = 1
                    break

    print('#{} {}'.format(tc, result))