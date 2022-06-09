from collections import deque
import sys
sys.stdin = open('input.txt')


"""
pipe_route: 각각 상/우/하/좌로 갈 수 있는 경로가 있는 터널 타입의 모음
    ex. pipe_route[3][1]이 1 => 3번 타입에서는 오른쪽으로 갈 수 있다.
        pipe_route[5][0]이 0 => 5번 타입에서는 위쪽으로 갈 수 없다.
"""
pipe_route = [
    [],
    [1, 1, 1, 1],
    [1, 0, 1, 0],
    [0, 1, 0, 1],
    [1, 1, 0, 0],
    [0, 1, 1, 0],
    [0, 0, 1, 1],
    [1, 0, 0, 1],
]


# 상/우/하/좌
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T + 1):
    N, M, R, C, L = map(int, input().split())
    board = []

    for _ in range(N):
        board.append([int(x) for x in input().split()])

    visited = [[False] * M for _ in range(N)]

    queue = deque()
    queue.append((R, C, 1))
    visited[R][C] = True
    # count: 제한 시간 내에 탈주범이 갈 수 있는 장소의 개수
    count = 1

    # BFS 알고리즘을 이용하여 탐색
    while queue:
        r, c, hour = queue.popleft()

        # 제한 시간(L)과 같은 경우 => 추가 경로를 탐색하지 않는다.
        if hour == L:
           continue

        # 상우하좌로 탐색 진행
        for i in range(4):
            """
            1) 범위가 유효하고 / 2) 해당 공간에 파이프가 있으며
            3) 아직 방문하지 않았고 / 4) 파이프가 연결되어 있다면
            """
            cnt_r, cnt_c = r + dr[i], c + dc[i]

            if (0 <= cnt_r < N and 0 <= cnt_c < M
                    and board[cnt_r][cnt_c]
                    and not visited[cnt_r][cnt_c]
                    and pipe_route[board[r][c]][i]  # 4 - 1) 현재 위치에서 상/우/하/좌로 갈 수 있다면
                    and pipe_route[board[cnt_r][cnt_c]][(i + 2) % 4]):  # 4 - 2) 이동할 위치에서 하/좌/상/우로 갈 수 있다면
                visited[cnt_r][cnt_c] = True
                count += 1
                queue.append((cnt_r, cnt_c, hour + 1))

    print("#{} {}".format(tc, count))
