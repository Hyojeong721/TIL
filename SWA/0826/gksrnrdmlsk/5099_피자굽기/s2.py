import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    pizzas = list(map(int, input().split()))
    last = M % N # 마지막 화덕에 들어갈 피자 수
    if not M % N:
        last = N
    pit = pizzas[-last:]
    cnt = 0
    while True:
        for i in range(last):
            if pit[i] == 0:
                pass
            else:
                pit[i] //= 2
                if pit[i] == 0:
                    cnt += 1
            if cnt == last - 1:
                break

        if cnt == last - 1:
            break
    for idx, value in enumerate(pit):
        if value != 0:
            result = idx

    print('#{} {}'.format(tc, (M - last) + result + 1))