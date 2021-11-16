import sys
sys.stdin = open('input.txt')

def go(station):
    global charge, result, N

    if result <= charge:
        return

    if station >= N:
        if result >= charge:
            result = charge
        return

    for i in range(station+stations[station], station, -1):
        charge += 1
        go(i)
        charge -= 1


T = int(input())

for tc in range(1, T + 1):
    stations = list(map(int, input().split()))
    N = stations[0]
    result = 1000000000
    charge = 0
    go(1)

    print(f'#{tc} {result-1}')