import itertools

import sys
sys.stdin = open('test.txt')
T = int(input())

for tc in range(1, T+1):
    answer = 9999999999999
    n = int(input())
    arr = [[0 for _ in range(n+1)]]+[[0]+list(map(int, input().split())) for _ in range(n)]
    temp = list(itertools.permutations([i for i in range(2, n+1)], n-1))

    while temp:
        set = temp.pop()
        idx = 0
        res = arr[1][set[idx]]
        while idx < len(set):
            if idx+1 < len(set):
                res += arr[set[idx]][set[idx+1]]
            else:
                break
            idx += 1

        res += arr[set[-1]][1]
        answer = min(res, answer)

    print("#{} {}".format(tc, answer))