'''
    LIVE - 연속된 1 (다음 방으로 갈 수 있는지 유무)의 개수 체크
        60,812 kb / 229 ms / 887 lines
'''
import sys
sys.stdin = open('input.txt')


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

def is_movable(r, c):
    """
    r행 c열에서 다음 방번호로 이동할 수 있으면 True, 없으면 False 를 반환.

    """
    for k in range(4):
        nr = r + dr[k]
        nc = c + dc[k]
        if nr < 0 or nc < 0 or nr >= N or nc >= N: continue
        if A[nr][nc] == A[r][c] + 1:
            return True
    return False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    A = [list(map(int, input().split())) for _ in range(N)]

    # movable: 다음 방으로 갈 수 있는지 유무 (1 or 0)
    movable = [0] * (N**2 + 1)
    for r in range(N):
        for c in range(N):
            if is_movable(r, c):
                movable[A[r][c]] = 1

    # max_move: start_room 에서 시작해 최대 이동 가능한 방 수
    max_move = 1
    start_room = N**2 + 1
    for idx in range(N**2-1, -1, -1):
        if movable[idx]:
            tmp = movable[idx] + movable[idx+1]
            movable[idx] = tmp
            if tmp >= max_move:
                max_move = tmp
                start_room = idx

    print('#{} {} {}'.format(tc, start_room, max_move+1))
