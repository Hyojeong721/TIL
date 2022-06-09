import sys
sys.stdin = open('sample_input.txt')

def get_greatest_weight(N, M, freights, trucks):
    freights.sort(reverse=True)
    trucks.sort(reverse=True)
    weight = 0
    while freights and trucks:
        truck = trucks[0]
        freight = freights.pop(0)
        if truck >= freight:
            weight += freight
            trucks.pop(0)
    else:
        return weight


T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    freights = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    print('#{} {}'.format(test_case, get_greatest_weight(N, M, freights, trucks)))