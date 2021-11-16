import sys
sys.stdin = open('input.txt')


def is_route(row, col):
    """
    목적지로의 길이 있으면 1을 반환. 없으면 0을 반환하는 함수

    :param row: 현재 위치한 행
    :param col: 현재 위치한 열
    :return: boolean
    """
    # 모든 방향 탐색
    for i in range(4):
        row += dr[i]
        col += dc[i]

        # 인덱스 범위가 유효하면
        if 0 <= row < 16 and 0 <= col < 16:
            # 도착지면 1 반환
            if maze[row][col] == 3:
                return 1

            # 벽이 아니고 방문한 적 없다면, 방문표시 후 해당 위치에서 탐색
            elif not maze[row][col] and not visited[row][col]:
                visited[row][col] = 1
                if is_route(row, col):
                    return 1

        # 탐색 후 복귀
        row -= dr[i]
        col -= dc[i]

    # 모든 방향 탐색 마치고도 도착점 못 찾았으면 0 반환
    return 0


for _ in range(10):
    tc = int(input())

    # N*N 미로 만들기
    maze = [[int(i) for i in input()] for _ in range(16)]

    # 방문한 위치 체크할 배열
    visited = [[0] * 16 for _ in range(16)]

    # 탐색 방향 순서 : 우하좌상
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    # 출발 좌표 : (1, 1)
    result = is_route(1, 1)
    print('#{} {}'.format(tc, result))