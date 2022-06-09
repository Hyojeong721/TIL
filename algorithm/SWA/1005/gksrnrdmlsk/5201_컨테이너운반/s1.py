import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    containers = list(map(int, input().split()))
    trucks = list(map(int, input().split()))
    containers.sort()
    trucks.sort()
    total = 0
    while containers and trucks:
        if containers[-1] <= trucks[-1]:
            total += containers.pop()
            trucks.pop()
        else:
            containers.pop()
    print('#{} {}'.format(tc, total))
