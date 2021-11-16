import sys
sys.stdin = open('input.txt')

for tc in range(1, 11):
    input()
    table = [list(map(int, input().split())) for _ in range(100)]

    deadlock = 0

    # 1를 찾은 후, 2와 1이 번갈아 나오는 횟수를 센다.
    for c in range(100):
        cnt = 0
        for r in range(100):
            if not cnt % 2 and table[r][c] == 1:
                cnt += 1
            elif cnt % 2 and table[r][c] == 2:
                cnt += 1
        deadlock += cnt // 2

    print('#{} {}'.format(tc, deadlock))