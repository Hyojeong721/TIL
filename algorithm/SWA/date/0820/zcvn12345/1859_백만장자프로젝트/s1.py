import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    price = list(map(int, input().split()))
    temp = price[-1]
    result = 0
    for i in range(len(price)-2, -1, -1):
        if price[i] > temp:
            temp = price[i]
        else:
            result = result + temp - price[i]
    print('#{0} {1}'.format(tc, result))

