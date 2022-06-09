import sys
sys.stdin = open('input.txt')

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]
direction = {
    1: [0, 1, 2, 3],
    2: [0, 1],
    3: [2, 3],
    4: [0, 3],
    5: [1, 3],
    6: [1, 2],
    7: [0, 2],
}
pair = {0: 1, 1: 0, 2: 3, 3: 2}

def move_tunnel(r, c):
    global cnt, visited
    starts = [[r, c]]
    time = 1

    while True:
        time += 1
        if time > L:
            return

        candidate = []
        for start in starts:
            ways = direction[tunnel[start[0]][start[1]]]
            for way in ways:
                row = start[0] + dr[way]
                col = start[1] + dc[way]
                if 0 <= row < N and 0 <= col < M and tunnel[row][col] and not visited[row][col]:
                    if pair[way] in direction[tunnel[row][col]]:
                        cnt += 1
                        visited[row][col] = True
                        candidate.append([row, col])
        starts = candidate


T = int(input())
for tc in range(1, T + 1):
    # num.row, num.col, manhole's row, manhole's col, elapsed time
    N, M, R, C, L = map(int, input().split())
    tunnel = []
    for _ in range(N):
        tunnel.append(list(map(int, input().split())))

    visited = [[False] * M for _ in range(N)]
    visited[R][C] = True
    cnt = 1
    move_tunnel(R, C)

    print('#{} {}'.format(tc, cnt))
