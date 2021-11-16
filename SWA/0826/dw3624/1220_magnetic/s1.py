import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    N = int(input())
    table = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0

    for x in range(N):
        state = 0
        for y in range(N):
            if state == 0 and table[y][x] == 1:
                state = 1
            if state == 1 and table[y][x] == 2:
                state = 0
                cnt += 1

    print('#{} {}'.format(tc, cnt))