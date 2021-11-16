'''
    LIVE - 가지치기
'''
import sys
sys.stdin = open('input.txt')


def find_minsum(idx, s, rs):
    global minsum

    if B <= s < minsum:
        minsum = s
        return
    if s + rs < B: return
    if s > minsum: return
    if idx == N: return

    find_minsum(idx+1, s+H[idx], rs-H[idx])
    find_minsum(idx+1, s, rs-H[idx])

T = int(input())
for tc in range(1, T + 1):
    N, B = map(int, input().split())
    H = list(map(int, input().split()))
    minsum = sum(H)
    find_minsum(0, 0, sum(H))
    print('#{} {}'.format(tc, minsum - B))
