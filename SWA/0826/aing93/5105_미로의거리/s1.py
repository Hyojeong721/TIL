import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    start = []
    end = []
    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start_y, start_x = i, j
            elif maze[i][j] == '3':
                end_y, end_x = i, j

    print(start_x,start_y)

