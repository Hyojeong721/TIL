from itertools import combinations
import sys
sys.stdin = open('input.txt')

T = int(input())
superset = list(range(1, 13))

for tc in range(1, T + 1):
    N, K = list(map(int, input().split()))
    lst = list(combinations(superset, N))
    cnt = 0
    for i in lst:
        if sum(i) == K:
            cnt += 1

    print('#{} {}'.format(tc, cnt))