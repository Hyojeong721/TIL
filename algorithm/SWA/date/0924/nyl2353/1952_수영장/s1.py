import sys
sys.stdin = open('input.txt')


def find_minpay(month, pay):
    global minimum

    if month < 12:
        if not monthly[month]:
            find_minpay(month + 1, pay)
        else:
            temp = min(prices[1], prices[0] * monthly[month])
            find_minpay(month + 1, pay + temp)
            find_minpay(month + 3, pay + prices[2])
    elif pay < minimum:
        minimum = pay


T = int(input())
for tc in range(1, T + 1):
    prices = list(map(int, input().split()))
    monthly = list(map(int, input().split()))
    minimum = prices[3]
    find_minpay(0, 0)
    print('#{} {}'.format(tc, minimum))
