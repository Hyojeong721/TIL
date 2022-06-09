import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())  # N: 컨테이너 수, M: 트럭 수
    weights = sorted(list(map(int, input().split())))
    trucks = sorted(list(map(int, input().split())))
    B = []

    # for weight in weights:
    #     if weight in trucks:
    #         B.append(weight)
    #         weights.remove(weight)
    #         trucks.remove(weight)

    n = len(weights) - 1
    t = len(trucks) - 1

    while n >= 0 and t >= 0:
        if weights[n] > trucks[t]:
            n -= 1
        else:
            B.append(weights[n])
            weights = weights[:n] + weights[n+1:]
            trucks = trucks[:t] + trucks[t+1:]
            n -= 1
            t -= 1

    print(f'#{tc} {sum(B)}')



