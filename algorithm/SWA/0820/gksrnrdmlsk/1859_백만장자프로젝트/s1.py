import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    money = 0
    temp = lst[-1]
    for i in range(N):
        if temp > lst[N - i - 1]:
            money += (temp - lst[N - i - 1])

        else:
            temp = lst[N - i - 1]
    print('#{} {}'.format(tc, money))

