import sys

sys.stdin = open('input.txt')

T = int(input())


def check_total(i, n):

    if i >= 12:
        total.append(n)
        return

    if lst[i] == 0:
        check_total(i+1, n)
    else:
        if lst[i] * D < M:
            check_total(i+1, n+lst[i]*D)
        else:
            check_total(i+1, n+M)
        check_total(i+3, n+M3)


for tc in range(1, T + 1):
    D, M, M3, Y = map(int, input().split())
    lst = list(map(int, input().split()))
    total = []

    check_total(0, 0)

    if min(total) > Y:
        answer = Y
    else:
        answer = min(total)

    print('#{} {}'.format(tc, answer))
