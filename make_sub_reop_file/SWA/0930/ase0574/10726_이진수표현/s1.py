# 런타임 에러
import sys
sys.stdin = open('input.txt')

T = int(input())
def num_2(num):
    ans = ''
    for i in range(7,-1,-1):
        if num & (1<<i):
            ans += '1'
        else:
            ans += '0'
    return ans

for tc in range(1, T+1):
    # 마지막 N개 비트
    N, M = map(int, input().split())
    num = num_2(M)

    for j in range(7,7-N,-1):
        if num[j] == '1':
            if j == 8-N + 1:
                result = 'ON'
        else:
            result = 'OFF'
            break
    print('#{} {}'.format(tc, result))
