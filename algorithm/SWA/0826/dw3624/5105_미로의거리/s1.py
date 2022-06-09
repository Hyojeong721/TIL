import sys
sys.stdin = open('input.txt')


def maze_run(start):
    # 상하좌우
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    que = [start]

    while que:
        v = que.pop(0)
        y, x = v[0], v[1]

        for d in range(4):
            new_y = y + dy[d]
            new_x = x + dx[d]

            if 0 <= new_y < N and 0 <= new_x < N:
                if maze[new_y][new_x] == 3:
                    # [print(m) for m in maze]
                    # [print(v) for v in visit]
                    return visit[y][x]

                if not maze[new_y][new_x] and not visit[new_y][new_x]:
                    que.append([new_y, new_x])
                    maze[new_y][new_x] = 2
                    visit[new_y][new_x] = visit[y][x] + 1

    return 0



T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [list(map(int, input())) for _ in range(N)]
    visit = [[0 for _ in range(N)] for _ in range(N)]

    for y in range(N):
        for x in range(N):
            if maze[y][x] == 2:
                start = [y, x]
                break

    result = maze_run(start)
    print('#{} {}'.format(tc, result))