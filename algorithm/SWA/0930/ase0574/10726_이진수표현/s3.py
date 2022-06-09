# 9441/100000
import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    # 마지막 N개 비트
    N, M = map(int, input().split())

    num_2 = bin(M)[2:][-N:]

    if len(num_2) < N:
        ans = 'OFF'
    else:
        if '0' in num_2:
            ans = 'OFF'
        else:
            ans = 'ON'

    print("#{} {}".format(tc, ans))


