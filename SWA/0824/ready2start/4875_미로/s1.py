# 방법 1 : while문 이용

import sys
sys.stdin = open("input.txt")


def check_route(board, N):
    """
    주어진 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인한다.
    Args:
        board: 미로 (2차원 배열)
               0은 통로, 1은 벽, 2는 출발점, 3은 도착점
        N: 미로의 가로, 세로 길이
    Returns:
        출발지에서 목적지에 도착하는 경로가 존재하면 True, 없으면 False
    """
    # 출발지 지정
    for r in range(N):
        # 인덱스 r의 문자열에 '2'가 존재한다면
        if board[r].find('2') > -1:
            # 해당 위치를 초기값으로 설정하고 반복을 종료한다.
            start_r, start_c = r, board[r].find('2')
            break

    visited = [[False] * N for _ in range(N)]
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]
    stack = [(start_r, start_c)]

    while stack:
        cnt_r, cnt_c = stack.pop()

        for i in range(4):
            # 탐색 위치의 인덱스가 유효하며, 아직 방문하지 않은 위치라면
            if 0 <= cnt_r + dr[i] < N and 0 <= cnt_c + dc[i] < N:
                # 현재 위치가 '3'이라면 => 도착점을 찾았으므로 True를 리턴한다.
                if board[cnt_r + dr[i]][cnt_c + dc[i]] == '3':
                    return True
                # 현재 위치가 '0'이고 아직 방문하지 않았다면
                # => 방문 표시를 하고, 스택에 해당 좌표를 저장한다.
                elif (board[cnt_r + dr[i]][cnt_c + dc[i]] == '0'
                      and not visited[cnt_r + dr[i]][cnt_c + dc[i]]):
                    visited[cnt_r + dr[i]][cnt_c + dc[i]] = True
                    stack.append((cnt_r + dr[i], cnt_c + dc[i]))

    return False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    result = check_route(board, N)
    print("#{} {}".format(tc, int(result)))
