import sys
sys.stdin = open('input.txt')
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def BFS(start, end):
    """
    :param start: 출발점
    :param end: 도착점
    :return: 거리
    """
    Q = [start]
    while Q:
        curr = Q.pop(0)
        if curr == end:
            return visited[end[0]][end[1]] - 1

        for i in range(4):
            if (maze[curr[0] + dx[i]][curr[1] + dy[i]] == 0 or maze[curr[0] + dx[i]][curr[1] + dy[i]] == 3) and visited[curr[0] + dx[i]][curr[1] + dy[i]] == 0:
                visited[curr[0] + dx[i]][curr[1] + dy[i]] = visited[curr[0]][curr[1]] + 1
                Q.append((curr[0] + dx[i], curr[1] + dy[i]))
    return 0

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    maze = [[1] * (N + 2)] + [[1] + list(map(int, list(input()))) + [1] for _ in range(N)] + [[1] * (N + 2)]
    for r in range(N + 2):
        for c in range(N + 2):
            if maze[r][c] == 2: # 출발지 검색
                start = (r, c)
            elif maze[r][c] == 3: # 도착지 검색
                end = (r, c)
    visited = [[0] * (N + 2) for _ in range(N + 2)]
    print('#{} {}'.format(tc, BFS(start, end)))