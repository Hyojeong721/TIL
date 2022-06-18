
T = int(input())
for tc in range(1, T+1):
    N = float(input())
    ans = ''
    while len(ans) < 13:
        N *= 2
        if N >= 1:
            ans += '1'
            if N == 1:
                break
            N -= 1
        else:
            ans += '0'

    if len(ans) < 13:
        print('#{} {}'.format(tc, ans))
    else:
        print('#{} overflow'.format(tc))
