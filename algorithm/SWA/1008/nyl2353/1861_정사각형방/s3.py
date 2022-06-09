'''
    LIVE - 각 방의 좌표와 거리 (이어진 이전 방 수)저장하여 체크
        65,040 kb / 225 ms / 941 lines
'''
import sys
sys.stdin = open('input.txt')


dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

T = int(input())
for tc in range(1, T + 1):
    N = int(input())

    # A: 방 배열, pos: 각 방의 좌표
    A = []
    pos = [[0, 0]] * (N**2 + 1)
    for r in range(N):
        tmp = list(map(int, input().split()))
        for c in range(N):
            pos[tmp[c]] = [r, c]
        A.append(tmp)

    # dist: 이전 방들로 되돌아 갈 수 있는 거리-1 (default=1)
    # max_move: start_room 에서 시작해 최대 이동 가능한 방 수
    dist = [1] * (N**2 + 1)
    max_move = 1
    for idx in range(2, N**2 + 1):
        if abs(pos[idx][0]-pos[idx-1][0]) + abs(pos[idx][1]-pos[idx-1][1]) == 1:
            dist[idx] += dist[idx-1]
            if dist[idx] > max_move:
                max_move = dist[idx]

    for idx in range(1, N**2+1):
        if dist[idx] == max_move:
            end_room = idx
            break
    start_room = end_room - max_move + 1

    print('#{} {} {}'.format(tc, start_room, max_move))