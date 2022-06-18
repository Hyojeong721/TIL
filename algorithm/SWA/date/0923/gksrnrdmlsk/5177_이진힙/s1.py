import sys
sys.stdin = open('input.txt')
import heapq

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    heap = [] # 힙을 만들기 위한 빈 리스트
    temp = list(map(int, input().split()))
    for i in temp:
        heapq.heappush(heap, i)
    total = 0
    idx = N // 2
    heap = [0] + heap
    while idx: # 조상 노드 탐색
        total += heap[idx]
        idx //= 2
    print('#{} {}'.format(tc, total))