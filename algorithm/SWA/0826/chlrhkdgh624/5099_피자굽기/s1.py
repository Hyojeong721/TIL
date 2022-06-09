import sys
sys.stdin = open('sample_input.txt')
T = int(input())


for tc in range(1, T+1):
    N, M = list(map(int, input().split()))  # N: 화덕 크기, M: 피자 개수
    pizzas = list(map(int, input().split()))
    idx = list(range(1, M+1))
    fire_pit = [0]*N
    q_idx = [0]*N
    done = []

    for i in range(N):
        fire_pit[i] = pizzas.pop(0)
        q_idx[i] = idx.pop(0)

    while fire_pit != [0]*N:
        for i in range(N):
            fire_pit[i] //= 2
            if fire_pit[i] == 0 and q_idx[i] not in done:
                done.append(q_idx[i])
                try:
                    fire_pit[i] = pizzas.pop(0)
                    q_idx[i] = idx.pop(0)
                except IndexError:
                    continue

    result = done[-1]
    print(f'#{tc} {result}')










