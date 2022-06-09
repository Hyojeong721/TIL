import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = list(map(int, input().split()))
    Ci = list(map(int, input().split()))

    pizza = []
    for i in range(M):
        pizza.append([i+1, Ci[i]])

    oven = []
    for i in range(N):
        oven.append(pizza[i])
    i += 1

    while len(oven) > 1:
        x = oven.pop(0)
        if x[1] // 2 > 0:
            x[1] = x[1] // 2
            oven.append(x)
        else:
            if i < M:
                oven.append(pizza[i])
                i += 1

    print('#{}'.format(test_case), oven[0][0])