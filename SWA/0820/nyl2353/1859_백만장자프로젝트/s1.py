'''

체크과정과 매매과정을 합쳤더니 꽤나 빨라졌다 !

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 매매 진행
    profit = 0
    max_price = prices[-1]
    for i in range(N - 2, -1, -1):
        if max_price > prices[i]:
            profit += max_price - prices[i]
        else:
            max_price = prices[i]

    # 출력
    print('#{0} {1}'.format(tc, profit))