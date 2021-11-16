import sys
sys.stdin = open('sample_input.txt')


def get_greatest_num(N, apps):
    apps.sort(key=lambda app: app[1])
    last_done = apps[0][1]
    i = 1
    count = 1
    while i < N:
        if apps[i][0] >= last_done:
            count += 1
            last_done = apps[i][1]
        i += 1
    return count


T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    apps = [list(map(int, input().split())) for _ in range(N)]
    print('#{} {}'.format(test_case, get_greatest_num(N, apps)))
