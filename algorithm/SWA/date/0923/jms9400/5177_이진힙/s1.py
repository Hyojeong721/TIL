import heapq
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    lst = list(map(int, input().split()))
    heap = []
    for i in lst:
        heapq.heappush(heap, i)
    answer = 0

    while N > 1:
        N = N // 2
        answer += lst[N-1]

    print('#{} {}'.format(tc, answer))