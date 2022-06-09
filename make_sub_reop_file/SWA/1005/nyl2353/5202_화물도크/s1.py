import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    times = [list(map(int, input().split())) for _ in range(N)]
    times.sort(key=lambda x: x[1])

    cnt = 0
    e = 0
    while True:
        for idx, time in enumerate(times):
            if time[0] >= e:
                cnt += 1
                e = time[1]
                break
        if idx == len(times)-1:
            break

    print('#{} {}'.format(tc, cnt))