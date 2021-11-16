import sys
sys.stdin = open('sample_input.txt')
T = int(input())

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]


def path_find(maze):
    global N
    start = []

    for row in maze:
        if 2 in row:
            start.append(maze.index(row))
            start.append(row.index(2))

    count = [[0] * (N+1) for _ in range(N+1)]
    queue = [start]

    while len(queue):
        search_point = queue.pop(0)
        i = search_point[0]
        j = search_point[1]

        for d in range(4):
            next_i = i + dy[d]
            next_j = j + dx[d]

            if 0 <= next_i < N and 0 <= next_j < N:
                if maze[next_i][next_j] == 0 and count[next_i][next_j] == 0:
                    queue.append([next_i, next_j])
                    count[next_i][next_j] = count[i][j] + 1
                if maze[next_i][next_j] == 3:
                    return count[i][j]

            else:
                continue
    else:
        return 0


for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    result = path_find(matrix)
    print(f'#{tc} {result}')
