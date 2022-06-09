# 방법 2 : 재귀 함수 이용

import sys
sys.stdin = open("input.txt")


def check_route(board, N, cnt_r, cnt_c):
    """
    주어진 미로에서 출발지에서 목적지에 도착하는 경로가 존재하는지 확인한다.
    Args:
        board: 미로 (2차원 배열)
               0은 통로, 1은 벽, 2는 출발점, 3은 도착점
        N: 미로의 가로, 세로 길이
        cnt_r, cnt_c: 현재 탐색 위치
    Returns:
        출발지에서 목적지에 도착하는 경로가 존재하면 True, 없으면 False
    """
    # 상우하좌 순서대로 탐색
    for i in range(4):
        cnt_r += dr[i]
        cnt_c += dc[i]

        # 탐색 위치의 인덱스가 유효하다면
        if 0 <= cnt_r < N and 0 <= cnt_c < N:
            # 현재 위치가 '3'이라면 => 도착점을 찾았으므로 True를 리턴한다.
            if board[cnt_r][cnt_c] == '3':
                return True
            # 현재 위치가 '0'이고 아직 방문하지 않았다면
            # => 방문 표시 후, 해당 위치에서 다시 탐색을 진행한다.
            elif (board[cnt_r][cnt_c] == '0'
                    and not visited[cnt_r][cnt_c]):
                visited[cnt_r][cnt_c] = True
                if check_route(board, N, cnt_r, cnt_c):
                    return True

        # 탐색 종료 후에는 기존 위치로 복귀한다.
        cnt_r -= dr[i]
        cnt_c -= dc[i]

    # 탐색을 마쳤는데 도착점을 찾지 못했다면 False를 리턴한다.
    return False


T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    board = [input() for _ in range(N)]

    # 시작 위치 설정
    for r in range(N):
        # 인덱스 r의 문자열에 '2'이 존재한다면
        if board[r].find('2') > -1:
            # 해당 위치를 초기값으로 설정하고 반복을 종료한다.
            cnt_r, cnt_c = r, board[r].find('2')
            break

    visited = [[False] * N for _ in range(N)]
    # 탐색 순서 : 상우하좌
    dr = [-1, 0, 1, 0]
    dc = [0, 1, 0, -1]

    result = check_route(board, N, cnt_r, cnt_c)
    print("#{} {}".format(tc, int(result)))
