import sys
sys.stdin = open('input.txt')

T = 10

for tc in range(1, T+1):
    a = int(input())
    maze = [input() for _ in range(16)]
    visited = [[0]*16 for _ in range(16)]

    # 시작점과 끝나는점 찾아서 튜플로 좌표 만들기
    for i in range(16):
        for j in range(16):
            if maze[i][j] == '2':
                start = (i, j)
            elif maze[i][j] == '3':
                end = (i, j)
            elif maze[i][j] == '1':
                visited[i][j] = 1

    # 상하좌우
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    # 스택 만들어서 시작점 넣기
    stack = [start]

    while stack:
        # 스택에서 pop해서 스택의 마지막부분 방문
        v = stack.pop()
        y = v[0]
        x = v[1]
        # 방문하지 않았던 좌표면
        if visited[y][x] == 0:
            visited[y][x] = 1
            # 주변 네군데 탐색
            for w in range(4):
                ty = y + dy[w]
                tx = x + dx[w]
                # index범위 지정, 방문하지 않은 곳만 탐색
                if 0 <= ty < 16 and 0 <= tx < 16 and visited[ty][tx] == 0:
                    stack.append((ty, tx))

    print(f'#{tc} {visited[end[0]][end[1]]}')