import sys
sys.stdin = open('input.txt')


def dist_maze(row, col):
    """
    시작점에서 도착점으로 길이 있으면 거리를 반환, 없으면 0을 반환하는 함수
    :param row: 시작 행
    :param col: 시작 열
    :return: (constant)
    """
    # 시작점 인큐, 방문
    queue = [[row, col]]
    visited[row][col] = 1

    # 큐가 비어있지 않으면
    while queue:
        # dequeue하고 현재 위치로 설정
        row, col = queue.pop(0)

        for i in range(4):
            r = row + dr[i]
            c = col + dc[i]

            # 현재 위치에서 갈 수 있는 방향이 인덱스 범위인지
            if r in range(N) and c in range(N):
                # 도착점이면 거리 반환
                if maze[r][c] == 3:
                    return visited[row][col] - 1

                # 벽이 아니고 방문한 적 없으면, 인큐하고 거리 저장
                elif not maze[r][c] and not visited[r][c]:
                    queue.append([r, c])
                    visited[r][c] = visited[row][col] + 1

    # 못 찾았으면 0 반환
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # N*N 미로 만들고, 출발 좌표(row, col) 찾기
    maze = []
    for r in range(N):
        temp = []
        idx = -1
        for c in input():
            idx += 1
            temp.append(int(c))
            if int(c) == 2:
                row = int(r)
                col = idx
        maze.append(temp)

    # 방문한 위치 체크할 배열
    visited = [[0] * N for _ in range(N)]

    # 탐색 방향 순서 : 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    result = dist_maze(row, col)
    print('#{} {}'.format(tc, result))