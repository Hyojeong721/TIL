import sys
sys.stdin = open('input.txt')


def find_minprice(k, price):
    global minprice

    if price > minprice:
        return
    if k == N:
        minprice = price
        return

    for i in range(N):
        if not factory[i]:
            factory[i] = True
            find_minprice(k+1, price+V[k][i])
            factory[i] = False


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    V = [list(map(int, input().split())) for _ in range(N)]

    minprice = N * 99
    factory = [False] * N
    find_minprice(0, 0)
    print('#{} {}'.format(tc, minprice))