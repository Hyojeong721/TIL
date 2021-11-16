'''

1. while 문

'''
import sys
sys.stdin = open('input.txt')


def is_route(N, maze, start):
    """
    미로에서 도착지로의 경로가 있으면 1 반환. 없으면 0 반환.
    전망이 없는 길(0)은 벽(1)으로 바꾸며 돌아온다.

    :param N: 미로의 길이
    :param maze: 1로 테두리 패딩한 미로
    :param start: 패딩된 미로에서 출발지의 위치
    :return: boolean

    """
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    stack = []      # 지나온 길
    r, c = start    # 현재 위치

    while True:
        # 막힌 방향의 수
        cnt = 0

        # 모든 방향에 대해 경로 탐색
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]

            # 다중 if : 길이 존재하는지 검사하고, 존재하면 for문 탈출
            # 인덱스 범위 (패딩 전 미로) 안이고,
            if 1 <= nr <= N and 1 <= nc <= N:
                # 벽이 아니며,
                if maze[nr][nc] != 1:
                    # 출발점이거나 이전위치가 아니면, 이 방향으로 길 존재!
                    if not stack or stack[-1] != [nr, nc]:
                        # 도착지면 1을 반환
                        if maze[nr][nc] == 3:
                            return 1
                        # 도착지 아니면 push 하고 이동 후 for 문 탈출
                        stack.append([r, c])
                        r, c = nr, nc
                        break

            # 해당 방향에 길이 없었으면 cnt +1
            cnt += 1

        # 모든 방향에 대해 갈 곳 없으면 => 현재 위치 1로 만들고 pop 하여 이동
        if cnt == 4:
            if stack:
                maze[r][c] = 1
                r, c = stack.pop()
            else:
                return 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # 좌우상하 1로 패딩된 N*N 미로 만들고, 출발점 찾기
    maze = [[1] * (N + 2)]
    for i in range(N):
        temp = [1]
        idx = 0
        for j in input():
            temp.append(int(j))
            idx += 1
            if int(j) == 2:
                start = [i + 1, idx]
        temp.append(1)
        maze.append(temp)
    maze.append([1] * (N + 2))

    # 경로 유무 찾기
    result = is_route(N, maze, start)
    print('#{} {}'.format(tc, result))