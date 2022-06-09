import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    n = int(input())
    lst = list(map(int, input().split())) + [0]

    sellV = lst[n-1]
    profit = 0
    for i in range(n-2, -1, -1):
        if sellV > lst[i]:
            profit += sellV - lst[i]
        else:
            sellV = lst[i]
    print(profit)

    # print('#{} {}'.format(tc, res))