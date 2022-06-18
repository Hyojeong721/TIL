import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = [input() for _ in range(N)]
    visited = [[0]*N for _ in range(N)]

    for i in range(N):
        for j in range(N):
            if maze[i][j] == '2':
                start = (i, j)
            elif maze[i][j] == '3':
                end = (i, j)
            elif maze[i][j] == '1':
                visited[i][j] = 1

    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    q = []
    q.append(start)

    while q:
        v = q.pop(0)
        y = v[0]
        x = v[1]
        for w in range(4):
            ty = y + dy[w]
            tx = x + dx[w]
            if 0 <= ty < N and 0 <= tx < N:
                if visited[ty][tx] == 0:
                    q.append((ty, tx))
                    visited[ty][tx] = visited[y][x] + 1

    if visited[end[0]][end[1]] == 0:
        print(f'#{tc} 0')
    else:
        print(f'#{tc} {visited[end[0]][end[1]]-1}')
