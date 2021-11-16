import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    load = list(map(int, input().split()))
    truck = list(map(int, input().split()))
    load.sort(reverse=True)
    truck.sort(reverse=True)
    total = 0
    for i in load:
        if truck and i <= truck[0]:
            total += i
            truck.pop(0)
    print(f'#{tc} {total}')