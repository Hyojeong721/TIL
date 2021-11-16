import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    tc = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    result = 0
    # start, goal 좌표 도출
    for i in range(16):
        for j in range(16):
            if maze[i][j] == 2:
                start = i, j
            if maze[i][j] == 3:
                goal = i, j
                break

    stack = [start]
    # 방문 배열 생성
    visited = [[0] * 16 for _ in range(16)]
    visited[start[0]][start[1]] = 1

    while stack:
        now = stack.pop()

        if maze[now[0]][now[1]] == 3:   # 도착지에 도착하면 반복문 종료
            visited[now[0]][now[1]] = 1
            break
        # 우, 하, 좌, 상 검토후 이동 가능한 곳이면 좌표 이동
        for dr, dc in [[0, 1], [1, 0], [0, -1], [-1, 0]]:
            ni = now[0] + dr
            nj = now[1] + dc
            # 인덱스 범위 안에 있고, 벽이 없고, 방문한 적 없으면 이동 가능
            if 0 <= ni < 16 and 0 <= nj < 16 and maze[ni][nj] != 1 and visited[ni][nj] == 0:
                stack.append((ni, nj))
                visited[ni][nj] = 1  # 방문한 곳을 1로 체크

    # 도착점이 체크되어 있는지 검토
    if visited[goal[0]][goal[1]]:
        result = 1

    print('#{} {}'.format(tc, result))
