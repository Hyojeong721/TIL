import sys
sys.stdin = open('input.txt')

def where_to_start(N, maze):
    x = y = 0
    i = j = 0
    while i < N:
        while j < N:
            if maze[i][j] == 2:
                y = i
                x = j
                maze[i][j] = 1
                return x, y
            j += 1
        j = 0
        i += 1

def if_can_out_of_maze(x, y, maze, forks):
    while True:
        if check_if_dest(x, y, maze):
            return 1
        while True:
            directions = [0, 0, 0, 0]
            forks, directions = check_if_fork(x, y, maze, forks, directions)
            if sum(directions):
                if directions[0] == 1:
                    maze[y - 1][x] = 1
                    y -= 1
                    break
                if directions[1] == 1:
                    maze[y + 1][x] = 1
                    y += 1
                    break
                if directions[2] == 1:
                    maze[y][x - 1] = 1
                    x -= 1
                    break
                if directions[3] == 1:
                    maze[y][x + 1] = 1
                    x += 1
                    break
            if forks:
                x = forks[0][1]
                y = forks[0][0]
                del forks[0]
            else:
                return 0

def check_if_fork(x, y, maze, forks, directions):
    if y - 1 >= 0 and maze[y - 1][x] == 0:
        directions[0] = 1
    if y + 1 <= N - 1 and maze[y + 1][x] == 0:
        directions[1] = 1
    if x - 1 >= 0 and maze[y][x - 1] == 0:
        directions[2] = 1
    if x - 1 >= 0 and maze[y][x + 1] == 0:
        directions[3] = 1
    if sum(directions) > 1:
        forks.append([y, x])
    return forks, directions

def check_if_dest(x, y, maze):
    if y - 1 >= 0 and maze[y - 1][x] == 3:
        return 1
    if y + 1 <= N - 1 and maze[y + 1][x] == 3:
        return 1
    if x - 1 >= 0 and maze[y][x - 1] == 3:
        return 1
    if x + 1 <= N - 1 and maze[y][x + 1] == 3:
        return 1

T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    maze = [list(int(n) for n in input()) for _ in range(N)]
    x, y = where_to_start(N, maze)
    forks = []
    print('#{} {}'.format(test_case, if_can_out_of_maze(x, y, maze, forks)))