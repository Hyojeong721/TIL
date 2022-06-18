'''

2. 재귀함수

'''
import sys
sys.stdin = open('input.txt')


def is_route(N, maze, row, col):
    """
    미로에서 도착지로의 경로가 있으면 1 반환. 없으면 0 반환.

    :param N: 미로의 가로(세로) 길이
    :param maze: 미로 (N*N 배열)
    :param row: 출발지의 행
    :param col: 출발지의 열
    :return: boolean
    """
    # 모든 방향 탐색
    for i in range(4):
        row += dr[i]
        col += dc[i]

        # 인덱스 범위가 유효하면
        if 0 <= row < N and 0 <= col < N:
            # 도착지면 1 반환
            if maze[row][col] == 3:
                return 1

            # 벽이 아니고 방문한 적 없다면, 방문표시 후 해당 위치에서 탐색
            elif not maze[row][col] and not visited[row][col]:
                visited[row][col] = 1
                if is_route(N, maze, row, col):
                    return 1

        # 탐색 후 복귀
        row -= dr[i]
        col -= dc[i]

    # 모든 방향 탐색 마치고도 도착점 못 찾았으면 0 반환
    return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # N*N 미로 만들고, 출발 좌표 찾기
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

    result = is_route(N, maze, row, col)
    print('#{} {}'.format(tc, result))