'''
    재귀
    22번 test case 에서 더 못 들어감
'''

import sys
sys.stdin = open('input.txt')


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def find_maxmove(r, c, cnt, start):
    """
    Args:
        r: 현재 행의 인덱스
        c: 현재 열의 인덱스
        cnt: 현재까지 이동 횟수
        start: 시작 좌표 [행, 열]

    """
    global max_move, start_room, visited

    if cnt > max_move:
        max_move = cnt
        start_room = A[start[0]][start[1]]
    elif cnt == max_move:
        start_room = min(start_room, A[start[0]][start[1]])

    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
            if A[nr][nc] == A[r][c] + 1:
                visited[nr][nc] = True
                find_maxmove(nr, nc, cnt+1, start)
                visited[nr][nc] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]
    visited = [[False] * N for _ in range(N)]

    # max_move: start_room 에서 시작해 최대 이동 가능한 방 수
    max_move = 1
    start_room = N ** 2 + 1
    for r in range(N):
        for c in range(N):
            visited[r][c] = True
            find_maxmove(r, c, 1, [r, c])
            visited[r][c] = False

    print('#{} {} {}'.format(tc, start_room, max_move))
