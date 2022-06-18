import sys
from itertools import permutations
sys.stdin = open('input.txt')

for test_case in range(1, int(input())+1):
    N = int(input())
    p = [i for i in range(1, N)]
    e = [list(map(int, input().split())) for _ in range(N)]
    result = []

    for per in permutations(p):
        count = e[0][per[0]]
        for i in range(len(per)-1):
            count += e[per[i]][per[i+1]]
        count += e[per[-1]][0]
        result.append(count)

    print('#{} {}'.format(test_case, min(result)))