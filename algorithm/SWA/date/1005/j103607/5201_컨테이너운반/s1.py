import sys
sys.stdin = open('input.txt')


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())   # N: 컨테이너 수  # M: 트럭 수
    weight = list(map(int, input().split()))   # N개의 컨테이너 무게
    truck = list(map(int, input().split()))   # M대의 트럭 적재용량

    # 큰 순서대로 정렬
    weight.sort(reverse=True)
    truck.sort(reverse=True)

    result = 0
    while weight and truck:   # 컨테이너나 트럭이 하나도 안남을 때까지
        container = weight.pop(0)
        if container <= truck[0]:
            truck.pop(0)
            result += container

    print('#{} {}'.format(tc, result))
