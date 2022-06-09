import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = float(input())
    ans = ''

    start = 0.5
    cnt = 0
    while cnt < 12:
        cnt += 1

        # 1 또는 0
        if N >= start:
            ans += '1'
            N -= start
        else:
            ans += '0'

        start /= 2

        # 이진수 완성했으면 break
        if not N:
            break

    # 12자리까지 본 후 N이 남아있으면 overflow
    if N:
        ans = 'overflow'

    print('#{} {}'.format(tc, ans))

