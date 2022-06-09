'''

Fail (Runtime error)

구매하는 날을 체크하는 과정과 매매를 진행하는 과정의 분리 때문에 느린건가?
잘 모르겠지만 결과는 맞다..!

'''

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    prices = list(map(int, input().split()))

    # 구매하는 날을 1로 체크
    check = [0 for _ in range(N)]
    max_price = prices[-1]
    for i in range(N - 2, -1, -1):
        if prices[i] < max_price:
            check[i] = 1
        elif prices[i] > max_price:
            max_price = prices[i]

    # 매매 진행
    cnt = 0
    cost = 0
    profit = 0
    for i in range(N):
        if check[i] == 1:
            cost += prices[i]
            cnt += 1
        else:
            profit += prices[i] * cnt - cost
            cnt = 0
            cost = 0

    # 출력
    print('#{0} {1}'.format(tc, profit))