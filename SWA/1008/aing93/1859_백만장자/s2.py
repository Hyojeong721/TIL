import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    n = int(input())
    a = list(map(int, input().split())) + [0]
    res = 0
    cnt = 0
    for i in range(n):
        if a[i+1] == 0:
            res += a[i] * cnt
            cnt = 0
            break

        if a[i] <= a[i+1]:
            res -= a[i]
            cnt += 1

        else:
            res += a[i] * cnt
            cnt = 0
    print('#{} {}'.format(tc, res))