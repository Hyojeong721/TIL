import sys
sys.stdin = open('input.txt')

T = int(input())

for TC in range(1, T+1):
    answer = 0
    N = int(input())
    price_list = list(map(int, input().split()))
    max_price = 0

    for i in range(N):
        if price_list[-1-i] > max_price:
            max_price = price_list[-1-i]
            continue
        else:
            answer += max_price - price_list[-1-i]

    print('#{} {}'.format(TC, answer))