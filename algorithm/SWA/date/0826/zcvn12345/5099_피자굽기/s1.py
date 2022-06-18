import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    p = list(map(int, input().split()))
    pizza = []
    for idx, i in enumerate(p):
        pizza.append((idx+1, i))
    Q = []
    for i in range(N):
        Q.append(pizza.pop(0))
    while len(Q) > 1:
        temp = Q.pop(0)
        temp = (temp[0], temp[1]//2)
        if temp[1] > 0:
            Q.append(temp)
        else:
            if len(pizza):
                Q.append(pizza.pop(0))

    print(f'#{tc} {Q[0][0]}')


