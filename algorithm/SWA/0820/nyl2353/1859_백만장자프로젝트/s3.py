'''

Fail (Runtime error)

내장 함수들을 발라서 빨라졌을 줄 알았는데 그래도 런타임 에러다 ㅠ
느리지만 결과는 맞다...

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 매매 진행
    profit = 0
    start = 0
    while start < N:
        maximum = prices.index(max(prices[start:]), start)
        if maximum == start:
            start += 1
        else:
            profit += prices[maximum] * (maximum - start)
            profit -= sum(prices[start:maximum])
            start = maximum + 1

    # 출력
    print('#{0} {1}'.format(tc, profit))