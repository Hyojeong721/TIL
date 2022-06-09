import sys
sys.stdin = open('input.txt')


def div(num):
    return (int(num) + 1) // 2


T = int(input())
for tc in range(1, T + 1):
    # 방 이동을 저장
    N = int(input())
    moves = [list(map(div, input().split())) for _ in range(N)]

    # 방 번호에 따른 리스트
    corridor = [0] * 201
    for move in moves:
        if move[0] > move[1]:
            move[0], move[1] = move[1], move[0]

        for j in range(move[0], move[1] + 1):
            corridor[j] += 1

    # 최대 겹친 횟수
    maximum = 0
    for n in corridor:
        if maximum < n:
            maximum = n

    print('#{0} {1}'.format(tc, maximum))