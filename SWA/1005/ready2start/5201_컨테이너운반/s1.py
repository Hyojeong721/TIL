import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())

    # weights : 화물의 무게 / truck_loads: 트럭의 적재용량
    weights = [int(x) for x in input().split()]
    truck_loads = [int(x) for x in input().split()]

    weights.sort(reverse=True)
    truck_loads.sort(reverse=True)
    idx = 0
    total = 0

    # 무거운 것부터 차례대로 담을 수 있는지 확인한다.
    for weight in weights:
        if weight <= truck_loads[idx]:
            total += weight
            idx += 1
            # 더 이상 담을 트럭이 없다면 탐색을 종료한다.
            if idx > len(truck_loads) - 1:
                break

    print("#{} {}".format(tc, total))
