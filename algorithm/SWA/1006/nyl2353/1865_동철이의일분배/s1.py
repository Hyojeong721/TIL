'''
 < -> fail
 <= -> pass
'''

import sys
sys.stdin = open('input.txt')

def find_maxP(k, p):
    global maxP

    if p <= maxP:
        return

    if k == N:
        maxP = p
        return

    for i in range(N):
        if not visited[i]:
            visited[i] = 1
            find_maxP(k+1, p * P[k][i] / 100)
            visited[i] = 0


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    P = [list(map(int, input().split())) for _ in range(N)]

    maxP = 0
    visited = [0] * N
    find_maxP(0, 100)

    print('#{} {:.6f}'.format(tc, round(maxP, 6)))
