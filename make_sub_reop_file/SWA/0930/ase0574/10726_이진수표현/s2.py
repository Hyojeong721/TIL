# 9441/100000
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    # 마지막 N개 비트
    N, M = map(int, input().split())
    num_2 = bin(M)[2:]

    for n in range(len(num_2)-1, len(num_2)-N+1, -1):
        if len(num_2) < N:
            ans = 'OFF'
            break

        if num_2[n] == '1':
            pass
            if n == len(num_2)-N+2:
                ans = 'ON'
        else:
            ans = 'OFF'
            break

    print("#{} {}".format(tc, ans))


