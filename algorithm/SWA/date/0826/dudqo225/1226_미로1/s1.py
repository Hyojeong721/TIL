import sys
sys.stdin = open('input.txt')

def findMaze():
    global maze, s_i, s_j, e_i, e_j

    stack = [(e_i, e_j)]

    while stack:


T = 10
for tc in range(1, T+1):
    tc_num = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[0 for _ in range(16)] for _ in range(16)]

    s_i, s_j, e_i, e_j = 0, 0, 0, 0
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                s_i, s_j = i, j
            if maze[i][j] == 3:
                e_i, e_j = i, j

    ans = findMaze()

    print(s_i, s_j, e_i, e_j)