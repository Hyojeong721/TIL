import sys
sys.stdin = open('input.txt')


T = int(input())

for t in range(1, T + 1):
    N = int(input())
    counts = []

    # (i = 4) => 만 이상 자리 수 : 50000원 + 10000원  (큰 금액부터 최대한 사용 => 그리디)
    # (i = 3) => 천의 자리 수 : 5000원 + 1000원
    # (i = 2) => 백의 자리 수 : 500원 + 100원
    # (i = 1) => 십의 자리 수 : 50원 + 10원
    for i in range(4, 0, -1):
        cost, N = divmod(N, 10 ** i)
        five, one = divmod(cost, 5)
        counts.append(five)
        counts.append(one)

    print('#{}'.format(t))

    for count in counts:
        print(count, end=" ")
    print()
