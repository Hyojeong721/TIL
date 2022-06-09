import sys
sys.stdin = open('input.txt', 'r')

dy = [0, 1]
dx = [1, 0]


def path_find(y, x):
    global minimum, total
    if total > minimum:
        return

    if x == N-1 and y == N-1:
        if total < minimum:
            minimum = total
        return

    for step in range(2):
        new_y = y + dy[step]
        new_x = x + dx[step]
        if new_y < N and new_x < N and (new_y, new_x) not in visited:
            visited.append((new_y, new_x))
            total += mat[new_y][new_x]
            path_find(new_y, new_x)
            visited.remove((new_y, new_x))
            total -= mat[new_y][new_x]


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    total = mat[0][0]
    visited = []
    minimum = 9876543210
    path_find(0, 0)

    print('#{} {}'.format(tc, minimum))