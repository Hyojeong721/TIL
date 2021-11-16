import sys
from itertools import permutations
# runtime error
sys.stdin = open('input.txt', 'r')


def move(direction):
    global x, y
    if direction == 'R':
        y += 1
    else:
        x += 1


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    mat = [list(map(int, input().split())) for _ in range(N)]
    directions = ['R']*(N-1) + ['D']*(N-1)  # right, down
    shortcuts = []

    for way in permutations(directions, len(directions)):
        shortcuts.append(way)
    shortcuts = list(set(shortcuts))

    minimum = 987654321
    for shortcut in shortcuts:
        x, y = 0, 0
        total = mat[0][0]
        for step in shortcut:
            move(step)
            total += mat[x][y]
        if total < minimum:
            minimum = total

    print('#{} {}'.format(tc, minimum))






