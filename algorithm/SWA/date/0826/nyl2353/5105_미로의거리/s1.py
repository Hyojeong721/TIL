'''

[DFS] -> s1
재귀함수로 하면 여러 경로가 있을 때 방향에 따라 경로에 따른 거리가 달라진다.

[BFS] -> s2
큐를 사용해야 가장 가까운 순서대로 출력한다.

'''
import sys
sys.stdin = open('input.txt')


def dist_maze(row, col, dist):
    """
    도착지로의 길이 있으면 출발지로부터의 거리를 반환, 없으면 0 을 반환하는 함수

    :param row: 현재 위치한 행
    :param col: 현재 위치한 열
    :param dist: 출발지에서 현재 위치까지의 거리
    :return: (constant)
    """
    # 모든 방향 탐색
    for i in range(4):
        row += dr[i]
        col += dc[i]

        # 인덱스 범위가 유효하면
        if 0 <= row < N and 0 <= col < N:
            # 도착지면 거리 반환
            if maze[row][col] == 3:
                return dist

            # 벽이 아니고 방문한 적 없다면, 방문표시 후 해당 위치에서 탐색
            elif not maze[row][col] and not visited[row][col]:
                visited[row][col] = 1
                temp = dist_maze(row, col, dist + 1)
                # 해당 위치에서 탐색한 결과, 길이 있다면 거리 반환
                if temp:
                    return temp

        # 탐색 후 복귀
        row -= dr[i]
        col -= dc[i]

    # 모든 방향 탐색 마치고도 도착점 못 찾았으면 0 반환
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

    result = dist_maze(row, col, 0)
    print('#{} {}'.format(tc, result))