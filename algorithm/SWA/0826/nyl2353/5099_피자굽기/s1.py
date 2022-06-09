import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    # N: 화덕크기, M: 피자개수, C: 각 피자위의 치즈, numbers: 1 ~ M의 숫자
    N, M = list(map(int, input().split()))
    C = list(map(int, input().split()))
    numbers = [i + 1 for i in range(M)]

    # 화덕 안/밖의 피자/피자인덱스
    in_pizza = C[:N]
    in_number = numbers[:N]
    out_pizza = C[N:]
    out_number = numbers[N:]

    # 화덕 안에 피자가 하나만 남을 때까지
    while len(in_pizza) != 1:
        # 한 바퀴 돌고 왔을 떄의 치즈 양 저장
        in_pizza[0] //= 2

        # 치즈 안 남았으면, dequeue하고 새로운 피자 enqueue
        if not in_pizza[0]:
            in_pizza.pop(0)
            in_number.pop(0)
            if len(out_pizza):
                in_pizza.append(out_pizza[0])
                out_pizza.pop(0)
                in_number.append(out_number[0])
                out_number.pop(0)

        # 치즈 남았으면, 맨 뒤로 보냄
        else:
            in_pizza.append(in_pizza.pop(0))
            in_number.append(in_number.pop(0))

    print('#{} {}'.format(tc, in_number[0]))