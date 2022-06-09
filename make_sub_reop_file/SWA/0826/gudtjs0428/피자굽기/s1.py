import sys
sys.stdin = open('input.txt')

# 은영 waiting queue
# runtime에러

def make_pizza(N, M, cheeses):
    fire = []
    pizzas = []
    for i in range(1, M + 1):
        pizzas.append([i, cheeses[i-1]])
    for _ in range(N):
        fire.append(pizzas.pop(0))

    while pizzas:
        while fire[-1][1] != 0:
            fire.append(fire.pop(0))
            fire[-1][1] = fire[-1][1] // 2
        fire.pop()
        fire.append(pizzas.pop(0))

    while len(fire) != 1:
        while fire[-1][1] != 0:
            fire.append(fire.pop(0))
            fire[-1][1] = fire[-1][1] // 2
        fire.pop()

    return fire[0][0]


    # fire = []
    # last_pizza = [i for i in range(1, N + 1)]
    # pizza_num = N + 1
    # for _ in range(N):
    #     fire.append(cheeses.pop(0))
    #
    # while cheeses:
    #     while fire[-1] != 0:
    #         fire.append(fire.pop(0) // 2)
    #         last_pizza.append(last_pizza.pop(0))
    #     fire.pop()
    #     last_pizza.pop()
    #     fire.append(cheeses.pop(0))
    #     last_pizza.append(pizza_num)
    #     pizza_num += 1
    #
    # pizza_count = N
    # while len(fire) != 1:
    #     while fire[-1] != 0:
    #         fire.append(fire.pop(0) // 2)
    #         last_pizza.append(last_pizza.pop(0))
    #     fire.pop()
    #     last_pizza.pop()
    #     pizza_count -= 1
    #
    # return last_pizza[0]


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    cheeses = list(map(int, input().split()))
    print('#{} {}'.format(test_case, make_pizza(N, M, cheeses)))