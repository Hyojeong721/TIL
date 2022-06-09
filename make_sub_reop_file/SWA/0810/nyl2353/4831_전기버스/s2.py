import sys
sys.stdin = open('input.txt')

def get_charge_count(K, N, stations):
    charge_count = 0
    position = 0

    while position < N:
        for idx in range(position + K, position - 1, -1):
            if idx >= N:
                return charge_count
            elif idx in stations:
                charge_count += 1
                position = idx
                break


    return charge_count


T = int(input())
for tc in range(1, T + 1):
    K, N, M = list(map(int, input().split()))
    stations = list(map(int, input().split()))
    charge_count = get_charge_count(K, N, stations)
    print('#{0} {1}'.format(tc, charge_count))