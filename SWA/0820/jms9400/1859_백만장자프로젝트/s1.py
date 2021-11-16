import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    day_price = list(map(int, input().split()))

    max_price = day_price[-1]
    result = 0

    for i in range(N-2, -1, -1):
        if day_price[i] < max_price:
            result += max_price - day_price[i]
        else:
            max_price = day_price[i]

    print('#{} {}'.format(tc, result))


