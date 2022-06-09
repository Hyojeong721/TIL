import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    last = M % N
    if not M % N:
        last = N
    pizzas = list(map(int, input().split()))
    lst = []
    for i in range(1, last + 1):
        lst.append([i, pizzas[-last - 1 + i ]])
    cnt = 0
    while True:
        for j in range(last):
            if cnt == last - 1:
                break
            if lst[j][1] != 0:
                lst[j][1] //= 2
                if lst[j][1] == 0:
                    cnt += 1
        if cnt == last - 1:
            break

    for k in range(last):
        if lst[k][1] != 0:
            result = lst[k][0]

    print('#{} {}'.format(tc, M - (last - result)))
