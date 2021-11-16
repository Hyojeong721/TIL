import sys
sys.stdin = open('input.txt')

def if_can_out_of_maze(x, y, destination, N, maze):
    # forks에 갈림길이 있는 지점들을 저장(하나씩 되짚어올 필요 없이 바로 가장 가까운 갈림길들로 워프)
    forks = []
    while True:
        if y == destination[0] and x == destination[1]:
            return 1
        go_up(x, y, forks, N, maze)
        go_down(x, y, forks, N, maze)
        go_left(x, y, forks, N, maze)
        go_right(x, y, forks, N, maze)
        if 0 not in maze:
            return 0
        else:
            if_can_out_of_maze(x, y, destination, N, maze)


def go_up(x, y, forks, N, maze):
    direction = directions(x, y, forks, N, maze)
    if sum(direction) == 0:
        for a, b in forks[-1]:
            y = a
            x = b
        del forks[-1]
    elif direction[0] == 1:
        y -= 1
        maze[y][x] = -1
        go_up(x, y, forks, N, maze)

def go_down(x, y, forks, N, maze):
    direction = directions(x, y, forks, N, maze)
    if sum(direction) == 0:
        for a, b in forks[-1]:
            y = a
            x = b
        del forks[-1]
    if direction[1] == 1:
        y += 1
        maze[y][x] = -1
        go_down(x, y, forks, N, maze)

def go_left(x, y, forks, N, maze):
    direction = directions(x, y, forks, N, maze)
    if sum(direction) == 0:
        for a, b in forks[-1]:
            y = a
            x = b
        del forks[-1]
    if direction[2] == 1:
        x -= 1
        maze[y][x] = -1
        go_left(x, y, forks, N, maze)

def go_right(x, y, forks, N, maze):
    direction = directions(x, y, forks, N, maze)
    if sum(direction) == 0:
        for a, b in forks[-1]:
            y = a
            x = b
        del forks[-1]
    if direction[3] == 1:
        x += 1
        maze[y][x] = -1
        go_right(x, y, forks, N, maze)


def directions(x, y, forks, N, maze):
    up = down = left = right = 0
    if y - 1 >= 0 and maze[y - 1][x] == 0:
        up = 1
    if y + 1 <= N - 1 and maze[y + 1][x] == 0:
        down = 1
    if x - 1 >= 0 and maze[y][x - 1] == 0:
        left = 1
    if y + 1 <= N - 1 and maze[y][x + 1] == 0:
        right = 1
    if up + down + left + right > 1:
        forks.append({(y, x): [up, down, left, right]})
    direction = [up, down, left, right]
    return direction

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(int(n) for n in input()) for _ in range(N)]
    # 출발점을 x, y에 입력
    x = y = 0
    destination = [0, 0]
    check = 0
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                y = i
                x = j
                check += 1
            if maze[i][j] == 3:
                destination[0] ,destination[1] = i, j
                check += 1
        if check == 2:
            break
    print('#{} {}'.format(test_case, if_can_out_of_maze(x, y, destination, N, maze)))