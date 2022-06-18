import sys
sys.stdin = open('input.txt')

def count_charge(K, N, stops):
    prestop = 0
    count = 0
    check_if_can_go = 0
    stops.append(N)
    while prestop < N:          # prestop <= N
        for nextstop in range(prestop+K, prestop, -1):
            if nextstop in stops:
                prestop = nextstop
                count += 1
                check_if_can_go = 1
                break
            else:
                check_if_can_go = 0
        if check_if_can_go == 0:
            return 0

    if prestop >= N:
        count -= 1
        return count
    else:
        return 0

T = int(input())

for tc in range(1, T + 1):
    K, N, M = map(int, input().split())
    stops = list(map(int, input().split()))
    print('#{} {}'.format(tc, count_charge(K, N, stops)))