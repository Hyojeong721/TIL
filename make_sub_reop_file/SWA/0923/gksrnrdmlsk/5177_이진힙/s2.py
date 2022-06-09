# 힙 직접 구현
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = []
    temp = [0] + list(map(int, input().split()))
    for idx, value in enumerate(temp):
        # 일단 해당 값을 push하고,
        heap.append(value)
        while idx:
            # 부모 노드가 자식노드보다 크면 바꿔준다!
            if heap[idx // 2] > heap[idx]:
                heap[idx // 2], heap[idx] = heap[idx], heap[idx // 2]
                idx //= 2

            else:
                break
    total = 0
    # 조상노드 시작
    ancestor = N // 2
    # 조상노드 탐색
    while ancestor:
        total += heap[ancestor]
        ancestor //= 2

    print('#{} {}'.format(tc, total))
