import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prices = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    num = [0] * 8
    ans = ''
    for idx, price in enumerate(prices):
        if N >= price:
            num[idx] = N // price
            N = N % price
        ans += str(num[idx]) + ' '
    print('#{}'.format(tc))
    print(ans)