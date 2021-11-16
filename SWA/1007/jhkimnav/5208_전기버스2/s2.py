import sys

sys.stdin = open('input.txt')


def dfs(bus_idx, fuel, change_cnt):
    global min_change

    #  0번째 정류장이 아닌데, 연료가 없는 경우
    if not fuel or change_cnt > min_change:
        return

    if bus_idx == N - 1:
        if change_cnt < min_change:
            min_change = change_cnt
            return

    else:
        fuel -= 1
        dfs(bus_idx + 1, fuel, change_cnt)

        fuel = charge_capa[bus_idx]
        dfs(bus_idx + 1, fuel, change_cnt+1)


T = int(input())

for tc in range(1, T + 1):
    N_list = list(map(int, input().split()))
    N = N_list[0]

    charge_capa = N_list[1:]
    min_change = N + 1
    bus_idx = 0
    change_cnt = 0


    dfs(bus_idx, 1, 0)

    print('#{} {}'.format(tc, min_change-1))
