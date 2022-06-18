import sys
sys.stdin = open('input.txt')

for tc in range(1, int(input()) + 1):
    N, M = map(int, input().split())
    bits = format(M, 'b')

    cnt = 0
    for bit in bits[::-1]:
        if bit == '0':
            break
        elif bit == '1':
            cnt += 1
            if cnt == N:
                break

    if cnt == N:
        ans = 'ON'
    else:
        ans = 'OFF'

    print('#{} {}'.format(tc, ans))