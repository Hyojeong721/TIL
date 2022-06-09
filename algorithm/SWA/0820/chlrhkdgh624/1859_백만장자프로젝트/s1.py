import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    prices = list(map(int, input().split()))

    sell = 0
    profit = 0

    for i in range(N-1, -1, -1):
        if prices[i] > sell:
            sell = prices[i]
        if sell > prices[i]:
            profit += sell - prices[i]

    print(f'#{tc} {profit}')




