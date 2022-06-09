import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())  # 화덕의 크기, 피자의 개수
    Ci = list(map(int, input().split()))
    queue = []
    pizza_order = []
    idx = 0

    while len(Ci) or len(queue):

        if idx >= N:
            p = queue.pop(0)
            pi = pizza_order.pop(0)
            p = p // 2
            if p > 0:
                queue.append(p)
                pizza_order.append(pi)
            if len(queue) == 1:
                break
        if len(queue) < N and len(Ci):
            s = Ci.pop(0)
            idx += 1
            queue.append(s)
            pizza_order.append(idx)


    print('#{} {}'.format(tc, pizza_order[0]))