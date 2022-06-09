import sys

sys.stdin = open("input.txt", "r")

for tc in range(1, int(input()) + 1):
    K, N, M = map(int, input().split())

    number = list(map(int, input().split()))

    ev = [0] * (N + 1)
    for i in number:
        ev[i] = 1
    visited = 0
    now = 0
    dis = K

    while now < N:
        if now + K >= N:
            break
        else:
            if ev[now + dis] == 1:
                visited += 1
                now += dis
                dis = K
            else:
                dis -= 1
                if dis == 0:
                    visited = 0
                    break
    print('#{} {}'.format(tc, visited))